import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_items(conn):
    """  cc  """
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")

    rows = cur.fetchall()

    for row in rows:
        print(row)

db_file = "c:\\Users\\admin\\Documents\\test.db"
conn = create_connection(db_file)
select_items(conn)