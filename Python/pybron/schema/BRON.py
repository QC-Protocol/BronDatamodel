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

from pybron.schema.BRONManualTypes import GLDMeasurement, COMChange
from pybron.schema.BRONTypes import (
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
from pybron.schema.matlabbasemodel import MatlabBaseModel


class GMW(MatlabBaseModel):
    Well: GMWWell
    Tube: list[GMWTube]
    History: list[GMWHistory]
    Adm: GMWAdm

    @classmethod
    def from_dict(cls, d: dict):
        gmw = cls(
            **{
                "Well": GMWWell(**d["Well"]),
                "Tube": [],
                "History": [],
                "Adm": GMWAdm(**d["Adm"]),
            }
        )
        if isinstance(d["Tube"], list):
            for tube in d["Tube"]:
                gmw.Tube.append(GMWTube(**tube))
        else:
            gmw.Tube.append(GMWTube(**d["Tube"]))
        if isinstance(d["History"], list):
            for history in d["History"]:
                gmw.History.append(GMWHistory(**history))
        else:
            gmw.History.append(GMWHistory(**d["History"]))
        return gmw


class GLD(MatlabBaseModel):
    Adm: list[GLDAdm]
    Dossier: list[GLDDossier]
    History: list[GLDHistory]
    Source: list[GLDSource]

    @classmethod
    def from_dict(cls, d: dict):
        gld = cls(
            **{
                "Adm": [],  # GLDAdm(**d["Adm"]),
                "Source": [],  # GLDSource(**d["Source"]),
                "Dossier": [],
                "History": [],
            }
        )
        if isinstance(d["Adm"], list):
            for adm in d["Adm"]:
                gld.Adm.append(GLDAdm(**adm))
        else:
            gld.Adm.append(GLDAdm(**d["Adm"]))

        if isinstance(d["Dossier"], list):
            for dossier in d["Dossier"]:
                gld.Dossier.append(GLDDossier(**dossier))
        else:
            gld.Dossier.append(GLDDossier(**d["Dossier"]))
        if isinstance(d["History"], list):
            for history in d["History"]:
                gld.History.append(GLDHistory(**history))
        else:
            gld.History.append(GLDHistory(**d["History"]))
        if not isinstance(d["Source"], list):
            d["Source"] = [d["Source"]]
        if isinstance(d["Source"], list):
            for source in d["Source"]:
                if isinstance(source["Measurements"], list):
                    measurements = [GLDMeasurement(**m) for m in source["Measurements"]]
                else:
                    measurements = [GLDMeasurement(**source["Measurements"])]
                if isinstance(source["Changes"], list):
                    changes = [COMChange.from_dict(c) for c in source["Changes"]]
                elif not isinstance(source["Changes"], str):
                    changes = [COMChange.from_dict(source["Changes"])]
                else:
                    changes = []
                source["Measurements"] = []
                source["Changes"] = []

                gld.Source.append(GLDSource(**source))
                for m in measurements:
                    gld.Source[-1].Measurements.append(m)
                for c in changes:
                    gld.Source[-1].Changes.append(c)
        else:
            gld.Source.append(GLDSource(**d["Source"]))

        return gld


class GMN(MatlabBaseModel):
    Adm: GMNAdm
    History: list[GMNHistory] | None
    Net: GMNNet
    Point: dict[int, GMNPoint] | None

    @classmethod
    def from_dict(cls, d: dict):
        gmn = cls(**{"Adm": GMNAdm(**d["Adm"]), "Net": [], "History": None, "Point": []})
        return gmn


class BRON(MatlabBaseModel):
    GMW: list[GMW]
    GMN: list[GMN]
    GLD: list[GLD]
