from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import uuid4

from schemas.user import User, UserPOST
from tables import Users
from database import get_session

user_router = APIRouter()


@user_router.post(
    '/user/',
    response_model=User,
    status_code=201,
    tags=['User']
)
async def create_user(body: UserPOST, db: AsyncSession = Depends(get_session)):
    username = body.dict().get('username')

    new_user = Users(
        uuid=str(uuid4()),
        username=username,
    )

    db.add(new_user)
    await db.commit()
    return {'id': new_user.id, 'uuid': new_user.uuid}


@user_router.get(
    '/user/',
    tags=['User'],
)
async def get_users(db: AsyncSession = Depends(get_session)):
    # users = await db.execute(text('SELECT * FROM users'))
    print('hi')
    result = await db.execute(select(Users))
    users = await result.fetchall()
    return users
