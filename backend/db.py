import pymysql
from pymysql.cursors import DictCursor

# MySQL Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "perseus"
DB_NAME = "founder_ai"

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=DictCursor
    )
