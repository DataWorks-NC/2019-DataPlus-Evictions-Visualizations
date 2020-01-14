import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASS')
PGHOST = os.getenv('PGHOST')
PGDATABASE = os.getenv('PGDATABASE')
