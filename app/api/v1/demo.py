from fastapi import APIRouter,status,Query
from fastapi.responses import JSONResponse
from app.schemas.common import ExampleRequest,ExampleResponse,ErrorResponse,Page

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
        path="/get_user/{user_id}",
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



DEMO_USERS = [
    
        {"id": 1, "name": "ali"},
        {"id": 2, "name": "kia"},
        {"id": 3, "name": "reza"},
        {"id": 4, "name": "sara"},
        {"id": 5, "name": "nima"},
        {"id": 6, "name": "hoda"},

    
]


@router.get(
    "/get_users",
    responses={
        404 : {"model": ErrorResponse}
    },
    status_code= status.HTTP_200_OK,
    response_model= Page[ExampleResponse]
)

def get_users(page: int = Query(1,ge=1), size: int = Query(2,ge=1,le=4)):

    start = (page-1)*size
    end = start + size
    total = len(DEMO_USERS)
    if start >= total :
        return Page[ExampleResponse](items=[],total=total)
    
    items = [ExampleResponse(name=u["name"]) for u in DEMO_USERS[start:end]]
    return Page[ExampleResponse](items=items,total=len(DEMO_USERS))