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

import pytest

# from scipy.io import loadmat
from mat4py import loadmat

from rws_bron.bronv3 import Well, generate_schemas, loadbronv3


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


def test_basic_read(testdata_filename: Path):
    data = loadmat(testdata_filename.__str__())
    assert len(data) > 0


def test_bronv2_read(testdata_filename_bronv2: Path):
    data = loadmat(testdata_filename_bronv2.__str__())
    assert len(data) > 0


def test_bronv3_read(testdata_filename_bronv3: Path):
    data = loadbronv3(testdata_filename_bronv3)
    assert data["GMW"][0].Adm.BROID == "GMW000000042649"
    assert data["GMW"][0].Well.XCoordinate == 157495.0
    assert isinstance(data["GMW"][0].Well, Well)


def test_well(renew_schemas):
    w = Well(
        Name="text",
        DeliveryContext="KRW",
        ConstructionStandard="onbekend",
        InitialFunction="kwaliteit",
        WellStability="onbekend",
        NITGCode="",
        Owner="01234567",
        Maintainer="012345676",
        HeadProtector="geen",
        HorPosMethod="RTKGPS10tot50cm",
        SurfaceLevel=0,
        VertPosMethodSurf="RTKGPS20tot100cm",
        XCoordinate=0,
        YCoordinate=0,
        VegType="gras",
        VegTypo="bla",
        OLGACode="asd",
        WellID=0,
    )

    assert w
