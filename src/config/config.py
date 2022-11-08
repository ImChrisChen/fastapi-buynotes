from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USERNAME: str = 'root'
    DB_PASSWORD: str = 'rootadmin'
    DB_PORT: int = 3306
    DB_DATABASE: str = 'buy_notes'
    DB_HOST: str = 'chrisorz.tpddns.cn'

    API_V1_STR: str = '/api/v1'
    pass


settings = Settings()
