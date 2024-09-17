from fastapi import APIRouter, HTTPException
from api.Config.config import attendance_collection
from api.Serializers.serializers import attendance_serializer

attendance_router = APIRouter()


@attendance_router.get("/{univ_id}")
async def get_attendance(univ_id: str):
    try:
        user = attendance_collection.find_one({"univ_id": univ_id})

        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        if isinstance(user, dict) and len(user) == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return attendance_serializer(user)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
