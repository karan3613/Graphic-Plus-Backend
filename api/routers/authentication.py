from fastapi import APIRouter, HTTPException
from api.Config.config import login_collection, forgotId_collection, forgotPassword_collection

auth_router = APIRouter()


@auth_router.get("/login/{univ_id}/{password}")
async def verify_login(univ_id: str, password: str):
    try:
        user = login_collection.find_one({"univ_id": univ_id, "password": password})

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if isinstance(user, dict) and len(user) == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {"result": "verified"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@auth_router.get("/forgotPassword/{univ_id}/{email}/{dob}")
async def verify_forgot_password(univ_id : str, email : str):

    query = {
        "univ_id": univ_id,
        "email": email,
    }
    try:
        user = forgotPassword_collection.find_one(query)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if isinstance(user, dict) and len(user) == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {"result": "verified"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@auth_router.get("/forgotId/{mobileNo}")
async def verify_forgot_id(mobileNo: str):
    query = {"mobileNo": mobileNo}
    try:
        user = forgotId_collection.find_one(query)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if isinstance(user, dict) and len(user) == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"result": user['univ_id']}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
