from pydantic import BaseModel


class AudioPost(BaseModel):
    class Config:
        orm_mode = True

    audio: bytes


class Audio(BaseModel):
    class Config:
        orm_mode = True

    uuid: int
    audio: bytes
