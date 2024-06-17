from typing import Optional

from pydantic import BaseModel

from .BRONEnums import (
    ConstructionStandardEnum,
    DeliveryContextEnum,
    EventNameEnum,
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


class Adm(BaseModel):
    WellID: Optional[int]
    BROID: Optional[str]
    AccParty: Optional[str]
    DvRespParty: Optional[str]
    QualityRegime: Optional[str]
    ObjRgstrDateTime: Optional[str]
    LastRgstrEvent: Optional[int]
    WellCode: Optional[str]


class Tube(BaseModel):
    WellID: Optional[int]
    TubeNo: Optional[int]
    Type: Optional[TypeEnum]
    ArtesianWellCapPresent: Optional[str]
    TubeDiameter: Optional[float]
    IsVarTubeDiam: Optional[str]
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
    LoggerDepth: Optional[str]
    LoggerSerial: Optional[str]
    LoggerType: Optional[str]
    GldBROID: Optional[str]


class History(BaseModel):
    WellID: Optional[int]
    TubeNo: Optional[int]
    EventName: Optional[EventNameEnum]
    DateTime: Optional[str]
    Comment: Optional[str]
    CommentBy: Optional[str]
    EventData: Optional[str]


class Well(BaseModel):
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


class Geen(BaseModel):
    Geen: Optional[GeenEnum]
