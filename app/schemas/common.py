from pydantic import BaseModel,Field
from typing import Generic,TypeVar

T = TypeVar("T")

class Page(BaseModel, Generic[T]):
    items : list[T]
    total : int

class HealthResponse(BaseModel):
    status: str

class HealthDebugResponse(BaseModel):
    status: str
    timestamp: str

class ErrorResponse(BaseModel):
    error: str
    message: str

class ExampleRequest(BaseModel):
    name: str = Field(min_length=2)

class ExampleResponse(BaseModel):
    name: str

