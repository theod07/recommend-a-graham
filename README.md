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

1. Modify image preprocessing step. Rescale image to match  `net['input'] = InputLayer((None, 3, 224, 224))`
2. 
