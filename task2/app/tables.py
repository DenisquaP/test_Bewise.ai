from sqlalchemy import (
    Column,
    String,
    Integer,
    LargeBinary,
    ForeignKey,
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)
    records = relationship('Audio', back_populates="user")

    def __str__(self):
        return self.username


class Audio(Base):
    __tablename__ = 'records'

    user_id = Column(Integer, ForeignKey('users.id'))
    uuid = Column(String, nullable=False, primary_key=True)
    record = Column(LargeBinary, nullable=False)

    user = relationship('Users', back_populates="records")
