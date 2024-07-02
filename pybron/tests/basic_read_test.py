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
from rws_bron.schema.BRONTypes import GMWTube, GMWWell
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
        / "2024-06-27 Testdata Provincie Utrecht (export).bron2"
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
        / "2024-07-01 Testdata Provincie Utrecht (export).bron2"
    )


@pytest.fixture
def testdata_filename_bronv3_write() -> Path:
    return (
        Path(os.path.dirname(os.path.realpath(__file__)))
        / "data"
        / "2024-07-01 Testdata Provincie Utrecht write-test.bron2"
    )


def test_bronv3_read(testdata_filename_bronv3: Path):
    data = loadbronv3(testdata_filename_bronv3)
    assert data.GMW[0].adm.BROID == "GMW000000042649"
    assert data.GMW[0].well.XCoordinate == 157495.0
    assert isinstance(data.GMW[0].well, GMWWell)
    for well in data.GMW:
        for ii_tube, _ in enumerate(well.tube):
            tube: GMWTube = well.tube[ii_tube]
            assert isinstance(tube.IsVarTubeDiam, float) or tube.IsVarTubeDiam is None


def test_bronv3_write(
    testdata_filename_bronv3: Path, testdata_filename_bronv3_write: Path
):
    data = loadbronv3(testdata_filename_bronv3)
    savebronv3(testdata_filename_bronv3_write, data)
    data_to_verify = loadbronv3(testdata_filename_bronv3_write)
    assert data.GMW[0].well.NITGCode == data_to_verify.GMW[0].well.NITGCode
    # assert data["GMW"][0].adm[0].bla == data_to_verify["GMW"][0].well.NITGCode
    for ii_gmw, _ in enumerate(data.GMW):
        if isinstance(data.GMW[ii_gmw].tube, list):
            for ii_tube, _ in enumerate(data.GMW[ii_gmw].tube):
                assert (
                    data.GMW[ii_gmw].tube[ii_tube]
                    == data_to_verify.GMW[ii_gmw].tube[ii_tube]
                )
        else:
            assert data.GMW[ii_gmw].tube == data_to_verify.GMW[ii_gmw].tube


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


@pytest.fixture
def adm_data() -> dict[str, Any]:
    return {
        "WellID": 0,
        "BROID": "BROID",
        "AccParty": "AccParty",
        "DvRespParty": "dv",
        "QualityRegime": 2,
        "ObjRgstrDateTime": 123.4,
        "LastRgstrEvent": 12,
        "WellCode": "sdaf",
    }


def test_well(renew_schemas, well_data):
    w = GMWWell(**well_data)

    assert w


def test_GMW(well_data, adm_data):
    gmw = GMW.from_dict({"Well": well_data, "Tube": [], "History": [], "Adm": adm_data})
    assert gmw.well.Name == "text"
    assert GMW.model_validate(gmw)
