import psycopg2
import csv

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
#
# # Create a cursor via the connection
# cur = con.cursor()
#
# with open('500-us-users.csv', 'r') as f:
#     reader=  csv.reader(f)
#     for row in reader:
#         print(row)
#
# con.commit()


# with open('500-us-users.csv', 'r') as f:
#     reader=  csv.DictReader(f)
#     for row in reader:
#         print(row['first_name'],row['last_name'])
#
# con.commit()

myData = ['Kwame', 'Mensah', 'P. O. Box 117', 'Accra', 'Accra', 'GA', 11234, 554892020, 554789678]
myfile = open('500-us-users.csv', 'w')
with myfile:
    writer = csv.writer(myfile)
    writer.writerow(myData)

