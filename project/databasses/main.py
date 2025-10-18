import config
import psycopg2

with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE IF NOT EXISTS brand (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL UNIQUE
            )
        """
        cursor.execute(query)

        query2 = """
            CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name VARCHAR(75) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS car (
                id SERIAL PRIMARY KEY,
                model VARCHAR(75) NOT NULL,
                cost INTEGER,
                brand_id INTEGER REFERENCES brand(id),
                customer_id INTEGER REFERENCES customer(id)
            );
        """
        cursor.execute(query2)

#a
#CREATE

with psycopg2.connect(
        dbname=config.PGDATABASE,
        user=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        port=5432,
) as connection:
    with connection.cursor() as cursor:
        query_insert = 'INSERT INTO brand (name) VALUES (%s)'
        cursor.execute(query_insert, ("BMW", ))