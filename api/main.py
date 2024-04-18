from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.generator import router as generator_router
from routers.parser import router as parser_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(parser_router)
app.include_router(generator_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
