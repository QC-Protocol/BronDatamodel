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

import os
from pathlib import Path
from typing import Any

import pytest

from rws_bron.bronv3 import loadbronv3, savebronv3
from rws_bron.schema.BRON import GMW
from rws_bron.schema.BRONTypes import Well
from rws_bron.schema_generation import generate_schemas

# from scipy.io import loadmat
# from mat4py import loadmat


@pytest.fixture
def renew_schemas():
    generate_schemas(
        target_directory=Path(os.path.dirname(os.path.realpath(__file__)))
        / ".."
        / "rws_bron"
        / "schema"
    )


@pytest.fixture
def testdata_filename() -> Path:
    return (
        Path(os.path.dirname(os.path.realpath(__file__)))
        / "data"
        / "2024-05-21 Testdata Provincie Utrecht (export).bron"
    )


@pytest.fixture
def testdata_filename_bronv2() -> Path:
    return (
        Path(os.path.dirname(os.path.realpath(__file__)))
        / "data"
        / "2024-05-21 Testdata Provincie Utrecht (export, v7.3).bron"
    )


@pytest.fixture
def testdata_filename_bronv3() -> Path:
    return (
        Path(os.path.dirname(os.path.realpath(__file__)))
        / "data"
        / "2024-06-10 Testdata Provincie Utrecht (export tables2structs d.GMW v6).bron"
    )


@pytest.fixture
def testdata_filename_bronv3_write() -> Path:
    return (
        Path(os.path.dirname(os.path.realpath(__file__)))
        / "data"
        / "2024-06-10 Testdata Provincie Utrecht (export tables2structs d.GMW v6) test.bron"  # noqa: E501
    )


def test_bronv3_read(testdata_filename_bronv3: Path):
    data = loadbronv3(testdata_filename_bronv3)
    assert data["GMW"][0].adm[0].BROID == "GMW000000042649"
    assert data["GMW"][0].well.XCoordinate == 157495.0
    assert isinstance(data["GMW"][0].well, Well)


def test_bronv3_write(
    testdata_filename_bronv3: Path, testdata_filename_bronv3_write: Path
):
    data = loadbronv3(testdata_filename_bronv3)
    savebronv3(testdata_filename_bronv3_write, data)
    data_to_verify = loadbronv3(testdata_filename_bronv3_write)
    assert data["GMW"][0].well.NITGCode == data_to_verify["GMW"][0].well.NITGCode
    # assert data["GMW"][0].adm[0].bla == data_to_verify["GMW"][0].well.NITGCode


@pytest.fixture
def well_data() -> dict[str, Any]:
    return {
        "Name": "text",
        "DeliveryContext": "KRW",
        "ConstructionStandard": "onbekend",
        "InitialFunction": "kwaliteit",
        "WellStability": "onbekend",
        "NITGCode": "",
        "Owner": "01234567",
        "Maintainer": "012345676",
        "HeadProtector": "geen",
        "HorPosMethod": "RTKGPS10tot50cm",
        "SurfaceLevel": 0,
        "VertPosMethodSurf": "RTKGPS20tot100cm",
        "XCoordinate": 0,
        "YCoordinate": 0,
        "VegType": "gras",
        "VegTypo": "bla",
        "OLGACode": "asd",
        "WellID": 0,
    }


def test_well(renew_schemas, well_data):
    w = Well(**well_data)

    assert w


def test_GMW(well_data):
    gmw = GMW.from_dict({"Well": well_data, "Tube": [], "History": [], "Adm": []})
    assert gmw.well.Name == "text"
    assert GMW.model_validate(gmw)
