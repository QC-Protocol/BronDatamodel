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

from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import scipy.io as spio

from rws_bron.schema.BRON import GMW
from rws_bron.schema.matlabbasemodel import datetime2matlab


def replace_empty(d: dict) -> dict:
    for k, v in d.items():
        if isinstance(v, list) and len(v) == 0:
            d[k] = ""
    return d


# def dict_to_model()


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
            elif isinstance(d[key], np.ndarray):
                d[key] = _tolist(d[key])
            else:
                d[key] = d[key]
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
        return replace_empty(d)

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
    data_py = loadmat(filename)
    data_py["GMW"] = [GMW.from_dict(gmw) for gmw in data_py["GMW"]]
    return data_py


def savebronv3(filename: Path, data: dict[str, list[dict]]):
    data_write: dict[str, list[dict[str, Any]]] = {
        "GMW": [gmw.as_matlab_dict() for gmw in data["GMW"]],
        "File": {
            "Name": filename.name,
            "Model": {
                "Nr": ["0", "9", "x.8", "(concept)"],
                "Date": datetime2matlab(datetime.now()),
            },
        },
    }
    spio.savemat(str(filename), data_write)
