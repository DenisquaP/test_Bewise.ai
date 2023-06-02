import io
import aiofiles
# import wave
from pydub import AudioSegment
from fastapi.responses import FileResponse, StreamingResponse
# from fastapi.responses import ChunkedFile
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4

from tables import Audio, Users
from database import get_session
from functions.delete import delete_file
# from functions.get_data import get_data_from_file

record_router = APIRouter()


@record_router.post(
    '/record/',
    status_code=201,
    tags=["Record"]
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
        await delete_file(f'records/{f_name}.wav')
        await delete_file(f'records/{f_name}.mp3')
        raise HTTPException(status_code=400, detail="This user are already have this record")  # noqa 501

    new_audio = Audio(
        user_id=user_id,
        uuid=str(uuid4()),
        record=record
    )
    await delete_file(f'records/{file.filename}')
    await delete_file(f'records/{f_name}.mp3')

    db.add(new_audio)
    await db.commit()
    return {'download link': f'http://localhost:8000/record/?user_id={new_audio.user_id}&record_id={new_audio.uuid}'}  # noqa 501


@record_router.get(
    '/record/',
    status_code=200,
    tags=["Record"]
)
async def get_record(user_id: int, record_id: str, db: AsyncSession = Depends(get_session)):  # noqa 501
    try:
        print('hi')
        result = await db.execute(select(Audio.record).filter(
            Audio.user_id == user_id,
            Audio.uuid == record_id)
            )
        bytes_data = b"".join(chunk.encode() for chunk in result)

        # async def generate():
        #     for chunk in result.chunks():
        #         yield chunk.encode('utf-8')
        # for chunk in file:
        #     yield chunk
        # print('hi')
        # file_path = '/records/record.mp3'
        # async with aiofiles.open(file_path, 'wb') as audio_file:
        #     async for chunk in file:
        #         print(chunk)
        #         await audio_file.write(chunk)
    except FileNotFoundError:
        raise HTTPException(detail="File not found", status_code=404)

    return StreamingResponse(io.BytesIO(bytes_data), media_type="audio/mpeg")
