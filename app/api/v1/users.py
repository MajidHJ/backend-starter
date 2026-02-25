from fastapi import APIRouter,status,HTTPException,Response,Depends,Query
from app.schemas.user import CreateUserRequest,UserResponse,UpdateUserRequest
from app.schemas.common import ErrorResponse,Page
from app.application.users.service import UserService
from app.application.users.commands import CreateUserCommand
from app.application.users.queries import GetUserQuery, ListUsersQuery

router = APIRouter(prefix="/users",tags=["users"])


fake_users : list[UserResponse]= []


def get_user_service():
    return UserService(fake_users)



@router.post(
    path="",
    status_code= status.HTTP_201_CREATED,
    response_model= UserResponse,
)
def create_user(user: CreateUserRequest, service: UserService = Depends(get_user_service)):
    cmd = CreateUserCommand(**user.model_dump())
    return service.create_user(cmd)


@router.get(
    path= "/{user_id}",
    status_code= status.HTTP_200_OK,
    response_model=UserResponse,
)

def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    query = GetUserQuery(user_id= user_id)
    user = service.get_user(query= query)
    if user is None :
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with id: {user_id} not found",
        )
    
    return user


@router.get(
    path="",
    status_code=status.HTTP_200_OK,
    response_model= Page[UserResponse]
)
def list_users(
    page: int = Query(1,ge=1),
    size: int = Query(10,ge=1,le=50),
    service:UserService =  Depends(get_user_service)
) -> Page[UserResponse]:
    query = ListUsersQuery(page=page,size=size)
    return service.list_users(query=query)




@router.put(
    path= "/{user_id}",
    status_code= status.HTTP_200_OK,
    response_model= UserResponse,
    responses= {
        404 : {
            "model": ErrorResponse,
            "description": "User Not Found"
            }
    }
)
def update_user(user_id:int, data: UpdateUserRequest):

    # TODO(day45): Move update use-case to application layer.
    # Route must not mutate fake_users_ directly; it should call UserService.update_user(...)
    # [EDUCATIONAL TRADE-OFF] Direct in-route mutation is temporary until service/repository is in place.

    user = next((u for u in fake_users if u.id == user_id),None)
    if user is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with id: {user_id} not found",
        )

    user.name = data.name
    return user



@router.delete(
    path="/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses= {
        404 : {"model": ErrorResponse, "description": "User Not Found"}
    }
)

def delete_user(user_id : int):
    # TODO(day45): Move delete use-case to application layer.
    # Route must not remove from fake_users_ directly; it should call UserService.delete_user(...)
    # [EDUCATIONAL TRADE-OFF] Direct in-route mutation is temporary until service/repository is in place.
    
    idx = next((i for i,u in enumerate(fake_users) if u.id == user_id),None)
    if idx is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with id: {user_id} not found",
        )
    fake_users.pop(idx)
    return Response(status_code=status.HTTP_204_NO_CONTENT)