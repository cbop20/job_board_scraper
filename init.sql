DROP TABLE IF EXISTS opportunities;
CREATE TABLE IF NOT EXISTS opportunities (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255),
    title VARCHAR(255),
    link TEXT,
    info TEXT[]
    );