from fastapi import APIRouter, HTTPException
from api.Config.config import community_collection
from api.Serializers.serializers import list_communities_serializer

community_router = APIRouter()


@community_router.get("/clubs")
async def get_communities():
    communities = list_communities_serializer(community_collection.find())
    if communities is None:
        raise HTTPException(status_code=404, detail="User not found")
    if isinstance(communities, dict) and len(communities) == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return communities
