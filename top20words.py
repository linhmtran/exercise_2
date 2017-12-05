
import csv
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#connect to Database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host ="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT word, CAST(count AS integer) from tweetwordcount ORDER BY count desc LIMIT 20")
top20 = cur.fetchall()

with open("top20.csv", "wb") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(top20)

conn.close()

