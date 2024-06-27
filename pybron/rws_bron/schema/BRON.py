"""
Created on : Tuesday, 18th June 2024 5:47:14 pm
Author: Dirkjan Krijnders
Script type: C tool
-----
Last Modified: Tuesday, 18th June 2024 5:47:14 pm
Modified By: Dirkjan Krijnders
-----
Copyright 2024 - 2024 Antea Nederland B.V.
"""

from rws_bron.schema.BRONTypes import (
    GLDAdm,
    GLDDossier,
    GLDHistory,
    GLDSource,
    GMNAdm,
    GMNHistory,
    GMNNet,
    GMNPoint,
    GMWAdm,
    GMWHistory,
    GMWTube,
    GMWWell,
)
from rws_bron.schema.matlabbasemodel import MatlabBaseModel


class GMW(MatlabBaseModel):
    well: GMWWell
    tube: list[GMWTube]
    history: list[GMWHistory]
    adm: list[GMWAdm]

    @classmethod
    def from_dict(cls, d: dict):
        gmw = cls(
            **{"well": GMWWell(**d["Well"]), "tube": [], "history": [], "adm": []}
        )
        if isinstance(d["Tube"], list):
            for tube in d["Tube"]:
                gmw.tube.append(GMWTube(**tube))
        else:
            gmw.tube.append(GMWTube(**d["Tube"]))
        if isinstance(d["History"], list):
            for history in d["History"]:
                gmw.history.append(GMWHistory(**history))
        else:
            gmw.history.append(GMWHistory(**d["History"]))
        if isinstance(d["Adm"], list):
            for adm in d["Adm"]:
                gmw.adm.append(GMWAdm(**adm))
        else:
            gmw.adm.append(GMWAdm(**d["Adm"]))
        return gmw


class GLD(MatlabBaseModel):
    source: list[GLDSource]
    adm: list[GLDAdm]
    dossier: list[GLDDossier]
    history: list[GLDHistory]

    @classmethod
    def from_dict(cls, d: dict):
        gld = cls(
            **{
                "adm": [],  # GLDAdm(**d["Adm"]),
                "source": [],  # GLDSource(**d["Source"]),
                "dossier": [],
                "history": [],
            }
        )
        if isinstance(d["Dossier"], list):
            for dossier in d["Dossier"]:
                gld.dossier.append(GLDDossier(**dossier))
        else:
            gld.dossier.append(GLDDossier(**d["Dossier"]))
        if isinstance(d["History"], list):
            for history in d["History"]:
                gld.history.append(GLDHistory(**history))
        else:
            gld.history.append(GLDHistory(**d["History"]))
        # if isinstance(d["Adm"], list):
        #     for adm in d["Adm"]:
        #         gld.adm.append(GLDAdm(**adm))
        # else:
        #     gld.adm.append(GLDAdm(**d["Adm"]))

        return gld


class GMN(MatlabBaseModel):
    adm: GMNAdm
    net: GMNNet
    point: GMNPoint
    history: GMNHistory

    @classmethod
    def from_dict(cls, d: dict):
        gmn = cls(**{"adm": GMNAdm(**d["Adm"]), "net": [], "history": [], "point": []})
        return gmn
