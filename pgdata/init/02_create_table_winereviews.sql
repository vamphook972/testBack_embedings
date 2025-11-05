-- Create winereviews table used by the app
-- Ensure this runs after the pgvector extension (this file is named 02_ so it runs after 01_create_extension_vector.sql)
CREATE TABLE IF NOT EXISTS winereviews (
    uid SERIAL PRIMARY KEY,
    country VARCHAR(255),
    description VARCHAR(2000),
    designation VARCHAR(255),
    points INTEGER,
    price FLOAT,
    province VARCHAR(255),
    region VARCHAR(255),
    variety VARCHAR(255),
    description_vector vector
);
