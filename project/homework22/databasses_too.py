import config
import psycopg2

# OPERATIONS WITH DATABASE
with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS topics (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL UNIQUE,
                description TEXT
            )
        """
        cursor.execute(query)

        query2 = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(75) NOT NULL,
                email TEXT UNIQUE NOT NULL
            );

            CREATE TABLE IF NOT EXISTS posts (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) NOT NULL,
                topic_id INTEGER REFERENCES topics(id) NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        cursor.execute(query2)

# CREATE
with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        query_insert = """
INSERT INTO topics (name, description) VALUES
('Історія України', 'Обговорення подій, персоналій та етапів історії'),
('Фізика', 'Теми з механіки, електрики, оптики'),
('Програмування', 'Обговорення мов програмування, алгоритмів та проєктів');
"""
        cursor.execute(query_insert)