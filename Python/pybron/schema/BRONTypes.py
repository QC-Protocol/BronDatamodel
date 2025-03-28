# flake8: noqa
from typing import Any, Optional

from pybron.schema.matlabbasemodel import MatlabBaseModel

from .BRONEnums import (
    GARAnalyticalTechniqueEnum,
    GARColourEnum,
    GARColourStrengthEnum,
    GARCorrectionReasonEnum,
    GARLimitSymbolEnum,
    GARPumpTypeEnum,
    GARQualityControlMethodEnum,
    GARQualityControlStatusEnum,
    GARSamplingStandardEnum,
    GARValuationMethodEnum,
    GLDAirPressureCompensationTypeEnum,
    GLDCensoredReasonEnum,
    GLDCorrectionReasonEnum,
    GLDEvaluationProcedureEnum,
    GLDInterpolationTypeEnum,
    GLDMeasurementInstrumentTypeEnum,
    GLDObservationTypeEnum,
    GLDProcessReferenceEnum,
    GLDProcessTypeEnum,
    GLDStatusCodeEnum,
    GLDStatusQualityControlEnum,
    GMNCorrectionReasonEnum,
    GMNDeliveryContextEnum,
    GMNEventNameEnum,
    GMNGroundwaterAspectEnum,
    GMNMonitoringPurposeEnum,
    GMWConstructionStandardEnum,
    GMWCoordTransformationEnum,
    GMWCorrectionReasonEnum,
    GMWDeliveryContextEnum,
    GMWElectrodePackingMaterialEnum,
    GMWElectrodeStatusEnum,
    GMWEventNameEnum,
    GMWGlueEnum,
    GMWGroundLevelPositioningMethodEnum,
    GMWHorizontalCrsEnum,
    GMWHorizontalPositioningMethodEnum,
    GMWInitialFunctionEnum,
    GMWLocalVerticalReferencePointEnum,
    GMWSockMaterialEnum,
    GMWTubeMaterialEnum,
    GMWTubePackingMaterialEnum,
    GMWTubeStatusEnum,
    GMWTubeTopPositioningMethodEnum,
    GMWTubeTypeEnum,
    GMWVerticalDatumEnum,
    GMWWellHeadProtectorEnum,
    GMWWellStabilityEnum,
)


class GMWAdm(MatlabBaseModel):
    GMWID: Optional[int]
    BROID: Optional[str]
    AccParty: Optional[str]
    DvRespParty: Optional[str]
    QualityRegime: Optional[int]
    ObjRgstrDateTime: Optional[float]
    LastRgstrEvent: Optional[int]


class GMWTube(MatlabBaseModel):
    GMWID: Optional[int]
    TubeNo: Optional[int]
    Type: Optional[GMWTubeTypeEnum]
    ArtesianWellCapPresent: Optional[float]
    TubeDiameter: Optional[float]
    IsVarTubeDiam: Optional[float]
    Status: Optional[GMWTubeStatusEnum]
    TopLevel: Optional[float]
    VertPosMethodTop: Optional[GMWTubeTopPositioningMethodEnum]
    PackingMaterial: Optional[GMWTubePackingMaterialEnum]
    Glue: Optional[GMWGlueEnum]
    Material: Optional[GMWTubeMaterialEnum]
    SockMaterial: Optional[GMWSockMaterialEnum]
    FilterTopLevel: Optional[float]
    FilterBottomLevel: Optional[float]
    sedSumpLength: Optional[float]
    LoggerBrand: Optional[str]
    LoggerDepth: Optional[float]
    LoggerSerial: Optional[str]
    LoggerType: Optional[str]
    GLDID: Optional[int]


class GMWHistory(MatlabBaseModel):
    GMWID: Optional[int]
    TubeNo: Optional[int]
    EventName: Optional[Any]
    DateTime: Optional[float]
    Comment: Optional[str]
    CommentBy: Optional[str]
    EventData: Optional[Any]


class GMWWell(MatlabBaseModel):
    Name: Optional[str]
    WellCode: Optional[str]
    NITGCode: Optional[str]
    Owner: Optional[str]
    Maintainer: Optional[str]
    DeliveryContext: Optional[GMWDeliveryContextEnum]
    ConstructionStandard: Optional[GMWConstructionStandardEnum]
    InitialFunction: Optional[GMWInitialFunctionEnum]
    WellStability: Optional[GMWWellStabilityEnum]
    HeadProtector: Optional[GMWWellHeadProtectorEnum]
    HorPosMethod: Optional[GMWHorizontalPositioningMethodEnum]
    SurfaceLevel: Optional[float]
    VertPosMethodSurf: Optional[GMWGroundLevelPositioningMethodEnum]
    XCoordinate: Optional[float]
    YCoordinate: Optional[float]
    VegType: Optional[str]
    VegTypo: Optional[str]
    OLGACode: Optional[str]


class GLDAdm(MatlabBaseModel):
    GLDID: Optional[int]
    BROID: Optional[str]
    AccParty: Optional[str]
    DvRespParty: Optional[str]
    QualityRegime: Optional[str]
    ObjRgstrDateTime: Optional[float]
    LastRgstrEvent: Optional[int]


class GLDDossier(MatlabBaseModel):
    GMWID : Optional[int]
    GMWBROID: Optional[str]
    TubeNo: Optional[int]


class GLDSource(MatlabBaseModel):
    GLDID: Optional[int]
    ObservationID: Optional[str]
    IsInterim: Optional[float]
    Investigator: Optional[str]
    ProcessID: Optional[int]
    LoggerSerial: Optional[str]
    LoggerDepth: Optional[float]
    # LoggerBrand: Optional[str]
    File: Optional[str]
    RefLevel: Optional[Any]
    WaterDensity: Optional[float] = 1
    Gravity: Optional[float] = 9.81
    Battery: Optional[str] = ""
    BaroID: Optional[int]
    Measurements: Optional[Any]
    Changes: Optional[Any]
    Drift: Optional[float]
    TimeShift: Optional[int]
    iChange: Optional[int]


class GLDHistory(MatlabBaseModel):
    GLDID: Optional[int]
    EventName: Optional[Any]
    EventDate: Optional[float]
    SourceID: Optional[int]
    EventData: Optional[Any]


class GMNAdm(MatlabBaseModel):
    GMNID: Optional[int]
    BROID: Optional[str]
    AccParty: Optional[str]
    DvRespParty: Optional[str]
    QualityRegime: Optional[str]
    ObjRgstrDateTime: Optional[float]
    LastRgstrEvent: Optional[int]


class GMNPoint(MatlabBaseModel):
    GMNID: Optional[int]
    MeasuringPointCode: Optional[str]
    GMWBROID: Optional[str]
    TubeNo: Optional[int]


class GMNHistory(MatlabBaseModel):
    GMNID: Optional[int]
    EventName: Optional[Any]
    EventDate: Optional[float]
    PointID: Optional[int]
    EventData: Optional[Any]


class GMNNet(MatlabBaseModel):
    Name: Optional[str]
    DeliveryContext: Optional[GMNDeliveryContextEnum]
    MonitoringPurpose: Optional[GMNMonitoringPurposeEnum]
    GroundwaterAspect: Optional[GMNGroundwaterAspectEnum]
    startDateMonitoring: Optional[float]
    endDateMonitoring: Optional[float]
