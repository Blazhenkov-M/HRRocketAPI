from pydantic_settings import BaseSettings
from environs import Env

env = Env()
env.read_env()


class Settings(BaseSettings):
    app_title: str = "Моя библиотека"

    # uvicorn
    host: str = env.str('HOST')
    port: int = env.int('PORT')

    # db
    db_url: str = env.str('DATABASE_URL')


conf = Settings()
