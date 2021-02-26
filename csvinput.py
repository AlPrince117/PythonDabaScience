import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

# Create a cursor via the connection
cur = con.cursor()

with open('500-us-users.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=',')

con.commit()