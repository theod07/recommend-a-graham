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


Given two categories, Cats & Dogs, here are the top 5 recommended users over a few attempts. Only cat images liked, not dog images.
1. categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['hangarang' 'heysp' 'mattslaby' 'davidluiz_4' 'puma']
group: most_popular  user: hangarang 
group: photographers  user: heysp 
group: photographers  user: mattslaby 
group: most_popular  user: davidluiz_4 
group: most_popular  user: puma 

2. categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['jacobamorton' 'hangarang' 'arishapiro' 'bortnikovrussia' 'puma']
group: models  user: jacobamorton 
group: most_popular  user: hangarang 
group: most_popular  user: arishapiro 
group: most_popular  user: bortnikovrussia 
group: most_popular  user: puma 

3. categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['makicocomo' 'amivitale' 'arishapiro' 'davidluiz_4' 'tifforelie']
group: cats  user: makicocomo 
group: photographers  user: amivitale 
group: most_popular  user: arishapiro 
group: most_popular  user: davidluiz_4 
group: foodies  user: tifforelie

4. categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['mattslaby' 'tifforelie' 'ferggotti' 'puma' 'bortnikovrussia']
group: photographers  user: mattslaby 
group: foodies  user: tifforelie 
group: most_popular  user: ferggotti 
group: most_popular  user: puma 
group: most_popular  user: bortnikovrussia 

5. categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['makicocomo' 'amivitale' 'arishapiro' 'davidluiz_4' 'tifforelie']
group: cats  user: makicocomo 
group: photographers  user: amivitale 
group: most_popular  user: arishapiro 
group: most_popular  user: davidluiz_4 
group: foodies  user: tifforelie


What if we change the preferences around to all dogs, no cats?

1. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['makicocomo' 'manchesterunited' 'sellsneakershere' 'rapo4' 'arishapiro']
group: cats  user: makicocomo 
group: most_popular  user: manchesterunited 
group: most_popular  user: sellsneakershere 
group: foodies  user: rapo4 
group: most_popular  user: arishapiro 

2. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['nasagoddard' 'ryan.abernathy' 'rapo4' 'sellsneakershere' 'humative']
group: most_popular  user: nasagoddard 
group: travel  user: ryan.abernathy 
group: foodies  user: rapo4 
group: most_popular  user: sellsneakershere 
group: dogs  user: humative 

3. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['lonelyplanet' 'jimmyfallon' 'onedirection' 'thegrammys' 'milwaukeebucks']
group: travel  user: lonelyplanet 
group: most_popular  user: jimmyfallon 
group: most_popular  user: onedirection 
group: most_popular  user: thegrammys 
group: most_popular  user: milwaukeebucks

4. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['theonion' 'rapo4' '9gag' 'sellsneakershere' 'arishapiro']
group: most_popular  user: theonion 
group: foodies  user: rapo4 
group: most_popular  user: 9gag 
group: most_popular  user: sellsneakershere 
group: most_popular  user: arishapiro 

5. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['rapjuggernaut' 'simonebirch' 'humative' '49ers' 'reuters']
group: most_popular  user: rapjuggernaut 
group: travel  user: simonebirch 
group: dogs  user: humative 
group: most_popular  user: 49ers 
group: most_popular  user: reuters 