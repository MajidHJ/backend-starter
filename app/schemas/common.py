from pydantic import BaseModel,Field

class HealthResponse(BaseModel):
    status: str

class ExampleRequest(BaseModel):
    name: str = Field(min_length=2)

class ExampleResponse(BaseModel):
    name: str

