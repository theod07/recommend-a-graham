# recommend-a-graham

## postgres

CREATE TABLE tracker (
	shortcode text,
	username text,
	img_id text,
	predicted boolean DEFAULT BOOL(0),
	PRIMARY KEY(shortcode)
);

