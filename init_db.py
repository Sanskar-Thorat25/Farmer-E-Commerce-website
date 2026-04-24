import pymysql
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Swayam')
MYSQL_DB = 'krishi_hub_db'

print(f"Connecting to MySQL at {MYSQL_HOST} with user {MYSQL_USER}...")

connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    autocommit=True
)

with connection.cursor() as cursor:
    print(f"Creating database {MYSQL_DB} if it doesn't exist...")
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB}")

connection.select_db(MYSQL_DB)

with open('database.sql', 'r') as f:
    sql_script = f.read()

# Filter out lines that start with -- (comments) so we don't accidentally split inside strings that contain semicolons
lines = sql_script.split('\n')
clean_lines = [line for line in lines if not line.strip().startswith('--')]
clean_script = '\n'.join(clean_lines)

statements = clean_script.split(';')

with connection.cursor() as cursor:
    for statement in statements:
        if statement.strip():
            cursor.execute(statement)
            
connection.close()
print("Database initialized successfully from database.sql!")
