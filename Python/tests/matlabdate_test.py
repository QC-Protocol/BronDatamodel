"""
Created on : Monday, 10th June 2024 11:44:04 am
Author: Dirkjan Krijnders
Script type: C tool
-----
Last Modified: Monday, 10th June 2024 11:44:04 am
Modified By: Dirkjan Krijnders
-----
Copyright 2024 - 2024 Antea Nederland B.V.
"""

from datetime import datetime

import pytest

from pybron.schema.matlabbasemodel import datetime2matlab, matlab2datetime


def test_datetime2matlab():
    to_test = 70000
    dt = matlab2datetime(to_test)
    expected = 70000
    assert datetime2matlab(dt) == expected
    dt = datetime(2012, 2, 13, 6, 56, 2, 619000)
    expected = 734912.28891203704
    assert expected == pytest.approx(datetime2matlab(dt))
