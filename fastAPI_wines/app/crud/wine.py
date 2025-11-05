from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List, Optional

from app.models.wine import WineReview
from app.schemas.wine import WineCreate

async def create_wine(db: AsyncSession, wine: WineCreate) -> WineReview:
    db_wine = WineReview(**wine.model_dump())
    db.add(db_wine)
    await db.commit()
    await db.refresh(db_wine)
    return db_wine

async def get_wine(db: AsyncSession, uid: int) -> Optional[WineReview]:
    result = await db.execute(select(WineReview).filter(WineReview.uid == uid))
    return result.scalar_one_or_none()

async def get_wines(
    db: AsyncSession, 
    skip: int = 0, 
    limit: int = 100
) -> List[WineReview]:
    result = await db.execute(select(WineReview).offset(skip).limit(limit))
    return result.scalars().all()

async def search_wines_by_country(
    db: AsyncSession, 
    country: str
) -> List[WineReview]:
    result = await db.execute(
        select(WineReview)
        .filter(WineReview.country.ilike(f"%{country}%"))
    )
    return result.scalars().all()

async def search_by_variety(
    db: AsyncSession,
    variety: str,
    limit: int = 10
) -> List[WineReview]:
    result = await db.execute(
        select(WineReview)
        .filter(WineReview.variety.ilike(f"%{variety}%"))
        .limit(limit)
    )
    return result.scalars().all()