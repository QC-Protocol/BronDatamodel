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
from typing import Any

from pydantic import BaseModel


def matlab2datetime(matlab_datenum: int) -> datetime:
    day = datetime.fromordinal(int(matlab_datenum))
    dayfrac = timedelta(days=matlab_datenum % 1) - timedelta(days=366)
    return day + dayfrac


def datetime2matlab(dt: datetime) -> int:
    #     ordinal = datetime.toordinal(dt)
    return 70000


class MatlabBaseModel(BaseModel):
    def as_matlab_dict(self) -> dict[str, Any]:
        base_dict = dict(self)
        matlab_dict = {}
        for k, v in base_dict.items():
            if v is None:
                matlab_dict[k] = ""
            elif isinstance(v, Enum):
                matlab_dict[k] = v.value
            elif isinstance(v, list):
                matlab_dict[k.capitalize()] = [li.as_matlab_dict() for li in v]

            elif isinstance(v, MatlabBaseModel):
                matlab_dict[k.capitalize()] = v.as_matlab_dict()
            else:
                matlab_dict[k] = v
        return matlab_dict
