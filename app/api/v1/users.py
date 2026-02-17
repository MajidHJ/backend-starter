from fastapi import APIRouter,status,HTTPException,Query
from fastapi.responses import JSONResponse
from app.schemas.user import UserCreate,UserResponse
from app.schemas.common import ErrorResponse,Page


router = APIRouter(prefix="/users",tags=["users"])

fake_users_ : list[UserResponse]= []
id_ = 1



@router.post(
    path="",
    status_code= status.HTTP_201_CREATED,
    response_model= UserResponse,
)
def create_user(user: UserCreate):
    global id_
    new_user = UserResponse(
        id=id_,
        name=user.name,
        email=user.email,
    )

    fake_users_.append(new_user)
    id_ +=1
    return new_user


@router.get(
    path= "/{id}",
    status_code= status.HTTP_200_OK,
    response_model=UserResponse,
    responses= {
        404: {
            "model":ErrorResponse,
            "description":"User Not Found"
        }
    }

)

def get_user(id: int):
    user = next((u for u in fake_users_ if u.id == id),None)
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
def get_users(page: int = Query(1,ge=1),size: int = Query(1,ge=1,le=50) ):
    start = (page-1)*size
    end = start + size
    users = Page[UserResponse](
        items= fake_users_[start:end],
        total=len(fake_users_),
    ) 

    return users

    