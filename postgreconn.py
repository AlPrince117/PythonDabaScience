# Load the postgres module
import psycopg2

# Create a connection object
con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

# Create a cursor via the connection
cur = con.cursor()

# Query via the cursor
cur.execute("select * from pubs2.authors")
rows = cur.fetchall()
for row in rows:
    print(row)

# Alternatively, set the 'search_path' to set the schema search path (prefix)
cur.execute("SET search_path TO pubs2")
cur.execute("select * from authors")
rows = cur.fetchall()
for row in rows:
    print(row)