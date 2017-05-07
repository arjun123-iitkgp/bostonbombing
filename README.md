# twitter-data-analysis
Getting started with Twitter data analysis.
<h1>Jupyter Notebooks</h1>
<ul>
<li><b>StopwordsRemoval.ipynb</b>: Stopwords are removed in this notebook. Look StopWords Removal heading for details. Changes saved in 'tweets_dataframe.csv'</li>
<li><b>Remove@tags.ipynb</b>: The @ tags of twitter are removed in this. Also, the links present in the tweets are seperated, saved in csv. Changes saved in 'tweets_dataframe.csv' </li>
<li><b>WordMatrix.ipynb</b>: Stemming performed and a matrix, a dictionary formed denoting the unique words and their frequency in dataset. The resultant matrix: [No. of unique words][Tweet Nos] is also saved in the form of 'wordmatrix.csv' file. The words appear in order of their frequency. I analysed and found that stemming helps in calculating more accurate word frequencies as shown in the notebook. This also reduces the size of wordmatrix and it's spareseness.</li>
<li><b>TFIDF.ipynb</b>:Performed TFIDF calculations over the generated wordmatrix. For details see below.</li>
</ul>

<h1>Stopwords Removal</h1>
<ul>
<li>The concerned notebook is "StopWordRemoval.ipynb". </li>
<li>The stopwords present in nltk toolkit were not enough in for the tweet texts because of the presence of slang words.</li>
<li>So, I used a specialised repository <a href="https://sites.google.com/site/iamgongwei/home/sw">from here.</a>. It is that repo present as Stopwords in this project.</li>
<li>Added all stopwords from the repo in a set. Removed from the original dataset.</li>
<li>Then I removed all the links present using regex expressions, which left a few lingering around.</li>
<li>Then I printed a list of most frequent 100 words in the dataset, added a few more stopwords such as '-' etc to the set, removed them from dataset.</li>
<li>Follwing this I tried to remove the @tags, when I realised that I removed stopwords from the dataset without making the text to lowercase (as the stopwords were lowercase.)</li>
<li>Went back to RemoveStopwords.ipynb, changed all tweets to lowercase and removed stopwords again.</li>
<li>Then, in Remove@Tags.ipynb, removed @tags, this time I made sure my regex doesn't miss various cases. </li>
<li>All the changes are overwritten in the original file "tweets_dataframe.csv."
</ul>

<h1>WordMatrix</h1>
<ul>
<li>Concerned Jupyter Notebook: "WordMatrix.ipynb"</li>
<li>Although the wordmatrix is finally saved in "wordmatrix.csv", it is present as default dictionary in the notebook.</li>
<li> The matrix obtained here is very sparse, obviously.</li>
</ul>

<h1>Stemming</h1>
<ul>
<li>Used more powerful stemmer than PorterStemmer.</li>
<li>Thought a lot about why should I do it. Then I analyzed it, as shown in wordmatrix.ipynb, and it helps.</li>
<li>Thuogh, I have not made the changes in original tweet texts of 'tweets_dataframe.csv'</li>
<li>The words in the index of 'wordmatrix.csv' are now in the order of their frequency in the dataset i.e. more frequent words appears above less frequent words in the csv file.</li>
<li>Appropriately, the matrix results are also displayed in the similar manner.</li>
</ul>


<h1>TFIDF Calculation</h1>
<ul>
<li>Used the wordmatrix created earlier to perform TF-IDF calculation.</li>
<li>Instead of doing it in 2 steps, I have performed it directly over the wordmatrix using this formula:</li>
TFIDF[i,j] = ( Ni,j / N*,j ) * log( D / Di )
#Ni,j = the number of times word i appears in document j (the original cell count).
#N*,j = the number of total words in document j (just add the counts in column j).
#D = the number of documents (the number of columns).
#Di = the number of documents in which word i appears (the number of non-zero columns in row i).

<li>Took care of corner cases e.g when denominators can be zero.</li>
<li>Created a dataframe from the tfidf matrix and saved the matrix as <b>tfidf.csv</b>.</li>
</ul>

