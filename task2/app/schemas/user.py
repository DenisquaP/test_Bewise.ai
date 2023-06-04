from pydantic import BaseModel


class UserPOST(BaseModel):
    username: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    uuid: str

    class Config:
        orm_mode = True


class UsersList(User):
    username: str

    class Config:
        orm_mode = True
