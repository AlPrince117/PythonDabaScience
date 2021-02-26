# Load the postgres module
import psycopg2

# Create a connection object
con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

# Create a cursor via the connection
cur = con.cursor()

# Query via the cursor
cur.execute("rollback")
# cur.execute("DROP SCHEMA ususers CASCADE")

cur.execute("CREATE SCHEMA IF NOT EXISTS ususers")
cur.execute("SET search_path TO ususers")


sql = """CREATE TABLE n users (
    first_name              varchar(20) not null,
    last_name               varchar(20) not null,           
    address                 varchar(50) not null,           
    city                    varchar(20) not null,
    county                 varchar(20) not null,
    state                   varchar(20) not null,
    zip                     integer not null,
    phone1                  varchar(20) not null,
    phone2                  varchar(20) not null
);"""

# cur.execute(sql)

cur.execute('ROLLBACK')
try:
    cur.execute(sql)
    con.commit()
except:
    print("Relation exist")

# cur.execute(sql)
# con.commit()


with open('500-us-users.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=',')

con.commit()