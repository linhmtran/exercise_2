Exercise 2 Instructions
1. Set up the postgres database and table by running psycopg-setup.py in
/exercise_2. This should create the tcount database and tweetcount table.
2. Stream live twitter feed by moving to /exercise_2/extweetcount/ and
running 'sparse run' at the command line. This will start updating live
twitter feeds into the tweetcount table in tcount database. You will see the
twitter word counts stream on the commmand line simultaneously. Ctrl-c to end
stream.
3. Query twitter wordcount results using finalresults.py or histogram.py at
the command line under directory /exercise_2
