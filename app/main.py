from fastapi import FastAPI
from app.routes import homepage
from app.routes import contact,insights,greengauge
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files if necessary
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routes from the homepage module
app.include_router(homepage.router)
app.include_router(contact.router)
app.include_router(insights.router)  # Include the insights router
app.include_router(greengauge.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
    