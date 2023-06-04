import aiofiles
from pydub import AudioSegment
from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4

from schemas.audio import Record
from tables import Audio, Users
from database import get_session
from functions.delete import delete_file

record_router = APIRouter()


@record_router.post(
    '/record/',
    status_code=201,
    tags=["Record"],
    response_model=Record
)
async def add_song(user_id: int, file: UploadFile = File(), db: AsyncSession = Depends(get_session)):  # noqa 501
    user = await db.execute(select(Users).filter(Users.id == user_id))
    if not user.scalar():
        raise HTTPException(status_code=404, detail="User not found")

    audio = await file.read()
    f_name = file.filename.rstrip('.wav')
    async with aiofiles.open(f'records/{file.filename}', 'wb') as record:  # noqa 501
        await record.write(audio)
        await record.flush()
    AudioSegment.from_wav(f'records/{file.filename}').export(f'records/{f_name}.mp3', format="mp3")  # noqa 501
    async with aiofiles.open(f'records/{f_name}.mp3', 'rb') as record_mp3:  # noqa 501
        record = await record_mp3.read()

    alredy_in_db = await db.execute(select(Audio).filter(
        Audio.record == record,
        Audio.user_id == user_id)
        )
    if alredy_in_db.scalar():
        delete_file(f'records/{f_name}.wav')
        delete_file(f'records/{f_name}.mp3')
        raise HTTPException(status_code=400, detail="This user are already have this record")  # noqa 501

    new_audio = Audio(
        user_id=user_id,
        uuid=str(uuid4()),
        record=record
    )
    delete_file(f'records/{file.filename}')
    delete_file(f'records/{f_name}.mp3')

    db.add(new_audio)
    await db.commit()
    return {'link': f'http://localhost:8000/record/?user_id={new_audio.user_id}&record_id={new_audio.uuid}'}  # noqa 501


@record_router.get(
    '/record/',
    status_code=200,
    tags=["Record"],
    response_class=FileResponse
)
async def get_record(user_id: int, record_id: str, db: AsyncSession = Depends(get_session)):  # noqa 501
    try:
        result = await db.execute(select(Audio.record).filter(
            Audio.user_id == user_id,
            Audio.uuid == record_id)
            )

        async with aiofiles.open(f'records/temp_out.mp3', 'wb') as record:  # noqa 501
            await record.write(result.scalars().first())
            await record.flush()

    except FileNotFoundError:
        raise HTTPException(detail="File not found", status_code=404)

    return FileResponse(
        path='records/temp_out.mp3',
        filename='record.mp3',
        media_type='audio/mp3')
