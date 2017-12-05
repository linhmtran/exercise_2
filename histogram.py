# set up the database and table
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#connect to Database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host ="localhost", port="5432")
cur = conn.cursor()

# check arguments
if len(sys.argv) == 2:
    # parse k1 and k2 arguments and turn into integers for iteration
    k1 = int(sys.argv[1].split(",")[0])
    k2 = int(sys.argv[1].split(",")[1])
    for count in list(range(k1,k2+1)):
        cur.execute("SELECT word, count from tweetwordcount WHERE count=%s",(str(count),))
        records = cur.fetchall()
        for rec in records:
            print rec[0],": ",rec[1]
else:
    print("Bin intervals missing. Please enter two numbers separated by a comma.")
    exit(1)

# close connection
conn.close()

