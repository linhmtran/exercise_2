import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#connect to Database
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host ="localhost", port="5432")
cur = conn.cursor()

# check arguments
if len(sys.argv) != 2:
    # if arguments missing, print all word counts
    cur.execute("SELECT word, count from tweetwordcount")
    records = cur.fetchall()
    for rec in records:
        print "(",rec[0],",",rec[1],")",
else:
    # return count for single argument word
    word = sys.argv[1]
    cur.execute("SELECT word, count from tweetwordcount WHERE word=%s",(word,))
    records = cur.fetchall()
    for rec in records:
        print "(",rec[0],",",rec[1],")"

# close connection
conn.close()

