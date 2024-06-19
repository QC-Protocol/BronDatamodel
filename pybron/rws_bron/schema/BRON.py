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

from rws_bron.schema.BRONTypes import Adm, History, Tube, Well
from rws_bron.schema.matlabbasemodel import MatlabBaseModel


class GMW(MatlabBaseModel):
    well: Well
    tube: list[Tube]
    history: list[History]
    adm: list[Adm]

    @classmethod
    def from_dict(cls, d: dict):
        gmw = cls(**{"well": Well(**d["Well"]), "tube": [], "history": [], "adm": []})
        if isinstance(d["Tube"], list):
            for tube in d["Tube"]:
                gmw.tube.append(Tube(**tube))
        else:
            gmw.tube.append(Tube(**d["Tube"]))
        if isinstance(d["History"], list):
            for history in d["History"]:
                gmw.history.append(History(**history))
        else:
            gmw.history.append(History(**d["History"]))
        if isinstance(d["Adm"], list):
            for adm in d["Adm"]:
                gmw.adm.append(Adm(**adm))
        else:
            gmw.adm.append(Adm(**d["Adm"]))
        return gmw
