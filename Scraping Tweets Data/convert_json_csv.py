from nltk.twitter.common import json2csv

#absolute path for the file: #input_file = os.path.abspath(jsonfile)=>returns virtualenv file path
input_file = '/home/mradul/twitter-files/Tweets.json'
#with open(input_file) as fp:
	#json2csv(fp,'tweets_text.csv',['text']) #json2csv(pointer, nameoffile, [feature1,feature2,feature3])

#think about the attributes to be imported, convert to panda, make a dataframe, apply stemming to tweet texts, save them. 
with open(input_file) as fp:
	json2csv(fp, 'boston.csv',['text','id','from_user','iso_language_code'])
#json, csv