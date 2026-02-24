from app.schemas.user import UserResponse
from app.schemas.common import Page
from .commands import CreateUserCommand
class UserService:

    def __init__(self,storage: list[UserResponse]):
        self._storage = storage
        self._next_id = max([user.id for user in storage],default= 0)+1

    def create_user(self, cmd: CreateUserCommand) ->UserResponse:

        new_user = UserResponse(
            id=self._next_id,
            name=cmd.name,
            email=cmd.email,
        )

        self._storage.append(new_user)
        self._next_id +=1
        return new_user
    
    
    def list_users(self,page:int,size:int) -> Page[UserResponse]:
        start = (page-1)*size
        end = start + size
        users = Page[UserResponse](
        items= self._storage[start:end],
        total=len(self._storage),
        )
        return users 
        

    def get_user_by_id(self,user_id) -> UserResponse | None:
        return next((u for u in self._storage if u.id == user_id),None)
        