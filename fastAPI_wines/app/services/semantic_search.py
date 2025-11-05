from typing import List
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/distiluse-base-multilingual-cased-v2")

async def search_wines_semantic(
    db: AsyncSession,
    query: str,
    top_k: int = 5
) -> List[dict]:
    """
    Búsqueda semántica de vinos usando embeddings y pgvector.
    """
    # Calcular embedding de la consulta
    query_embedding = model.encode(query)
    
    # Convertir a string para SQL
    vec_str = "[" + ",".join(map(str, query_embedding.tolist())) + "]"
    
    # Consulta con distancia coseno
    sql = text("""
        SELECT 
            uid, country, description, designation,
            points, price, province, region, variety,
            1 - (description_vector <=> :vec::vector) as similarity
        FROM winereviews
        ORDER BY description_vector <=> :vec::vector
        LIMIT :k
    """)
    
    result = await db.execute(
        sql, 
        {"vec": vec_str, "k": top_k}
    )
    
    return [dict(row) for row in result]