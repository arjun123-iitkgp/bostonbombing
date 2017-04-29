# twitter-data-analysis
Getting started with Twitter data analysis.
<h1>Stopwords Removal</h1>
<ul>
<li>The stopwords present in nltk toolkit were not enough in for the tweet texts because of the presence of slang words.</li>
<li>So, I used a specialised repository <a href="https://sites.google.com/site/iamgongwei/home/sw">from here.</a>. It is that repo present as Stopwords in this project.</li>
<li>Added all stopwords from the repo in a set. Removed from the original dataset.</li>
<li>Then I removed all the links present using regex expressions, which left a few lingering around.</li>
<li>Then I printed a list of most frequent 100 words in the dataset, added a few more stopwords such as '-' etc to the set, removed them from dataset.</li>
<li>Follwing this I tried to remove the @tags, when I realised that I removed stopwords from the dataset without making the text to lowercase (as the stopwords were lowercase.)</li>
<li>Went back to RemoveStopwords.ipynb, changed all tweets to lowercase and removed stopwords again.</li>
<li>Then, in Remove@Tags.ipynb, removed @tags, this time I made sure my regex doesn't miss various cases. </li>
</ul>


