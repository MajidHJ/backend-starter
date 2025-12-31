from pydantic import BaseModel,Field

class HealthResponse(BaseModel):
    status: str


class ErrorResponse(BaseModel):
    error: str
    message: str

class ExampleRequest(BaseModel):
    name: str = Field(min_length=2)

class ExampleResponse(BaseModel):
    name: str

