from app.db import get_db_connection
from app import create_app

app = create_app()
with app.app_context():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, username, email FROM user")
        users = cur.fetchall()
        for u in users:
            print(u)
