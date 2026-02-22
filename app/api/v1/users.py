from fastapi import APIRouter,status,HTTPException,Response,Depends,Query
from app.schemas.user import UserCreate,UserResponse,UserUpdate
from app.schemas.common import ErrorResponse,Page
from app.application.users.service import UserService

router = APIRouter(prefix="/users",tags=["users"])


fake_users_ : list[UserResponse]= []


def get_user_service():
    return UserService(fake_users_)



@router.post(
    path="",
    status_code= status.HTTP_201_CREATED,
    response_model= UserResponse,
)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(name=user.name,email= user.email)


@router.get(
    path= "/{id}",
    status_code= status.HTTP_200_OK,
    response_model=UserResponse,
)

def get_user_by_id(id: int, service: UserService = Depends(get_user_service)):
    user = service.get_user_by_id(id)
    if user is None :
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with id: {id} not found",
        )
    
    return user


@router.get(
    path="",
    status_code=status.HTTP_200_OK,
    response_model= Page[UserResponse]
)
def get_users(
    page: int = Query(1,ge=1),
    size: int = Query(10,ge=1,le=50),
    service:UserService =  Depends(get_user_service)
):
    return service.get_users(page,size)




@router.put(
    path= "/{id}",
    status_code= status.HTTP_200_OK,
    response_model= UserResponse,
    responses= {
        404 : {
            "model": ErrorResponse,
            "description": "User Not Found"
            }
    }
)
def update_user(id:int, data: UserUpdate):

    # TODO(day45): Move update use-case to application layer.
    # Route must not mutate fake_users_ directly; it should call UserService.update_user(...)
    # [EDUCATIONAL TRADE-OFF] Direct in-route mutation is temporary until service/repository is in place.

    user = next((u for u in fake_users_ if u.id == id),None)
    if user is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with id: {id} not found",
        )

    user.name = data.name
    return user



@router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses= {
        404 : {"model": ErrorResponse, "description": "User Not Found"}
    }
)

def delete_user(id: int):
    # TODO(day45): Move delete use-case to application layer.
    # Route must not remove from fake_users_ directly; it should call UserService.delete_user(...)
    # [EDUCATIONAL TRADE-OFF] Direct in-route mutation is temporary until service/repository is in place.
    
    idx = next((i for i,u in enumerate(fake_users_) if u.id == id),None)
    if idx is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= f"user with id: {id} not found",
        )
    fake_users_.pop(idx)
    return Response(status_code=status.HTTP_204_NO_CONTENT)