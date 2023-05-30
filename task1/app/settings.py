from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = 'localhost'
    server_port: int = 8000

    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"  # noqa 501


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
