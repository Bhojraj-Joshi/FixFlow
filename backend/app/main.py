from fastapi import FastAPI

app = FastAPI(
    title="FixFlow API",
    description="Service and Maintenance Management System",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to FixFlow API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }