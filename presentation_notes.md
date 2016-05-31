Presentation Outline


Introduction
- Motivation
- Recommendation Systems
- Data collection / Scraping
- Data management & storage
- Neural Networks
- Curse of Dimensionality
- Principle Component Analysis & Singular Value Decomposition
- TfIdf
- Results
- Future Work

Motivation
- instagram has a lot of information about you, they belong to facebook after all
- as such, they know a lot about your social network and all of their activity.
- they know who likes what and use that as a way to recommend content to you.
- that is, they use a social influence graph to recommend content.
- but what if we had a recommender system that didn't need social network information about its users? Only required data about the content?
- in this presentation, I'll show you my approach to a content-based recommender system for images
- instagram. what is it?
- facebook. what is it?
- Instagram
- why is it important?


Recommendation systems / Collaborative Filtering
- we've all experienced recommender systems. anytime you buy something from a website you get a personalized set of recommendations.
- Netflix, Amazon, <insert_ecommerce_here>
- ubiquitous! how does it work?
- Netflix: Utility Matrix shows every user's rating (1-5) of every item. Downside is that this is sparse matrix.
- Amazon: Can treat an item as the vector across users and compare similarities between items.


Measuring Similarity
- Euclidean Distance: dist(a,b) = ||a-b|| = sqrt((a-b)*(a-b))
- Euclidean Distance = 0 means items are identical
- Pearson Correlation: cov(a,b)/std(a)/std(b)
    - also known as normalized covariance
    - benefit: not sensitive to user who consistently rates low or high: 5,5,1 same as 3,3,1
-Cosine Similarity: measures angle between vectors
    - cosine_sim(a,b) = a.dot(b)/||a||/||b||


Similarity matrix
- Once we decide on a similarity metric, can compute a similarity matrix
- item-item similarity is symmetric because similarity(x,y) = similarity(y,x)
Alterative Methods
- Netflix uses matrix factorization
- can also use user-user similarity. Same concept as item-item

Data Collection
- Subgroups of Profiles
- Cats, Dogs, Foodies, Models, Most Popular, Photographers, Travel
- Searched for users belonging to each category via our friend Google!
- Attempted to collect information via Instagram API, but too limited
- Resort to downloading images from each user manually

Scraping images
- Architecture of Instagram Profile / Challenges
- Pesky "Load More" button. Only 12 images shown on profile home page
- Page is hidden by javascript  
- Infinite scroll, loading 15 images at a time when you reach bottom of page
- BeautifulSoup, Requests, Scrapy all rendered helpless
- Enter Selenium browser. Opens up a full browser and loads the javascript on page

Selenium Browser Data Collection
- Multiple iterations to get it right
- Load page
- Scroll down to bottom of page
- Manually click "Load More" button via tag-selection
- Scroll down, pause...
- Scroll down, pause...
- Scroll down, pause...
- ...
- Program a macro to save all content
- Drawbacks
- Must be run in the foreground
- Slow: latency
- Slow: load javascript
- Slow: avoid block IP


Data management
- Raw Instagram files saved locally on distributed machines
- Periodic batch uploads to AWS S3
- Calculated values stored and managed via Postgres Relational Database
- Access Postgres data via python wrapper psycopg2

  Postgres Tables
  CREATE TABLE tracker (
  	shortcode text,
  	username text,
  	img_id text,
  	predicted int DEFAULT 0,
  	PRIMARY KEY(shortcode)
  );

  CREATE TABLE softmax (
  	shortcode text,
  	softmax text,
  	PRIMARY KEY(shortcode)
  );

  CREATE TABLE fc8 (
  	shortcode text,
  	fc8 text,
  	PRIMARY KEY(shortcode)
  );

  CREATE TABLE fc7 (
  	shortcode text,
  	fc7 text,
  	PRIMARY KEY(shortcode)
  );


Neural Networks
- We have the data/images now, cool. Now what?
- Enter the Neural Network
- Pros:
  - works well with high dimensional data
  - 1 image: 256x256x3 = 196,608 elements per image vector
  - Natural choice for images. High dimensionality, highly correlated
- Cons:
  - Not interpretable
  - Slow to train
  - Easy to overfit
  - Difficult to tune

- I think of a neural network as logistic regression on steroids.
- People spend entire graduate studies looking at neural networks and how to tune them.
- Fortunately for me, I'm able to stand on the shoulders of giants and treat the neural network as a black box.


Transfer Learning
- ImageNet -- annual challenge to detect/identify objects and classification/localization
- Training can take months, even on GPU.
- Fortunately, smart people have done the work for us which allowed me to implement it quickly in Lasagne, which is a python wrapper for the Theano-based model.
- Neural networks provide an engine for us to featurize our data for us so that we don't have to go through and manually engineer features. This is a huge benefit for data of this size!
- Can use neural network as a black box to generate features!


VGG-16 Architecture
- Pretrained neural network VGG-16 from a team at University of Oxford
- Input layer
- 13x Convolutional layers
- 5x Pooling layers
- 3x Fully connected layers, separated by dropout layers (p=0.5)
- Softmax output layer


Example Outputs:
We're not only limited to the final output of the network. Also have access to intermediate layers!
Softmax Output -- 1000-element stored in postgres database
fc8 Output -- 1000-element stored in postgres database
fc7 Output -- 4096-element stored in postgres database
**sparse vector**

Methodology & Approach
- Now that we have vectors for our images, we can group them together to represent various Instagram profiles.
- The natural idea would be to represent a user by the mean of their images
- We could then represent every profile as the mean of their images and compare similarity between them, eg. cosine similarity
(img1 + img2 + ... + imgN)/N = UserPreference or UserStyle
- Can take a np.mean([img for img in imgs]), easy!

Results
- Easy? Yes!
- Useful? No!
- Results did not seem very good. No signal.
- What could it be...?


What is the Curse of Dimensionality?
- Any data we have comes with features/predictors/variables that we can use to guess an outcome
- It's not uncommon to want more information about a situation to make a more informed decision
- However, it turns out that there is a point where having more features/predictors/variables becomes detrimental to our ability to decide!
- As we increase the number of features in our model, the distance between points quickly explodes and we lose the density required for statistical significance. Our feature space quickly becomes sparse and unhelpful.
- So we went from 196,608 dimensions per image to 4096 dimensions per image (fc7) to 1000 dimensions per image (fc8, softmax). That's a huge improvement!
- But we still have fewer observations (Instagram profiles) than our feature space!
- How can we resolve this issue?


Dimensionality Reduction to the Rescue!
- Principle Component Analysis helps us reduce dimensionality further by finding new basis for our data.
- Matrix decomposition method through calculating the eigenvalue/eigenvectors of our feature covariance matrix.
- Eigenvectors give us the new basis for dimensions.
- Eigenvalues tell us the variance along each dimension.
- Goal: reduce dimensionality so that most variance in data is still explained


Results of PCA
- This curve is so round! OH NO!
- Hoping to see a sharp decay that will help us determine cutoff point. No luck.
- Try it anyway for 90% explained.. no good
- Try it anyway for 80% explained.. no good
- Try it anyway for 70% explained.. no good
- Try it anyway for 60% explained.. no good
- Try it anyway for 50% explained.. down to # features now, and results are still no good
- Why do celebrities keep showing up in my results?
- I cannot recommend JustinBieber to people in good conscience!


Cry.. Take a coffee break. Coffee break lasts a week.
What's going on??


Maybe taking the mean of a bunch of images is tainting my results. If I have a user who really enjoys posting photos of their cat and photos of natural landscape, the average of those vectors will be significantly different from the average of a bunch of cat photos and the average of a bunch of landscape photos. Taking the mean like this wipes away any signal we extracted from our neural network
The key is to not take the mean!


Enter Tf-Idf! Term Frequency - Inverse Document Frequency
- Used in Natural Language Processing for information retrieval
- Terminology:
  - Corpus -- a dataset of text, eg. newspaper, tweets, etc...
  - Document --  a single body of text from Corpus
  - Vocabulary -- distinct list of all words in Corpus
  - Token -- an instance of a word in a document


Tf-Idf: How it works
- Treats each document as a bag of words:
Featurizes a body of text by counting the number of times each word appears, don't care about language structure. Call that the Term Frequency.
Example from Kamil's ipynb
- Document Freqency is the ratio of number of documents that contain a term to the total number of documents in corpus
- Inverse Document Frequency = log( 1/df(term, corpus) )


So what? How does it relate to Neural Networks and Recommenders?
- Excellent question, I'm glad you asked!
- Document => Image
- Term Frequency => NN Output Vector
- Corpus => Collection of images
- use the vectors from Neural Network as the term-frequency for each image
- represent each user as the sum of their images
- calculate tfidf for all users
- Benefit: tfidf is not adversely affected by summation of vectors!


Results


Future Work
