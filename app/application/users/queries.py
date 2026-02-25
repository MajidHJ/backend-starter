class GetUserQuery:
    def __init__(self, *, user_id: int) -> None:
        self.user_id = user_id


class ListUsersQuery:
    def __init__(self, *, page: int, size: int) -> None:
        self.page = page
        self.size = size