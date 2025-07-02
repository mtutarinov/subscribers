import os

from dotenv import load_dotenv

load_dotenv()

class Settings:

    APP_NAME: str = os.getenv("APP_NAME", "subscribers")

    DB_NAME: str = os.getenv("DB_NAME", "dev")
    DB_USER: str = os.getenv("DB_USER", "dev")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "dev")
    DB_HOST: str = os.getenv("DB_HOST", "db")
    DB_PORT: str = os.getenv("DB_PORT", "27017")
    DB_URL: str = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"


settings = Settings()


