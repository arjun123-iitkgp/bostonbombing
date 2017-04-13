from nltk.corpus import twitter_samples
from nltk.twitter.common import json2csv

#corpus twitter_sample tweets ~20k
jsonfile = twitter_samples.fileids()[-1]

#absolute path for the file: #input_file = os.path.abspath(jsonfile)=>returns virtualenv file path
input_file = twitter_samples.abspath(jsonfile) #returns system /usr/share/ path

#with open(input_file) as fp:
	#json2csv(fp,'tweets_text.csv',['text']) #json2csv(pointer, nameoffile, [feature1,feature2,feature3])

#think about the attributes to be imported, convert to panda, make a dataframe, apply stemming to tweet texts, save them. 
with open(input_file) as fp:
	json2csv(fp, 'tweets_dataframe.csv',['id','text','user.favourites_count','user.id','lang','user.followers_count','user.verified','truncated'])

