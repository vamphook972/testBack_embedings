from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base

class WineReview(Base):
    """Modelo para reseñas de vinos."""
    __tablename__ = "winereviews"

    uid = Column(Integer, primary_key=True)
    country = Column(String(255))
    description = Column(String(2000))
    designation = Column(String(255))
    points = Column(Integer)
    price = Column(Float)
    province = Column(String(255))
    region = Column(String(255))
    variety = Column(String(255))
    # description_vector se maneja nativamente en PostgreSQL con pgvector