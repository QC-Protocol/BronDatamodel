"""
Created on : Tuesday, 11th June 2024 8:28:48 am
Author: Dirkjan Krijnders
Script type: C tool
-----
Last Modified: Tuesday, 11th June 2024 8:28:48 am
Modified By: Dirkjan Krijnders
-----
Copyright 2024 - 2024 Antea Nederland B.V.
"""

import logging
import os
from enum import Enum
from pathlib import Path
from typing import Optional

from pandas import DataFrame, read_excel


def read_excel_schema(schema_filename: Optional[Path] = None) -> DataFrame:
    if not schema_filename:
        schema_filename = (
            Path(os.path.dirname(os.path.realpath(__file__)))
            / ".."
            / ".."
            / "BronDataModel"
            / "BROMappings"
            / "Mapping en definitie BRO GMW.xlsx"
        )

    with schema_filename.open("rb") as fid:
        schema_df = read_excel(fid, header=0)

    return schema_df


datatype_map = {
    "[ID]": "int",
    "[BroID]": "str",
    "[KvKNumber]": "str",
    "[Integer]": "int",
    "[Uint8]": "int",
    "[PutCode]": "str",
    "[MatlabDate]": "float",
    "[NITGCode]": "str",
    "[m]": "float",
    "[m+ref]": "float",
    "[NaNBoolean]": "float",
    "[-m+topw]": "float",
    "[Table]": "Any",
}

categorical_map = {
    "VegType": "str",
    "VegTypo": "str",
    "WellStability": "str",
    "LoggerBrand": "str",
    "LoggerType": "str",
    "QualityRegime": "int",
    "ObjRgstrDateTime": "float",
    "EventName": "Any",
}


def source_attribute_map(schema: DataFrame) -> dict[str, str]:
    # sam = dict(zip(schema["TargetAttributeEng"], schema["SourceAttributeEng"]))
    sam = dict(zip(schema["SourceAttributeEng"], schema["TargetAttributeEng"]))
    # sam["WellID"] = "WellID"
    # sam["BROID"] = "BROID"
    sam["HorizontalCrs"] = "CRS"
    sam["CorrectionReason"] = "BROID"
    sam2 = {(k[0].upper() + k[1:]).strip(): v for k, v in sam.items()}
    return sam2


def _excel_schema_to_pydantic_str(
    schema: DataFrame, enums: dict[str, Enum]
) -> dict[str, dict[str, str]]:
    classes: list[str] = [c for c in schema["TargetEntity"].unique() if c != "Afgeleid"]
    r: dict[str, dict[str, str]] = {}
    for c in classes:
        r[c] = {}
        attrs = (
            schema[["TargetAttributeEng", "TargetDatatype"]]
            .where(schema["TargetEntity"] == c)
            .dropna()
            .set_index("TargetAttributeEng")
        )
        for attr, datatype in attrs.iterrows():
            datatype_py = datatype
            datatype_name = datatype.values[0]
            if datatype_name == "[Categorical]":
                if attr in categorical_map:
                    datatype_py = categorical_map[attr]
                else:
                    if datatype.name == "BROID":
                        pass
                    datatype_py = datatype.name + "Enum"
            else:
                if datatype_name in datatype_map:
                    datatype_py = datatype_map[datatype_name]
                else:
                    datatype_py = "str"
            r[c][attr] = datatype_py

    return r


def read_excel_categories(category_filename: Optional[Path] = None) -> DataFrame:
    if not category_filename:
        category_filename = (
            Path(os.path.dirname(os.path.realpath(__file__)))
            / ".."
            / "data"
            / "BROObject - GMW data file NL samengevoegd (v2.x).xlsx"
        )

    with category_filename.open("rb") as fid:
        category_df = read_excel(fid, sheet_name="Waardelijsten", header=0)

    return category_df


def read_excel_waardelijsten(
    category_filename: Optional[Path] = None,
) -> dict[str : list[str]]:
    if not category_filename:
        category_filename = (
            Path(os.path.dirname(os.path.realpath(__file__)))
            / ".."
            / ".."
            / "BronDataModel"
            / "BroCategoricals"
            / "Waardelijsten BRO GMW.xlsx"
        )

    with category_filename.open("rb") as fid:
        category_df_sheets = read_excel(fid, header=0, sheet_name=None)

    d = dict()
    for sheetname, sheet in category_df_sheets.items():
        d[sheetname] = list(sheet["Codes"][1:].values)

    return d


def category_dict_to_pydantic_enum(df: dict[str, list[str]]) -> dict[str, Enum]:
    keys: list[str] = [
        key for key in df.keys() if key.lower() not in ["[afgeleid]", "[janeeonbekend]"]
    ]
    enums = {}
    schema = read_excel_schema()
    sam = source_attribute_map(schema)
    for key in keys:
        enum = Enum(
            key,
            {
                value: value
                for value in df[key]
                if isinstance(value, str)
                and value != "Geel gearceerd = 'Waarde alleen IMBRO/A'"
            },
        )
        if key in sam:
            enums[sam[key]] = enum
    del enums["Afgeleid"]
    del enums["CRS"]
    del enums["EventName"]
    del enums["BROID"]
    return enums


def category_dataframe_to_pydantic_enum(df: DataFrame) -> dict[str, Enum]:
    keys: list[str] = [
        key for key in df.columns if key not in ["[afgeleid]", "[JaNeeOnbekend]"]
    ]
    enums = {}
    schema = read_excel_schema()
    sam = source_attribute_map(schema)
    for key in keys:
        enum = Enum(
            key,
            {
                value: value
                for value in df[key]
                if isinstance(value, str)
                and value != "Geel gearceerd = 'Waarde alleen IMBRO/A'"
            },
        )
        enums[sam[key]] = enum
    del enums["Afgeleid"]
    return enums


def generate_pydantic_enums(enums: dict[str, Enum], target_file: Path):
    logger = logging.getLogger(__name__)
    logger.warning(f"Writing enums to {target_file}")
    with target_file.open("wt") as fid:
        fid.write("from enum import Enum\n")

        for k, v in enums.items():
            fid.write(f"\n\nclass {k}Enum(str, Enum):\n")
            for field in v:
                fid.write(f'    {field.value} = "{field.value}"\n')


def generate_pydantic_schemas(
    df_schema: DataFrame,
    enums: dict[str, Enum],
    target_directory: Optional[Path] = None,
):
    if not target_directory:
        target_directory = Path(os.path.realpath(os.getcwd()))

    generate_pydantic_enums(enums=enums, target_file=target_directory / "BRONEnums.py")
    ps = _excel_schema_to_pydantic_str(df_schema, enums)
    enum_list_str = [key + "Enum" for key, _ in enums.items()]
    enum_list_str.sort()
    import_enum_str = ",\n    ".join(enum_list_str)
    with (target_directory / "BRONTypes.py").open("wt") as fid:
        fid.write("from typing import Optional, Any\n\n")
        fid.write("from rws_bron.schema.matlabbasemodel import MatlabBaseModel\n\n")
        fid.write(f"from .BRONEnums import (\n    {import_enum_str},\n)\n")
        for k, v in ps.items():
            fid.write(f"\n\nclass {k}(MatlabBaseModel):\n")
            for k2, v2 in v.items():
                fid.write(f"    {k2}: Optional[{v2}]\n")
