from typing import Generator
import aiofiles


async def get_data_from_file(file_path: str) -> Generator:
    async with aiofiles.open(file=file_path, mode="rb") as file_like:
        yield file_like.read()
