import aiohttp


async def get_questions(question_num: int = 1) -> list():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://jservice.io/api/random?count={question_num}') as resp:  # noqa 501
            json_resp = await resp.json()
            return json_resp
