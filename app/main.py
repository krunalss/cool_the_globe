from fastapi import FastAPI
from app.routes import homepage
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files if necessary
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routes from the homepage module
app.include_router(homepage.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
