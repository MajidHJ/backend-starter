from fastapi import APIRouter,status
from app.schemas.common import ExampleRequest,ExampleResponse

router = APIRouter(prefix="/v1",tags=["demo"])


@router.post(
        "/demo",
        status_code=status.HTTP_200_OK,
        response_model= ExampleResponse,
        responses={
            422:{"description":"unprocceable entity"}
        }
)
def demo(payload: ExampleRequest):
    return ExampleResponse(name=payload.name)
