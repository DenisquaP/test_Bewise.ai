import os
from fastapi import HTTPException


async def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Try again later"
            )
