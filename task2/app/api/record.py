import aiofiles
import wave
from pydub import AudioSegment
# from fastapi.responses import StreamingResponse
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4

from tables import Audio
from database import get_session

record_router = APIRouter()


@record_router.post(
    '/record/',
    status_code=201,
    tags=["Audio"]
)
async def add_song(file: UploadFile = File(), db: AsyncSession = Depends(get_session)):  # noqa 501
    audio = await file.read()
    with aiofiles.open(f'app/records/{file.filename}.wav', 'wb') as record:
        await record.write(audio)
    # new_audio = Audio(
    #     uuid=str(uuid4()),
    #     record=record
    # )
    # db.add(new_audio)
    # db.commit()
    return {'filename': file.filename}


# @record_router.get(
#     '/record/{user_id}/{file_uuid}/',
#     status_code=200
# )
# def get_record(user: str = user_id, db: Session = Depends(get_session)):
#     db_file = db.query(Audio).filter(Audio.id==file_uuid).first()
#     if not db_file:
#         raise HTTPException(status_code=404, detail="File not found")
#     return StreamingResponse(io.BytesIO(db_file.data), media_type=db_file.content_type, headers={"Content-Disposition": f"attachment; filename={db_file.filename}"})
