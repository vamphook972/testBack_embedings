CREATE TABLE winereviews (
    uid INTEGER,
    country VARCHAR(255),
    description VARCHAR(2000),
    designation VARCHAR(255),
    points INTEGER,
    price DOUBLE PRECISION,
    province VARCHAR(255),
    region VARCHAR(255),
    variety VARCHAR(255),
    description_vector vector(512)
);