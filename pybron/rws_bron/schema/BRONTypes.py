from typing import Any, Optional

from rws_bron.schema.matlabbasemodel import MatlabBaseModel

from .BRONEnums import (
    ConstructionStandardEnum,
    DeliveryContextEnum,
    GeenEnum,
    GlueEnum,
    HeadProtectorEnum,
    HorPosMethodEnum,
    InitialFunctionEnum,
    MaterialEnum,
    PackingMaterialEnum,
    SockMaterialEnum,
    StatusEnum,
    TypeEnum,
    VertPosMethodSurfEnum,
    VertPosMethodTopEnum,
)


class Adm(MatlabBaseModel):
    WellID: Optional[int]
    BROID: Optional[str]
    AccParty: Optional[str]
    DvRespParty: Optional[str]
    QualityRegime: Optional[int]
    ObjRgstrDateTime: Optional[float]
    LastRgstrEvent: Optional[int]
    WellCode: Optional[str]


class Tube(MatlabBaseModel):
    WellID: Optional[int]
    TubeNo: Optional[int]
    Type: Optional[TypeEnum]
    ArtesianWellCapPresent: Optional[float]
    TubeDiameter: Optional[float]
    IsVarTubeDiam: Optional[float]
    Status: Optional[StatusEnum]
    TopLevel: Optional[float]
    VertPosMethodTop: Optional[VertPosMethodTopEnum]
    PackingMaterial: Optional[PackingMaterialEnum]
    Glue: Optional[GlueEnum]
    Material: Optional[MaterialEnum]
    SockMaterial: Optional[SockMaterialEnum]
    FilterTopLevel: Optional[float]
    FilterBottomLevel: Optional[float]
    sedSumpLength: Optional[float]
    LoggerBrand: Optional[str]
    LoggerDepth: Optional[float]
    LoggerSerial: Optional[str]
    LoggerType: Optional[str]
    GLDBROID: Optional[str]


class History(MatlabBaseModel):
    WellID: Optional[int]
    TubeNo: Optional[int]
    EventName: Optional[str]
    DateTime: Optional[float]
    Comment: Optional[str]
    CommentBy: Optional[str]
    EventData: Optional[Any]


class Well(MatlabBaseModel):
    Name: Optional[str]
    DeliveryContext: Optional[DeliveryContextEnum]
    ConstructionStandard: Optional[ConstructionStandardEnum]
    InitialFunction: Optional[InitialFunctionEnum]
    WellStability: Optional[str]
    NITGCode: Optional[str]
    Owner: Optional[str]
    Maintainer: Optional[str]
    HeadProtector: Optional[HeadProtectorEnum]
    HorPosMethod: Optional[HorPosMethodEnum]
    SurfaceLevel: Optional[float]
    VertPosMethodSurf: Optional[VertPosMethodSurfEnum]
    XCoordinate: Optional[float]
    YCoordinate: Optional[float]
    VegType: Optional[str]
    VegTypo: Optional[str]
    OLGACode: Optional[str]


class Geen(MatlabBaseModel):
    Geen: Optional[GeenEnum]
