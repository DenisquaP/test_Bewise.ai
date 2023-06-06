from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = 'localhost'
    server_port: int = 8000

    database_url: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/postgres"  # noqa 501


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
