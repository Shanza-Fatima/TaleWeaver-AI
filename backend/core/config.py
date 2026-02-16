from typing import List
from pydantic_settings import BaseSettings
#pydantic used for datavalidation and field_validator, data cleaner function
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX : str = "/api"

    DEBUG : bool = False

    ALLOWED_ORIGINS : str =""

    OPEN_API_KEY : str

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
#splits the raw string into a lIst otherwise returns empty list to prevent app from crashing.        
        return v.split(',') if v else [] 
    
#instruction manual for Setting class,
#tells pydantic how to find and read the the configuration
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()