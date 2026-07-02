"""
Created on : Monday, 17th June 2024 12:00:14 pm
Author: Dirkjan Krijnders
Script type: C tool
-----
Last Modified: Monday, 17th June 2024 12:00:14 pm
Modified By: Dirkjan Krijnders
-----
Copyright 2024 - 2024 Antea Nederland B.V.
"""

from datetime import datetime, timedelta
from enum import Enum
from math import isnan
from typing import Any

from numpy.rec import array, fromrecords
from pydantic import BaseModel, model_validator


def matlab2datetime(matlab_datenum: float) -> datetime:
    day = datetime.fromordinal(int(matlab_datenum))
    dayfrac = timedelta(days=matlab_datenum % 1) - timedelta(days=366)
    return day + dayfrac


def datetime2matlab(dt: datetime) -> float:
    mdn = dt + timedelta(days=366)
    frac_seconds = (dt - datetime(dt.year, dt.month, dt.day, 0, 0, 0)).seconds / (
        24.0 * 60.0 * 60.0
    )
    frac_microseconds = dt.microsecond / (24.0 * 60.0 * 60.0 * 1000000.0)
    return mdn.toordinal() + frac_seconds + frac_microseconds


# @dataclass
class MatlabBaseModel(BaseModel):
    @model_validator(mode="before")
    @classmethod
    def empty_str_to_None(cls, data):
        if isinstance(data, dict):
            return {k: None if v == "" else v for k, v in data.items()}
        return data

    # @model_validator(mode="before")
    # @classmethod
    # def nan_to_None(cls, data):
    #     if isinstance(data, dict):
    #         return {
    #             k: None if isinstance(v, float) and isnan(v) else v
    #             for k, v in data.items()
    #         }
    #     return data

    def as_matlab_dict(
        self, only_children=False, use_structarray=False
    ) -> dict[str, Any]:
        base_dict = dict(self)
        matlab_dict = {}
        for k, v in base_dict.items():
            if v is None:
                matlab_dict[k] = ""
            elif isinstance(v, Enum):
                matlab_dict[k] = v.value
            elif isinstance(v, list) and use_structarray:
                matlab_dict[k] = list_to_structarray(v)
            elif isinstance(v, list):
                try:
                    matlab_dict[k] = [
                        li.as_matlab_dict() if isinstance(li, MatlabBaseModel) else li
                        for li in v
                    ]
                except AttributeError:
                    pass
            elif isinstance(v, MatlabBaseModel):
                matlab_dict[k] = v.as_matlab_dict()
            else:
                matlab_dict[k] = v
        if only_children or not use_structarray:
            return matlab_dict
        else:
            return fromrecords(
                [v for v in matlab_dict.values()], names=",".join(matlab_dict.keys())
            )

    def dict_compare(d1, d2):
        d1_keys = set(d1.keys())
        d2_keys = set(d2.keys())
        shared_keys = d1_keys.intersection(d2_keys)
        added = d1_keys - d2_keys
        removed = d2_keys - d1_keys
        modified = {o: (d1[o], d2[o]) for o in shared_keys if d1[o] != d2[o]}
        same = {o for o in shared_keys if d1[o] == d2[o]}
        return added, removed, modified, same

    def __eq__(self, other):
        if isinstance(other, MatlabBaseModel):
            if self.__dict__ == other.__dict__:
                return True
            else:
                for key in self.model_fields.keys():
                    if (
                        isinstance(getattr(self, key), float)
                        and isnan(getattr(self, key))
                        and isnan(getattr(other, key))
                    ):
                        continue

                    if getattr(self, key) != getattr(other, key):
                        return False
                return True
        return NotImplemented


def list_dict_to_structarray(list_: list[dict]):
    # keys = [key for key in list_[0].keys()]
    # arr = array([[li[k] for k in keys] for li in list_], names=",".join(keys))
    return array(list_)


def list_to_structarray(list_: list[MatlabBaseModel]):
    keys = [key for key in list_[0].model_fields.keys()]
    return fromrecords(
        [[getattr(li, k) for k in keys] for li in list_], names=",".join(keys)
    )
