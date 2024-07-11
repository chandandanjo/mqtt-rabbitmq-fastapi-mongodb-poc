from pydantic import BaseModel

# model for validating time range query parameters
class TimeRange(BaseModel):
    start_time: str
    end_time: str