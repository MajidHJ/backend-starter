from app.schemas.user import UserResponse
from app.schemas.common import Page
from .commands import CreateUserCommand
from .queries import GetUserQuery,ListUsersQuery
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
    
    
    def list_users(self,query: ListUsersQuery ) -> Page[UserResponse]:
        start = (query.page-1)*query.size
        end = start + query.size
        users = Page[UserResponse](
        items= self._storage[start:end],
        total=len(self._storage),
        )
        return users 
        

    def get_user(self, query: GetUserQuery) -> UserResponse | None:
        return next((u for u in self._storage if u.id == query.user_id),None)
        