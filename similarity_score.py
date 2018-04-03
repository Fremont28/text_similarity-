#get twitter feeds 
def twitter_setup():
    #create twitter app
    consumer_key = 'aSIenX8nyf75Lx3no4j5xuw3a'
    consumer_secret = 'dzQPbwEGcGfTB0uSRuRWxaHxbRpGr68jpS8SNG2lk2FFUtRc3o'
    access_token = '42704027-Aj1hOUheQ0awUF1Bepayab2G8q57mOvyPIuWj4YSl'
    access_secret = 'Ab2MS9fSqybmS6t6BM6fQojEKjU72PPjkwz81iDbZpMs9'
    #import libraries
    import tweepy
    import credentials
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # Return API with authentication:
    api = tweepy.API(auth)
    return api

#create an extractor object
#twitter stream 1 
extractor=twitter_setup()
tweets=extractor.user_timeline(screen_name="atlanta",count=1000)
tweets1=[]
for tweet in tweets:
    tweets1.append(tweet.text)
tweets2=''.join(tweets1) #convert from list to string

#twitter stream 2 
tweets_x=extractor.user_timeline(screen_name="WaffleHouse",count=1000)
tweets1x=[]
for tweet in tweets_x:
    tweets1x.append(tweet.text)
tweets2x=''.join(tweets1x)

#returns similarity score between two twitter feeds 
def food_similarity(x,y):
    #import libraries
    import sklearn 
    from sklearn.feature_extraction.text import TfidfVectorizer
    #compare two twitter feeds
    documents=x,y
    tfidf=TfidfVectorizer().fit_transform([x,y])
    return ((tfidf*tfidf.T).A)[0,1]

food_compare=food_similarity(tweets2,tweets2x)
food_compare

