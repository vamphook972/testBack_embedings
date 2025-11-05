from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.database import get_session
from app.schemas.wine import Wine, WineSearchQuery, WineSearchResult
from app.crud import wine as wine_crud
from app.services import semantic_search

router = APIRouter()

@router.get("/{uid}", response_model=Wine)
async def get_wine(
    uid: int,
    db: AsyncSession = Depends(get_session)
):
    wine = await wine_crud.get_wine(db, uid)
    if wine is None:
        raise HTTPException(status_code=404, detail="Wine not found")
    return wine

@router.get("/", response_model=List[Wine])
async def list_wines(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_session)
):
    return await wine_crud.get_wines(db, skip, limit)

@router.post("/search", response_model=List[WineSearchResult])
async def search_wines(
    query: WineSearchQuery,
    db: AsyncSession = Depends(get_session)
):
    """Búsqueda semántica de vinos basada en descripción."""
    results = await semantic_search.search_wines_semantic(
        db, 
        query.query, 
        query.top_k
    )
    return results