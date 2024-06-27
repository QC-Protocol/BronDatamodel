"""
Created on : Tuesday, 11th June 2024 8:26:38 am
Author: Dirkjan Krijnders
Script type: C tool
-----
Last Modified: Tuesday, 11th June 2024 8:26:38 am
Modified By: Dirkjan Krijnders
-----
Copyright 2024 - 2024 Antea Nederland B.V.
"""

from rws_bron.schema.excel_shema import (
    _excel_schema_to_pydantic_str,
    category_dataframe_to_pydantic_enum,
    category_dict_to_pydantic_enum,
    read_excel_categories,
    read_excel_schema,
    read_excel_waardelijst,
    read_excel_waardelijsten,
    source_attribute_map,
)


def test_read_excel_schema():
    df = read_excel_schema()
    assert df["TargetEntity"][6] == "Well"


def test_read_excel_schema_GMN():
    df = read_excel_schema(namespace="GMN")
    assert df["TargetEntity"][6] == "Net"


def test_read_excel_schema_GLD():
    df = read_excel_schema(namespace="GLD")
    assert df["TargetEntity"][6] == "Adm"


def test_source_attribute_map_GMW():
    df_schema = read_excel_schema()
    sam = source_attribute_map(df_schema)
    assert sam["ConstructionStandard"] == "ConstructionStandard"


def test_source_attribute_map_GLD():
    df_schema = read_excel_schema(namespace="GLD")
    sam = source_attribute_map(df_schema)
    assert sam["QualityRegime"] == "QualityRegime"


def test_source_attribute_map_GMN():
    df_schema = read_excel_schema(namespace="GMN")
    sam = source_attribute_map(df_schema)
    assert sam["GroundwaterAspect"] == "GroundwaterAspect"


def test_convert_excel_schema_GMW():
    df_schema = read_excel_schema()
    df_cat = read_excel_waardelijst()
    enums = category_dict_to_pydantic_enum(df_cat)
    types = _excel_schema_to_pydantic_str(df_schema, enums)
    assert types["GMWWell"]["ConstructionStandard"] == "GMWConstructionStandardEnum"


def test_convert_excel_schema_GMN():
    df_schema = read_excel_schema(namespace="GMN")
    df_cat = read_excel_waardelijst()
    enums = category_dict_to_pydantic_enum(df_cat)
    types = _excel_schema_to_pydantic_str(df_schema, enums)
    assert types["GMNNet"]["GroundwaterAspect"] == "GMNGroundwaterAspectEnum"


def test_convert_excel_schema_GLD():
    df_schema = read_excel_schema(namespace="GLD")
    df_cat = read_excel_waardelijst()
    enums = category_dict_to_pydantic_enum(df_cat)
    types = _excel_schema_to_pydantic_str(df_schema, enums)
    assert types["GLDSource"]["Drift"] == "float"
    assert types["GLDSource"]["Gravity"] == "float"


def test_read_excel_waardelijsten():
    df = read_excel_waardelijst()
    assert "kokerNietMetaal" in df["GMWWellHeadProtector"]


def test_read_excel_categories():
    df = read_excel_categories()
    assert df["beschermconstructie"][2] == "kokerNietMetaal"


def test_category_dataframe_to_pydantic_enum():
    df = read_excel_categories()
    enums = category_dataframe_to_pydantic_enum(df)
    assert len(enums["HeadProtector"]) == 8


def test_category_dict_to_pydantic_enum():
    df = read_excel_waardelijst()
    enums = category_dict_to_pydantic_enum(df)
    assert len(enums["GMWWellHeadProtector"]) == 8


def test_all_namespaces_category_dict_to_pydantic_enum():
    df = read_excel_waardelijsten()
    enums = category_dict_to_pydantic_enum(df)
    assert len(enums["GMWWellHeadProtector"]) == 8
    assert len(enums["GMNGroundwaterAspect"]) == 3
