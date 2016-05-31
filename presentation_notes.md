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


VGG-16 Architecture
- Pretrained neural network VGG-16 from a team at University of Oxford
- Input layer
- 13x Convolutional layers
- 5x Pooling layers
- 3x Fully connected layers, separated by dropout layers (p=0.5)
- Softmax output layer

Softmax Output -- 1000-element stored in postgres database
fc8 Output -- 1000-element stored in postgres database
fc7 Output -- 4096-element stored in postgres database
