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


def read_excel_schema(
    schema_filename: Optional[Path] = None, namespace: str = "GMW"
) -> DataFrame:
    if not schema_filename:
        schema_filename = (
            Path(os.path.dirname(os.path.realpath(__file__)))
            / ".."
            / ".."
            / ".."
            / "BROMappings"
            / f"Mapping en definitie BRO {namespace}.xlsx"
        )

    with schema_filename.open("rb") as fid:
        schema_df = read_excel(fid, header=0)
    schema_df.namespace = namespace

    return schema_df

idcategorical: list[str] = ["COMQualityRegime"]

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
    "[NaNBoolean]": "bool | float",
    "[-m+topw]": "float",
    "[Table]": "Any",
    "[m3 s−2 kg−1]": "float",
    "[kgm-3]": "float",
    "[Days]": "float",
    "[%]": "float",
    "[IDCategorical]": "COMQualityRegimeEnum"
}

categorical_map = {
    "VegType": "str",
    "VegTypo": "str",
    # "WellStability": "str",
    "LoggerBrand": "str",
    "LoggerType": "str",
    "Unit": "str",
    "ObjRgstrDateTime": "float",
    # "EventName": "Any",
    "RefLevel": "Any",
}


def source_attribute_map(schema: DataFrame) -> dict[str, str]:
    # sam = dict(zip(schema["TargetAttributeEng"], schema["SourceAttributeEng"]))
    sam = dict(
        zip(
            [value.strip() for value in schema["TargetAttributeEng"]],
            [
                value[0].upper() + value[1:].strip()
                for value in schema["SourceAttributeEng"]
            ],
        )
    )
    # sam["WellID"] = "WellID"
    # sam["BROID"] = "BROID"
    sam["HorizontalCrs"] = "CRS"
    sam["CorrectionReason"] = "BROID"
    sam2 = {(k[0].upper() + k[1:]).strip(): v for k, v in sam.items()}
    return sam2


def _excel_schema_to_pydantic_str(
    schema: DataFrame, enums: dict[str, Enum]
) -> dict[str, dict[str, dict[str, str]]]:
    sam = source_attribute_map(schema)
    classes: list[str] = [c for c in schema["TargetEntity"].unique() if c != "Afgeleid"]
    r: dict[str, dict[str, str]] = {}
    for c in classes:
        if c == "Geen":
            continue
        r[schema.namespace + c] = {}
        attrs = (
            schema[["TargetAttributeEng", "TargetDatatype", "SourceMin", "SourceMax"]]
            .where(schema["TargetEntity"] == c)
            .dropna()
            .set_index("TargetAttributeEng")
        )
        for attr, datatype in attrs.iterrows():
            if attr == "EventName":
                pass
            datatype_py = datatype["TargetDatatype"]
            datatype_name = datatype["TargetDatatype"]
            if datatype_name == "[Categorical]": # or datatype_name == "[CategoricalID]":
                if attr in categorical_map:
                    datatype_py = {
                        "type": categorical_map[attr],
                        "cardinality": [
                            datatype["SourceMin"],
                            datatype["SourceMax"],
                        ],
                    }
                else:
                    if datatype.name == "BROID":
                        pass
                    if datatype.name in sam:
                        namespace_enum = schema.namespace + sam[datatype.name] + "Enum"
                        if namespace_enum[:-4] not in enums.keys():
                            namespace_enum = "COM" + sam[datatype.name] + "Enum"
                        datatype_py = {
                            "type": namespace_enum,
                            "cardinality": [
                                datatype["SourceMin"],
                                datatype["SourceMax"],
                            ],
                        }
                    else:
                        if datatype.name == "EventData":
                            pass
                        namespace_enum = schema.namespace + datatype.name + "Enum"
                        if namespace_enum[:-4] not in enums.keys():
                            namespace_enum = "COM" + datatype.name + "Enum"
                        datatype_py = {
                            "type": namespace_enum,
                            "cardinality": [
                                datatype["SourceMin"],
                                datatype["SourceMax"],
                            ],
                        }
            else:
                if datatype_name in datatype_map:
                    datatype_py = {
                        "type": datatype_map[datatype_name],
                        "cardinality": [datatype["SourceMin"], datatype["SourceMax"]],
                    }
                else:
                    datatype_py = {
                        "type": "str",
                        "cardinality": [datatype["SourceMin"], datatype["SourceMax"]],
                    }
            r[schema.namespace + c][attr] = datatype_py

    return r

"""
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
"""

def read_excel_waardelijsten() -> dict[str, list[str]]:
    ps = {}
    for ns in ["GMW", "GMN", "GLD", "GAR", "COM"]:
        ps = {**ps, **read_excel_waardelijst(namespace=ns)}
    
    for ns in ["GMW", "GMN", "GLD"]:
        d = read_excel_gebeurtenis(namespace=ns)
        ps[ns + "EventName"] = d[ns + "EventName"]

    return ps

def read_excel_gebeurtenis(
        event_filename: Optional[Path] = None,
        namespace: str = "GMW"
) -> dict[str, list[str]]:
    if not event_filename:
        event_filename = (
            Path(os.path.dirname(os.path.realpath(__file__)))
            / ".."
            / ".."
            / ".."
            / "BROMappings"
            / f"Mapping BRO {namespace} Events.xlsx"
        )

    with event_filename.open("rb") as fid:
        event_df_sheets = read_excel(fid, header=0, sheet_name=None)

    d = dict()
    for _, sheet in event_df_sheets.items():
        d[namespace + "EventName"] = list(sheet["BronGebeurtenis"][0:].values)

    return d


def read_excel_waardelijst(
    category_filename: Optional[Path] = None, namespace: str = "GMW"
) -> dict[str, list[str]]:
    if not category_filename:
        category_filename = (
            Path(os.path.dirname(os.path.realpath(__file__)))
            / ".."
            / ".."
            / ".."
            / "BroCategoricals"
            / f"Waardelijsten BRO {namespace}.xlsx"
        )

    with category_filename.open("rb") as fid:
        category_df_sheets = read_excel(fid, header=0, sheet_name=None)

    d = dict()
    for sheetname, sheet in category_df_sheets.items():
        d[namespace + sheetname] = list(sheet["Codes"][1:].values)

    return d


def category_dict_to_pydantic_enum(df: dict[str, list[str]]) -> dict[str, Enum]:
    keys: list[str] = [
        key for key in df.keys() if key.lower() not in ["[afgeleid]", "[janeeonbekend]"]
    ]
    enums = {}
    # schema = read_excel_schema()
    # sam = source_attribute_map(schema)
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
        # if key in sam:
        #    enums[sam[key]] = enum
        # else:
        enums[key] = enum
    # del enums["Afgeleid"]
    # del enums["CRS"]
    # del enums["EventName"]
    # del enums["BROID"]
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
    key_translation = str.maketrans(
        {".": "_", ":": "_", "-": "_", "+": "_", " ": "_", "/": "_", "(": "_", ")": "_"}
    )
    with target_file.open("wt", encoding="utf-8") as fid:
        fid.write("# flake8: noqa\n")
        fid.write("from enum import Enum\n")

        for k, v in enums.items():
            if len(v) == 0:
                continue
            fid.write(f"\n\nclass {k}Enum(str, Enum):\n")
            if k == "COMQualityRegime":
                pass
            if k in idcategorical:
                for ii, field in enumerate(v):
                    fid.write(
                        f'    {field.value.translate(key_translation)} = {ii}\n'
                    )

            else:
                for field in v:
                    fid.write(
                        f'    {field.value.translate(key_translation)} = "{field.value}"\n'
                    )
            if "onbekend" in v._member_names_:
                fid.write("\n    @classmethod\n")
                fid.write("    def _missing_(cls, value):\n")
                fid.write("        return cls.onbekend\n")


def generate_pydantic_schemas(
    df_schema: DataFrame | list[DataFrame],
    enums: dict[str, Enum],
    target_directory: Optional[Path] = None,
    use_source_cardinality: Optional[bool] = False,
):
    if isinstance(df_schema, DataFrame):
        df_schema = [df_schema]
    if not target_directory:
        target_directory = Path(os.path.realpath(os.getcwd()))

    generate_pydantic_enums(enums=enums, target_file=target_directory / "BRONEnums.py")
    ps = {}
    for df in df_schema:
        ps = {**ps, **_excel_schema_to_pydantic_str(df, enums)}
    ps["GLDSource"]["Measurements"] = {"type": "list[GLDMeasurement]", "cardinality": ['Geen', 'Geen']}
    ps["GLDSource"]["Changes"] = {"type": "list[GLDChange]", "cardinality": ['Geen', 'Geen']}
    enum_list_str = [key + "Enum" for key, v in enums.items() if len(v) > 0]
    enum_list_str.sort()
    import_enum_str = ",\n    ".join(enum_list_str)

    with (target_directory / "BRONTypes.py").open("wt") as fid:
        fid.write("# flake8: noqa\n")
        fid.write("# This file is generated, do not change\n")
        fid.write("from typing import Any, Optional\n\n")
        fid.write("from pybron.schema.matlabbasemodel import MatlabBaseModel\n\n")
        fid.write(f"from .BRONEnums import (\n    {import_enum_str},\n)\n")
        fid.write("from .BRONManualTypes import GLDMeasurement, GLDChange\n\n")
        for k, v in ps.items():
            fid.write(f"\n\nclass {k}(MatlabBaseModel):\n")
            for k2, v2 in v.items():
                if (
                    use_source_cardinality
                    and isinstance(v2["cardinality"][0], int)
                    and v2["cardinality"][0] > 0
                ):
                    fid.write(f"    {k2}: {v2['type']}\n")
                else:
                    fid.write(f"    {k2}: Optional[{v2['type']}]\n")
