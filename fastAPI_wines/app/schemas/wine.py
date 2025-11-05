from pydantic import BaseModel, Field
from typing import Optional, List

class WineBase(BaseModel):
    country: Optional[str] = None
    description: str
    designation: Optional[str] = None
    points: Optional[int] = Field(None, ge=0, le=100)
    price: Optional[float] = Field(None, ge=0)
    province: Optional[str] = None
    region: Optional[str] = None
    variety: Optional[str] = None

class WineCreate(WineBase):
    pass

class Wine(WineBase):
    uid: int
    
    class Config:
        from_attributes = True

class WineSearchQuery(BaseModel):
    query: str
    top_k: int = Field(default=5, ge=1, le=100)

class WineSearchResult(Wine):
    similarity: float