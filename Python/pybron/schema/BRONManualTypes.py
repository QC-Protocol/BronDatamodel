from pydantic import ValidationError
from pybron.schema.matlabbasemodel import MatlabBaseModel


class GLDMeasurement(MatlabBaseModel):
    DateTime: float
    RawValue: float


class GLDChange(MatlabBaseModel):
    values: list[tuple[float, float]]
    person: str
    date: float

    @staticmethod
    def from_dict(data: dict):
        if len(data['values']) > 0:
            if isinstance(data['values'][0], float):
                data['values'] = [data['values']]
        try:
            change = GLDChange(**data)
        except ValidationError:
            pass
        return change
