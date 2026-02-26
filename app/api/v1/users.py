from fastapi import APIRouter,status,HTTPException,Response,Depends,Query
from app.schemas.user import CreateUserRequest,UserResponse,UpdateUserRequest
from app.schemas.common import ErrorResponse,Page
from app.application.users.commands import CreateUserCommand,UpdateUserCommand,DeleteUserCommand
from app.application.users.queries import GetUserQuery, ListUsersQuery
from app.application.users.service import UserService
from app.deps import get_user_service

router = APIRouter(prefix="/users",tags=["users"])



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
def update_user(user_id:int, data: UpdateUserRequest , service: UserService = Depends(get_user_service)):
    cmd = UpdateUserCommand(user_id = user_id,name=data.name)
    user = service.update_user(cmd)

    if user is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with id: {user_id} not found",
        )
    
    return user
     



@router.delete(
    path="/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses= {
        404 : {"model": ErrorResponse, "description": "User Not Found"}
    }
)

def delete_user(user_id : int , service: UserService = Depends(get_user_service)):
    cmd = DeleteUserCommand(user_id=user_id)
    ok = service.delete_user(cmd)
  
    if not ok:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with id: {user_id} not found",
        )
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)