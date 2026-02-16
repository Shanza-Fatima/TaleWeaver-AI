from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
app = FastAPI(
    title = "Choose your own Adventure Game API",
    description = "API to generate cool stuff",
    docs_url = "/docs",
    redocs_url = "/redoc",
)
app.add_middleware(
    CORSMiddleware,
    #secuirity setup, making specific list urls to decide who can access the API
    allow_origins = settings.ALLOWED_ORIGINS,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host= "0.0.0.0", port = 8000, reload= True)