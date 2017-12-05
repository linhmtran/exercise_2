import tweepy

consumer_key = "fKWLGDmpqPVAnLWjyvEMlpbKg";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "LwBX6fX4uv7srhGoXoj4NKNTsk71uFO02hRwRLFoHz1BEUD2H1";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "57261602-Js5ZQtdjihpZUDzNyDbVGaXvwzOfMZSJGl1dNKV17";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "7bhXWcB3DqT6M5ewbVBOyFL8QY9W8uljpfhswDOz2Vjcx";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

