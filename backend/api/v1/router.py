from fastapi import APIRouter

# Create the router instance
router = APIRouter()

@router.get("/")
async def health_check():
    return {"status": "Good "}

# Add your routes here
@router.get("/health")
async def health_check():
    return {"status": "healthy"}

# Add more routes as needed