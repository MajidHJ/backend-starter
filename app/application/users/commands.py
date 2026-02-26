
class CreateUserCommand:
    def __init__(self, *, name: str,email: str) -> None:
        self.name = name
        self.email = email



class DeleteUserCommand:
    def __init__(self,*,user_id: int) -> None:
        self.user_id = user_id


class UpdateUserCommand:
    def __init__(self, *, user_id: int, name: str) -> None:
        self.user_id = user_id
        self.name = name