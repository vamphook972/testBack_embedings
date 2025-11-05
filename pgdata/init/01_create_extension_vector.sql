-- Create pgvector extension at DB init
-- This will run during the first container startup (mounted into /docker-entrypoint-initdb.d/)
CREATE EXTENSION IF NOT EXISTS vector;
