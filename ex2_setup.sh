cp /home/w205/w205-fall-17-labs-exercises/exercise_2/tweetwordcount/src/spouts/tweets.py .

cd ..
cd bolts
rm wordcount.py
ls -l

cp /home/w205/w205-fall-17-labs-exercises/exercise_2/tweetwordcount/src/bolts/parse.py .
cp /home/w205/w205-fall-17-labs-exercises/exercise_2/tweetwordcount/src/bolts/wordcount.py .

cd ..
cd ..
cd ..

cp /home/w205/w205-fall-17-labs-exercises/exercise_2/Twittercredentials.py .
cp /home/w205/w205-fall-17-labs-exercises/exercise_2/hello-stream-twitter.py .
cp /home/w205/w205-fall-17-labs-exercises/exercise_2/hello-stream-twitter.py .

# go to topologies folder
cp /home/w205/w205-fall-17-labs-exercises/exercise_2/tweetwordcount/topologies/tweetwordcount.clj .

#go to exercise_2
cp /home/w205/w205-fall-17-labs-exercises/exercise_2/psycopg-sample.py .

# checking postgres
psql -U postgres #open postgres
# \l to list databases
# \c tcount to connect to tcount
# \dt to show Table details
# select *from <table>;
