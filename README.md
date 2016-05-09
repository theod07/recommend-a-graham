# recommend-a-graham

## postgres

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

CREATE TABLE fc6 (
	shortcode text,
	fc6 text,
	PRIMARY KEY(shortcode)
);


To Do:

1. Calculate mean vector for each existing_user (softmax, fc8, fc7)
2. Calculate mean vector for new_user
3. Calculate cosine_similarity(existing_users, new_user)
4. Get top20_most_similar users. Do they make sense?


