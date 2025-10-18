import os
from dotenv import load_dotenv
#a
load_dotenv()

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_USER = os.environ.get("REDIS_USER")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

PGHOST = os.environ.get("PGHOST")
PGDATABASE = os.environ.get("PGDATABASE")
PGUSER = os.environ.get("PGUSER")
PGPASSWORD = os.environ.get("PGPASSWORD")
print(PGHOST)
