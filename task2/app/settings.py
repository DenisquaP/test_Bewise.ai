from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_HOST: str = 'localhost'
    SERVER_PORT: int = 8000

    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/postgres"  # noqa 501


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
