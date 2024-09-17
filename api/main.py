from fastapi import FastAPI
from mangum import Mangum
from api.routers.community import community_router
from api.routers.user import user_router
from api.routers.attendance import attendance_router
from api.routers.authentication import auth_router

app = FastAPI()
handler = Mangum(app)


@app.get("/")
def get_started():
    return {
        "message": "Hi this is the graphic era api "
    }


app.include_router(community_router, prefix="/community")
app.include_router(user_router, prefix="/user")
app.include_router(attendance_router, prefix="/attendance")
app.include_router(auth_router, prefix="/auth")
