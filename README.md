<div align="center" >
  <img width="330"  src="/slides/Slide01.jpg">
</div>

![alt text](/slides/Slide01.jpg "Slide01")

![alt text][Slide04]
![alt text][Slide06]

[Slide04]: ./slides/Slide04.jpg "Slide04"
[Slide06]: ./slides/Slide06.jpg "Slide06"
[Slide07]: ./slides/Slide07.jpg "Slide07"
[Slide08]: ./slides/Slide08.jpg "Slide08"
[Slide09]: ./slides/Slide09.jpg "Slide09"
[Slide10]: ./slides/Slide10.jpg "Slide10"
[Slide11]: ./slides/Slide11.jpg "Slide11"
[Slide12]: ./slides/Slide12.jpg "Slide12"
[Slide14]: ./slides/Slide14.jpg "Slide14"
[Slide15]: ./slides/Slide15.jpg "Slide15"
[Slide16]: ./slides/Slide16.jpg "Slide16"
[Slide17]: ./slides/Slide17.jpg "Slide17"
[Slide18]: ./slides/Slide18.jpg "Slide18"
[Slide19]: ./slides/Slide19.jpg "Slide19"
Most of us here are familiar with Instagram. Sometimes we're greeted with selfies. Sometimes we're greeted with foodies. I don't know about you, but I'm not terribly interested in celebrity selfies and fancy hamburgers.


It's hard to find relevant content on Instagram. We could search for hashtags, but that requires that you know what you're looking for before hand. And even if we did, we'd get back images that have been tagged. What if we could use the content of the images, instead?


Let's say you're interested in dogs -- patriotic, fourth of july dogs. Here's something you might enjoy.
Or maybe you enjoy cinematic aerial views of san francisco. You might love this one here.
My objective is to do this type of content-based recommendation.


Here's the pipeline i used to do this.
I used selenium webdriver for data collection from instagram.
Data storage and management using postgres database.
Images were featurized by a neural network trained on imagenet dataset.
Used python's scikit-learn library to analyze featurized images.


My first approach was the natural one: represent each user as an average of their images and compare users via cosine similarity. I tested this using an input of cat images, the model recommended Justin Bieber.
I knew that couldn't be right. Back to the drawing board.


My next approach was to use TF-IDF.
The benefit with this is that the model is additive and it penalizes less significant features.


A quick primer on TF-IDF:
Let's say we have these three strings of words.
The set of all strings is our corpus.
We'll call each string is a document.
Each document has a word count. In s3, "the" and "cat" each show up once, and everything else is zero. We'll call this a term frequency vector.
We can also look at the count of documents that contain each term to get an IDF vector. This is the money maker. Terms that show up often have a larger denominator and are valued less.


Here are some results of this method:
The output for this cat profile is that cat profile.
The output for this dog profile is that dog profile.
Here's a result that i found interesting. The input profile is from my travel category, but the recommended profile is from my most_popular category. At first glance, that seems like it would be a bad recommendation, but when we take a closer look we can see that both profiles have images of natural scenery.

I know that this model is performing well because the output for this travel profile is that most_popular profile. Even though these profiles belong to different categories, we as humans we can see similar themes among the images.

[slide01]: (https://github.com/theod07/recommend-a-graham/blob/master/slides/Slide01.jpg) "Slide01"
