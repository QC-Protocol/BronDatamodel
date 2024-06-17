"""
Created on : Monday, 10th June 2024 1:57:40 pm
Author: Dirkjan Krijnders
Script type: C tool
-----
Last Modified: Monday, 10th June 2024 1:57:41 pm
Modified By: Dirkjan Krijnders
-----
Copyright 2024 - 2024 Antea Nederland B.V.
"""

from pathlib import Path
from typing import Optional

import numpy as np
import scipy.io as spio

from rws_bron.schema.excel_shema import (
    category_dataframe_to_pydantic_enum,
    generate_pydantic_schemas,
    read_excel_categories,
    read_excel_schema,
)

from .schema.BRONTypes import Well


def generate_schemas(target_directory: Optional[Path] = None):
    df_schema = read_excel_schema()
    df_cat = read_excel_categories()
    enums = category_dataframe_to_pydantic_enum(df_cat)
    generate_pydantic_schemas(df_schema, enums, target_directory)


def loadmat(filename):
    """
    this function should be called instead of direct spio.loadmat
    as it cures the problem of not properly recovering python dictionaries
    from mat files. It calls the function check keys to cure all entries
    which are still mat-objects
    """

    def _check_keys(d):
        """
        checks if entries in dictionary are mat-objects. If yes
        todict is called to change them to nested dictionaries
        """
        for key in d:
            if isinstance(d[key], spio.matlab.mat_struct):
                d[key] = _todict(d[key])
        return d

    def _todict(matobj):
        """
        A recursive function which constructs from matobjects nested dictionaries
        """
        d = {}
        for strg in matobj._fieldnames:
            elem = matobj.__dict__[strg]
            if isinstance(elem, spio.matlab.mat_struct):
                d[strg] = _todict(elem)
            elif isinstance(elem, np.ndarray):
                d[strg] = _tolist(elem)
            else:
                d[strg] = elem
        return d

    def _tolist(ndarray):
        """
        A recursive function which constructs lists from cellarrays
        (which are loaded as numpy ndarrays), recursing into the elements
        if they contain matobjects.
        """
        elem_list = []
        for sub_elem in ndarray:
            if isinstance(sub_elem, spio.matlab.mat_struct):
                elem_list.append(_todict(sub_elem))
            elif isinstance(sub_elem, np.ndarray):
                elem_list.append(_tolist(sub_elem))
            else:
                elem_list.append(sub_elem)
        return elem_list

    data = spio.loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_keys(data)


def loadbronv3(filename: Path) -> dict[str, list[dict]]:
    data = loadmat(filename)

    for index in range(len(data["GMW"])):
        d = dict(
            zip(
                data["GMW"][index].Well._fieldnames,
                [
                    getattr(data["GMW"][index].Well, fn)
                    for fn in data["GMW"][index].Well._fieldnames
                ],
            )
        )
        for k, v in d.items():
            if not v:
                d[k] = None
        data["GMW"][index].Well = Well(**d)

    return data
