import os


class Settings:
    PROJECT_NAME: str = "Polish Reverse Notation Calculator"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str = os.getenv("DB_USER")
    POSTGRES_PASSWORD = os.getenv("DB_PASS")
    POSTGRES_SERVER: str = os.getenv("DB_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("DB_PORT", 5432)
    POSTGRES_DB: str = os.getenv("DB_NAME", "tdd")
    DATABASE_URL = (
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
        f"{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )


settings = Settings()
