from pydantic import BaseModel


class Record(BaseModel):
    link: str
