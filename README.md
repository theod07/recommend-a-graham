# recommend-a-graham

## postgres

CREATE TABLE tracker (
	shortcode text,
	username text,
	img_id text,
	predicted int DEFAULT 0,
	PRIMARY KEY(shortcode)
);

CREATE TABLE pred_1 (
	shortcode text,
	pred_1 decimal, 
	PRIMARY KEY(shortcode) 
);

CREATE TABLE pred_2 (
	shortcode text,
	pred_2 decimal, 
	PRIMARY KEY(shortcode) 
);


To Do:

1. Modify image preprocessing step. Rescale image to match  `net['input'] = InputLayer((None, 3, 224, 224))`
2. 
