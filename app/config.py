from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_HOST:str = ""
    POSTGRES_PORT:int = 0
    POSTGRES_USER:str = ""
    POSTGRES_PASSWORD:str = ""
    POSTGRES_DB:str = ""
    
    @property
    def DATABASE_URL(self):
        return (f'postgresql+asyncpg://{self.POSTGRES_USER}:'
                f'{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:'
                f'{self.POSTGRES_PORT}/{self.POSTGRES_DB}')
    
    class Config:
        env_file = ".env"
        
settings = Settings()
