# Author: chthon@seas.upenn.edu

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.generator import router as generator_router
from routers.parser import router as parser_router

# Create a new FastAPI app
app = FastAPI()

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include the routers in the app
app.include_router(parser_router)
app.include_router(generator_router)

if __name__ == "__main__":
    import uvicorn

    # Run the app using Uvicorn on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
