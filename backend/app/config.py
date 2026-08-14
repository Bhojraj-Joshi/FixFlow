import os


class Settings:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "fixflow-secret-key-change-this"
    )

    ALGORITHM = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES = 60


settings = Settings()