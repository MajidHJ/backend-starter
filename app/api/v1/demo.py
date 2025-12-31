from fastapi import APIRouter,status
from fastapi.responses import JSONResponse
from app.schemas.common import ExampleRequest,ExampleResponse,ErrorResponse

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

FAKE_DB = {1:{"id":1, "name":"ali"}}

@router.get(
        path="/get_user",
        status_code=status.HTTP_200_OK,
        responses={
            404:{
                "model":ErrorResponse
            }
        },
        response_model=ExampleResponse,

)
def get_user(user_id: int):
    user = FAKE_DB.get(user_id)

    if not user:
        return JSONResponse(
            status_code= status.HTTP_404_NOT_FOUND,
            content= ErrorResponse(
                error= "USER_NOT_FOUND",
                message= f"user with id= {user_id} does not exist",
            ).model_dump()
        )
    return ExampleResponse(name=user.get("name"))