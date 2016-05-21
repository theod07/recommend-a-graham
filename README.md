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
most_sim_users : ['jacobamorton' 'mattslaby' 'shanelavalette' 'theblondegypsy'
 'skylerwagoner' 'davidluiz_4' 'nationalpost' 'bkstreetart' 'puma'
 'justinbieber']
group: models  user: jacobamorton 
group: photographers  user: mattslaby 
group: photographers  user: shanelavalette 
group: travel  user: theblondegypsy 
group: photographers  user: skylerwagoner 
group: most_popular  user: davidluiz_4 
group: most_popular  user: nationalpost 
group: photographers  user: bkstreetart 
group: most_popular  user: puma 
group: most_popular  user: justinbieber 

2. categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['nationalpost' 'arishapiro' '49ers' 'ferggotti' 'thekillertruth'
 'tifforelie' 'bortnikovrussia' 'heysp' 'mattslaby' 'davidluiz_4']
group: most_popular  user: nationalpost 
group: most_popular  user: arishapiro 
group: most_popular  user: 49ers 
group: most_popular  user: ferggotti 
group: most_popular  user: thekillertruth 
group: foodies  user: tifforelie 
group: most_popular  user: bortnikovrussia 
group: photographers  user: heysp 
group: photographers  user: mattslaby 
group: most_popular  user: davidluiz_4

3.  categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['graciethelabrador' 'makicocomo' 'ferggotti' 'reuters' 'humative'
 'sellsneakershere' 'rapo4' 'bortnikovrussia' 'puma' 'arishapiro']
group: dogs  user: graciethelabrador 
group: cats  user: makicocomo 
group: most_popular  user: ferggotti 
group: most_popular  user: reuters 
group: dogs  user: humative 
group: most_popular  user: sellsneakershere 
group: foodies  user: rapo4 
group: most_popular  user: bortnikovrussia 
group: most_popular  user: puma 
group: most_popular  user: arishapiro 

4. categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['jacobamorton' 'aabbyylou' 'mattslaby' 'hamilton_the_hipster_cat'
 'shanelavalette' 'bkstreetart' 'davidluiz_4' 'nationalpost' 'ferggotti'
 'bortnikovrussia']
group: models  user: jacobamorton 
group: photographers  user: aabbyylou 
group: photographers  user: mattslaby 
group: cats  user: hamilton_the_hipster_cat 
group: photographers  user: shanelavalette 
group: photographers  user: bkstreetart 
group: most_popular  user: davidluiz_4 
group: most_popular  user: nationalpost 
group: most_popular  user: ferggotti 
group: most_popular  user: bortnikovrussia 


5. categories: ['cats', 'dogs'], vtype: fc7
most_sim_users : ['bkstreetart' 'justintimberlake' 'reuters' 'ashleyrparker' 'arishapiro'
 'othellonine' 'aabbyylou' 'shanelavalette' 'nationalpost' 'puma']
group: photographers  user: bkstreetart 
group: most_popular  user: justintimberlake 
group: most_popular  user: reuters 
group: most_popular  user: ashleyrparker 
group: most_popular  user: arishapiro 
group: photographers  user: othellonine 
group: photographers  user: aabbyylou 
group: photographers  user: shanelavalette 
group: most_popular  user: nationalpost 
group: most_popular  user: puma 



What if we change the preferences around to all dogs, no cats?

1. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['49ers' 'ashleyrparker' 'rapjuggernaut' 'reuters' 'bortnikovrussia'
 'rapo4' 'michaelbaileygates' 'artisticvoid' 'sellsneakershere' 'humative']
group: most_popular  user: 49ers 
group: most_popular  user: ashleyrparker 
group: most_popular  user: rapjuggernaut 
group: most_popular  user: reuters 
group: most_popular  user: bortnikovrussia 
group: foodies  user: rapo4 
group: models  user: michaelbaileygates 
group: dogs  user: artisticvoid 
group: most_popular  user: sellsneakershere 
group: dogs  user: humative 

2. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['reuters' 'rapo4' 'ashleyrparker' 'parislemon' 'sellsneakershere'
 'bortnikovrussia' 'humative' '49ers' 'arishapiro' 'tunameltsmyheart']
group: most_popular  user: reuters 
group: foodies  user: rapo4 
group: most_popular  user: ashleyrparker 
group: most_popular  user: parislemon 
group: most_popular  user: sellsneakershere 
group: most_popular  user: bortnikovrussia 
group: dogs  user: humative 
group: most_popular  user: 49ers 
group: most_popular  user: arishapiro 
group: dogs  user: tunameltsmyheart 

3. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['artisticvoid' 'makicocomo' 'sellsneakershere' 'ashleyrparker'
 'tunameltsmyheart' 'rapjuggernaut' 'rapo4' 'manchesterunited'
 'michaelbaileygates' 'humative']
group: dogs  user: artisticvoid 
group: cats  user: makicocomo 
group: most_popular  user: sellsneakershere 
group: most_popular  user: ashleyrparker 
group: dogs  user: tunameltsmyheart 
group: most_popular  user: rapjuggernaut 
group: foodies  user: rapo4 
group: most_popular  user: manchesterunited 
group: models  user: michaelbaileygates 
group: dogs  user: humative

4. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['lonelyplanet' 'simonebirch' 'makicocomo' 'graciethelabrador'
 'othellonine' 'artisticvoid' 'humative' 'rapo4' 'reuters'
 'sellsneakershere']
group: travel  user: lonelyplanet 
group: travel  user: simonebirch 
group: cats  user: makicocomo 
group: dogs  user: graciethelabrador 
group: photographers  user: othellonine 
group: dogs  user: artisticvoid 
group: dogs  user: humative 
group: foodies  user: rapo4 
group: most_popular  user: reuters 
group: most_popular  user: sellsneakersher

5. categories: ['dogs', 'cats'], vtype: fc7
most_sim_users : ['jacobamorton' 'manchesterunited' 'ashleyrparker' 'amivitale'
 'nasagoddard' 'reuters' 'rapo4' 'artisticvoid' 'arishapiro'
 'sellsneakershere']
group: models  user: jacobamorton 
group: most_popular  user: manchesterunited 
group: most_popular  user: ashleyrparker 
group: photographers  user: amivitale 
group: most_popular  user: nasagoddard 
group: most_popular  user: reuters 
group: foodies  user: rapo4 
group: dogs  user: artisticvoid 
group: most_popular  user: arishapiro 
group: most_popular  user: sellsneakershere 


What about when we like foodies, no dogs?

1. categories: ['foodies', 'dogs'], vtype: fc7
most_sim_users : ['patricknorton' 'kevinmiyazaki' 'acouplecooks' 'andersoncooper'
 'lukasabbat' 'mchammer' 'dogsofinstagram' 'reemteam' 'sellkixcity'
 'gjelinatakeaway']
group: most_popular  user: patricknorton 
group: photographers  user: kevinmiyazaki 
group: foodies  user: acouplecooks 
group: most_popular  user: andersoncooper 
group: models  user: lukasabbat 
group: most_popular  user: mchammer 
group: dogs  user: dogsofinstagram 
group: most_popular  user: reemteam 
group: most_popular  user: sellkixcity 
group: foodies  user: gjelinatakeaway

2. categories: ['foodies', 'dogs'], vtype: fc7
most_sim_users : ['youngthegiant' 'photogeekdom' 'sellkixcity' 'witchoria' 'kidfella'
 '_voguevariety' 'uncornered_market' 'joythebaker' 'modelisy' 'reemteam']
group: most_popular  user: youngthegiant 
group: most_popular  user: photogeekdom 
group: most_popular  user: sellkixcity 
group: photographers  user: witchoria 
group: most_popular  user: kidfella 
group: most_popular  user: _voguevariety 
group: travel  user: uncornered_market 
group: foodies  user: joythebaker 
group: most_popular  user: modelisy 
group: most_popular  user: reemteam 

3. categories: ['foodies', 'dogs'], vtype: fc7
most_sim_users : ['kevinmiyazaki' 'ashleighannah' 'ideal' 'gjelinatakeaway' 'nickiminaj'
 'lucyfarted' 'dogsofinstagram' 'reemteam' 'lukasabbat' 'mchammer']
group: photographers  user: kevinmiyazaki 
group: models  user: ashleighannah 
group: most_popular  user: ideal 
group: foodies  user: gjelinatakeaway 
group: most_popular  user: nickiminaj 
group: dogs  user: lucyfarted 
group: dogs  user: dogsofinstagram 
group: most_popular  user: reemteam 
group: models  user: lukasabbat 
group: most_popular  user: mchammer


4. categories: ['foodies', 'dogs'], vtype: fc7
most_sim_users : ['youngthegiant' 'vindiesel' 'lucyfarted' 'acouplecooks' 'mchammer'
 'photogeekdom' 'witchoria' 'andersoncooper' 'reemteam' 'lukasabbat']
group: most_popular  user: youngthegiant 
group: most_popular  user: vindiesel 
group: dogs  user: lucyfarted 
group: foodies  user: acouplecooks 
group: most_popular  user: mchammer 
group: most_popular  user: photogeekdom 
group: photographers  user: witchoria 
group: most_popular  user: andersoncooper 
group: most_popular  user: reemteam 
group: models  user: lukasabbat

5. categories: ['foodies', 'dogs'], vtype: fc7
most_sim_users : ['lukasabbat' 'kidfella' 'ideal' 'ladygaga' 'kevinmiyazaki'
 'dogsofinstagram' 'uncornered_market' 'gjelinatakeaway' 'acouplecooks'
 'jackswifefreda']
group: models  user: lukasabbat 
group: most_popular  user: kidfella 
group: most_popular  user: ideal 
group: most_popular  user: ladygaga 
group: photographers  user: kevinmiyazaki 
group: dogs  user: dogsofinstagram 
group: travel  user: uncornered_market 
group: foodies  user: gjelinatakeaway 
group: foodies  user: acouplecooks 
group: foodies  user: jackswifefreda 


Travel vs foodies?

1. categories: ['travel', 'foodies'], vtype: fc7
most_sim_users : ['parisinfourmonths' 'barbershopconnect' 'floydmayweather' 'treyratcliff'
 'budgettraveller' 'cirquedusoleil' 'oceana' 'danrubin' 'mayrilyn'
 'lacikaysomers']
group: travel  user: parisinfourmonths 
group: most_popular  user: barbershopconnect 
group: most_popular  user: floydmayweather 
group: travel  user: treyratcliff 
group: travel  user: budgettraveller 
group: most_popular  user: cirquedusoleil 
group: most_popular  user: oceana 
group: photographers  user: danrubin 
group: cats  user: mayrilyn

2. categories: ['travel', 'foodies'], vtype: fc7
most_sim_users : ['year' 'elnuevodiariord' 'shakira' 'stevenchevrin' 'zachking' 'foodzie'
 'vanessahudgens' 'paniexx_shop' 'starbucks' 'macenzo']
group: most_popular  user: year 
group: most_popular  user: elnuevodiariord 
group: most_popular  user: shakira 
group: models  user: stevenchevrin 
group: most_popular  user: zachking 
group: most_popular  user: foodzie 
group: most_popular  user: vanessahudgens 
group: most_popular  user: paniexx_shop 
group: most_popular  user: starbucks 
group: photographers  user: macenzo 

3. categories: ['travel', 'foodies'], vtype: fc7
most_sim_users : ['year' 'elnuevodiariord' 'shakira' 'stevenchevrin' 'zachking' 'foodzie'
 'vanessahudgens' 'paniexx_shop' 'starbucks' 'macenzo']
group: most_popular  user: year 
group: most_popular  user: elnuevodiariord 
group: most_popular  user: shakira 
group: models  user: stevenchevrin 
group: most_popular  user: zachking 
group: most_popular  user: foodzie 
group: most_popular  user: vanessahudgens 
group: most_popular  user: paniexx_shop 
group: most_popular  user: starbucks 
group: photographers  user: macenzo 

4. categories: ['travel', 'foodies'], vtype: fc7
most_sim_users : ['foofighters' 'starbucks' 'lakers' 'vanessahudgens' 'laudyacynthiabella'
 'champagnepapi' 'macenzo' 'onedirection' 'shakira' 'rontez']
group: most_popular  user: foofighters 
group: most_popular  user: starbucks 
group: most_popular  user: lakers 
group: most_popular  user: vanessahudgens 
group: most_popular  user: laudyacynthiabella 
group: most_popular  user: champagnepapi 
group: photographers  user: macenzo 
group: most_popular  user: onedirection 
group: most_popular  user: shakira 
group: models  user: rontez 


5. categories: ['travel', 'foodies'], vtype: fc7
most_sim_users : ['vanessahudgens' 'starbucks' 'buzzfeedfood' 'onedirection'
 'elnuevodiariord' 'macenzo' 'paniexx_shop' 'kicks4sale' 'alexstrohl'
 'zachking']
group: most_popular  user: vanessahudgens 
group: most_popular  user: starbucks 
group: foodies  user: buzzfeedfood 
group: most_popular  user: onedirection 
group: most_popular  user: elnuevodiariord 
group: photographers  user: macenzo 
group: most_popular  user: paniexx_shop 
group: most_popular  user: kicks4sale 
group: travel  user: alexstrohl 
group: most_popular  user: zachking 



Photographers vs travel?

1. categories: ['photographers', 'travel'], vtype: fc7
most_sim_users : ['alexandracooks' 'onedirection' 'imchasingdreamz' 'japhetweeks'
 'tru_chadd' 'giggstage' 'serenawilliams' 'food52' 'jeffonline' 'opry']
group: foodies  user: alexandracooks 
group: most_popular  user: onedirection 
group: most_popular  user: imchasingdreamz 
group: travel  user: japhetweeks 
group: most_popular  user: tru_chadd 
group: most_popular  user: giggstage 
group: most_popular  user: serenawilliams 
group: foodies  user: food52 
group: photographers  user: jeffonline 
group: most_popular  user: opry 

2. categories: ['photographers', 'travel'], vtype: fc7
most_sim_users : ['japhetweeks' 'npr' 'alexandracooks' 'onedirection' 'ivmikspb' 'food52'
 'treyratcliff' 'imchasingdreamz' 'wideeyedlegless' 'bythebrush']
group: travel  user: japhetweeks 
group: most_popular  user: npr 
group: foodies  user: alexandracooks 
group: most_popular  user: onedirection 
group: most_popular  user: ivmikspb 
group: foodies  user: food52 
group: travel  user: treyratcliff 
group: most_popular  user: imchasingdreamz 
group: photographers  user: wideeyedlegless 
group: photographers  user: bythebrush 

3. categories: ['photographers', 'travel'], vtype: fc7
most_sim_users : ['addzim' 'travelnoire' 'dvl' 'imchasingdreamz' 'vanessahudgens'
 'whiskey_theaussie' 'thegrammys' 'elnuevodiariord' 'onedirection'
 'new_fork_city']
group: foodies  user: addzim 
group: travel  user: travelnoire 
group: photographers  user: dvl 
group: most_popular  user: imchasingdreamz 
group: most_popular  user: vanessahudgens 
group: dogs  user: whiskey_theaussie 
group: most_popular  user: thegrammys 
group: most_popular  user: elnuevodiariord 
group: most_popular  user: onedirection 

4. categories: ['photographers', 'travel'], vtype: fc7
most_sim_users : ['treyratcliff' 'addzim' 'travelnoire' 'katyperry' 'ivmikspb'
 'paigehathaway' 'dvl' 'mayrilyn' 'elnuevodiariord' 'kicks4sale']
group: travel  user: treyratcliff 
group: foodies  user: addzim 
group: travel  user: travelnoire 
group: most_popular  user: katyperry 
group: most_popular  user: ivmikspb 
group: models  user: paigehathaway 
group: photographers  user: dvl 
group: cats  user: mayrilyn 
group: most_popular  user: elnuevodiariord 
group: most_popular  user: kicks4sale

5. categories: ['photographers', 'travel'], vtype: fc7
most_sim_users : ['jeffonline' 'treyratcliff' 'maluma' 'asos' 'japhetweeks' 'alukoyanov'
 'danielvanderdeen' 'alexandracooks' 'mayrilyn' 'eyemediaa']
group: photographers  user: jeffonline 
group: travel  user: treyratcliff 
group: most_popular  user: maluma 
group: travel  user: japhetweeks 
group: most_popular  user: alukoyanov 
group: models  user: danielvanderdeen 
group: foodies  user: alexandracooks 
group: cats  user: mayrilyn 
group: most_popular  user: eyemediaa 
