from app.schemas.user import UserResponse
from app.schemas.common import Page 
class UserService:

    def __init__(self,storage: list[UserResponse]):
        self._storage = storage
        self._next_id = max([user.id for user in storage],default= 0)+1

    def create_user(self, *,name:str,email:str):

        new_user = UserResponse(
            id=self._next_id,
            name=name,
            email=email,
        )

        self._storage.append(new_user)
        self._next_id +=1
        return new_user
    
    
    def get_users(self,page:int,size:int):
        start = (page-1)*size
        end = start + size
        users = Page[UserResponse](
        items= self._storage[start:end],
        total=len(self._storage),
        )
        return users 
        

    def get_user_by_id(self,id):
        return next((u for u in self._storage if u.id == id),None)
        