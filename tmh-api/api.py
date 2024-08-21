from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.users import router as users_router
from endpoints.hmo import router as hmo_router
from endpoints.centers import router as center_router
from endpoints.tests import router as test_router

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:8800",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(users_router, prefix="/api/users", tags=["users"])
app.include_router(hmo_router, prefix="/api/hmo", tags=["hmo"])
app.include_router(center_router, prefix="/api/center", tags=["centers"])
app.include_router(test_router, prefix="/api/test", tags=["tests"])

# You can add more routers here for other endpoints...
