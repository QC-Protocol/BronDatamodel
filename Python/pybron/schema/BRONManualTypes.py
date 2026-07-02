from Python.pybron.schema.matlabbasemodel import MatlabBaseModel


class GLDMeasurement(MatlabBaseModel):
    DateTime: float
    RawValue: float


class GLDChange(MatlabBaseModel):
    values: list[list[float]]
    person: str
    date: float
