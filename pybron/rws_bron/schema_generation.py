"""
Created on : Wednesday, 19th June 2024 1:24:18 pm
Author: Dirkjan Krijnders
Script type: C tool
-----
Last Modified: Wednesday, 19th June 2024 1:24:18 pm
Modified By: Dirkjan Krijnders
-----
Copyright 2024 - 2024 Antea Nederland B.V.
"""

from pathlib import Path
from typing import Optional

from rws_bron.schema.excel_shema import (
    category_dict_to_pydantic_enum,
    generate_pydantic_schemas,
    read_excel_schema,
    read_excel_waardelijsten,
)


def generate_schemas(target_directory: Optional[Path] = None):
    df_schema = read_excel_schema()
    df_cat = read_excel_waardelijsten()
    enums = category_dict_to_pydantic_enum(df_cat)
    generate_pydantic_schemas(df_schema, enums, target_directory)
