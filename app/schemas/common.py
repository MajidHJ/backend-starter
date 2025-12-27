from pydantic import BaseModel

class HealthResponse(BaseModel):
    status: str

class ExampleRequest(BaseModel):
    name: str

class ExampleResponse(BaseModel):
    id: int
    name: str

