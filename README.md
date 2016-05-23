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


Models vs photographers

1. categories: ['models', 'photographers'], vtype: fc7
most_sim_users : ['kirstenalana' 'princessyahrini' 'channingtatum' 'gucci' 'photojojo'
 'claudjdean' 'zendaya' 'warbyparker' 'samhorine' 'mattblack_blackmatt']
group: photographers  user: kirstenalana
group: most_popular  user: princessyahrini
group: most_popular  user: channingtatum
group: most_popular  user: gucci
group: most_popular  user: photojojo
group: models  user: claudjdean
group: most_popular  user: zendaya
group: most_popular  user: warbyparker
group: photographers  user: samhorine
group: photographers  user: mattblack_blackmatt

2. categories: ['models', 'photographers'], vtype: fc7
most_sim_users : ['drizzleanddip' 'convergence' 'gwneff' 'pozzialessio' 'sacramentokings'
 'thesorensen' 'theaccessoryqueen_mrsdds' 'toppeopleworld' 'mfj57'
 'gothiphop']
group: most_popular  user: convergence
group: models  user: gwneff
group: models  user: pozzialessio
group: most_popular  user: sacramentokings
group: models  user: thesorensen
group: most_popular  user: theaccessoryqueen_mrsdds
group: most_popular  user: toppeopleworld
group: most_popular  user: mfj57
group: most_popular  user: gothiphop

3. categories: ['models', 'photographers'], vtype: fc7
most_sim_users : ['gothiphop' 'iamzlatanibrahimovic' 'miamiheat' 'milesmcmillan' 'jaybling'
 'maggie_rawlins' 'realmadrid' 'gucci' 'theroxy' 'burkhartsokc']
group: most_popular  user: gothiphop
group: most_popular  user: iamzlatanibrahimovic
group: most_popular  user: miamiheat
group: models  user: milesmcmillan
group: most_popular  user: jaybling
group: models  user: maggie_rawlins
group: most_popular  user: realmadrid
group: most_popular  user: gucci
group: most_popular  user: theroxy
group: photographers  user: burkhartsokc

4. categories: ['models', 'photographers'], vtype: fc7
most_sim_users : ['kaka' 'thesorensen' 'riverviiperi' 'rainyseasonshop' 'mexicotravel'
 'evys_mom' 'jesse_burke' 'thekatvond' 'realfoodz' 'convergence']
group: most_popular  user: kaka
group: models  user: thesorensen
group: models  user: riverviiperi
group: most_popular  user: rainyseasonshop
group: most_popular  user: mexicotravel
group: dogs  user: evys_mom
group: photographers  user: jesse_burke
group: most_popular  user: thekatvond
group: most_popular  user: convergence

5. categories: ['models', 'photographers'], vtype: fc7
most_sim_users : ['halno' 'foooodieee' 'gothiphop' 'donalskehan' 'samariaregalado'
 'ediblebrooklyn' 'popeater' 'erinandrews' 'amanda.leefans' 'skinart_mag']
group: photographers  user: halno
group: most_popular  user: gothiphop
group: models  user: samariaregalado
group: foodies  user: ediblebrooklyn
group: most_popular  user: popeater
group: most_popular  user: erinandrews
group: models  user: amanda.leefans
group: most_popular  user: skinart_mag


Most popular vs models?

1. categories: ['most_popular', 'models'], vtype: fc7
most_sim_users : ['alexandracooks' 'beybleedblue' 'giggstage' 'wouter38' 'mtv'
 'deanthebasset' 'adidasoriginals' 'seanopry55' 'spoonforkbacon'
 'gavinkaysen']
group: foodies  user: alexandracooks
group: most_popular  user: beybleedblue
group: most_popular  user: giggstage
group: most_popular  user: wouter38
group: most_popular  user: mtv
group: dogs  user: deanthebasset
group: most_popular  user: adidasoriginals
group: models  user: seanopry55
group: foodies  user: spoonforkbacon
group: foodies  user: gavinkaysen

2. categories: ['most_popular', 'models'], vtype: fc7
most_sim_users : ['wouter38' 'kimkardashian' 'markhoppus' 'mistercap' 'cnnireport'
 'bythebrush' 'exopassion' 'alexandracooks' 'adidas' 'breakingnews']
group: most_popular  user: wouter38
group: most_popular  user: kimkardashian
group: most_popular  user: markhoppus
group: most_popular  user: mistercap
group: most_popular  user: cnnireport
group: photographers  user: bythebrush
group: most_popular  user: exopassion
group: foodies  user: alexandracooks
group: most_popular  user: adidas
group: travel  user: breakingnews

3. categories: ['most_popular', 'models'], vtype: fc7
most_sim_users : ['camerondallas' 'dogumantry' 'newtgingrich' 'feedprojects'
 'ryannealcordwell' 'claudiaalende' 'stressedouthams' 'mistercap' 'janske'
 'lil_rufio']
group: most_popular  user: camerondallas
group: dogs  user: dogumantry
group: most_popular  user: newtgingrich
group: most_popular  user: feedprojects
group: photographers  user: ryannealcordwell
group: most_popular  user: stressedouthams
group: most_popular  user: mistercap
group: photographers  user: janske
group: dogs  user: lil_rufio

4. categories: ['most_popular', 'models'], vtype: fc7
most_sim_users : ['katyperry' 'cnnireport' 'chrisburkard' 'theultimateclub' 'luissuarez9'
 'inestrocchia' 'redbull' 'gess8' 'nbcnews' 'skylerandsabrina']
group: most_popular  user: katyperry
group: most_popular  user: cnnireport
group: travel  user: chrisburkard
group: most_popular  user: theultimateclub
group: most_popular  user: luissuarez9
group: models  user: inestrocchia
group: most_popular  user: redbull
group: travel  user: gess8
group: most_popular  user: nbcnews
group: dogs  user: skylerandsabrina

5. categories: ['most_popular', 'models'], vtype: fc7
most_sim_users : ['emil_valentino' 'mtv' 'misvincent' 'deanthebasset' 'adidasoriginals'
 'utosh' 'caiocastro' 'toms' 'victoriassecret' 'karaswisher']
group: most_popular  user: emil_valentino
group: most_popular  user: mtv
group: photographers  user: misvincent
group: dogs  user: deanthebasset
group: most_popular  user: adidasoriginals
group: most_popular  user: caiocastro
group: most_popular  user: toms
group: most_popular  user: victoriassecret
group: most_popular  user: karaswisher


tfidf pilot testing:

sample_users = ['goemon16', 'andrew_icant', 'instagramtop50', 'lebackpacker']
sample 10 images per user
each user is represented by the sum of their images (not mean)
Results:
goemon16 img 0 most similar to [('goemon16', 0.79821803788168744), ('instagramtop50', 0.42362810184121885), ('andrew_icant', 0.30798728694654998), ('lebackpacker', 0.12842522912844559)]
goemon16 img 1 most similar to [('lebackpacker', 0.27766070556393213), ('instagramtop50', 0.23567860072892957), ('goemon16', 0.22487687737429632), ('andrew_icant', 0.20028834152913827)]
goemon16 img 2 most similar to [('goemon16', 0.67549429932511429), ('instagramtop50', 0.48121889845332827), ('andrew_icant', 0.28204628368254209), ('lebackpacker', 0.14431713846102492)]
goemon16 img 3 most similar to [('goemon16', 0.68651468384687819), ('instagramtop50', 0.53475369308727549), ('andrew_icant', 0.20553761795980197), ('lebackpacker', 0.097344156479695576)]
goemon16 img 4 most similar to [('goemon16', 0.81212751187837651), ('instagramtop50', 0.49296244829638097), ('andrew_icant', 0.30405060236052067), ('lebackpacker', 0.1553832694800879)]
goemon16 img 5 most similar to [('goemon16', 0.74101622014140345), ('instagramtop50', 0.44472023389851773), ('andrew_icant', 0.22935075777542752), ('lebackpacker', 0.12492626852460227)]
goemon16 img 6 most similar to [('goemon16', 0.76725920059267627), ('instagramtop50', 0.53600980171858736), ('andrew_icant', 0.30335136220312375), ('lebackpacker', 0.20829284795203643)]
goemon16 img 7 most similar to [('goemon16', 0.81694292370710087), ('instagramtop50', 0.57569498276968101), ('andrew_icant', 0.36326331196892792), ('lebackpacker', 0.19460394893072577)]
goemon16 img 8 most similar to [('goemon16', 0.50529099816574918), ('instagramtop50', 0.41789844999213349), ('lebackpacker', 0.17759087134620621), ('andrew_icant', 0.1738816758334587)]
goemon16 img 9 most similar to [('goemon16', 0.67077796338402107), ('andrew_icant', 0.42579194259154896), ('instagramtop50', 0.33911862166869616), ('lebackpacker', 0.14861808926780587)]
andrew_icant img 0 most similar to [('andrew_icant', 0.89649573377959579), ('instagramtop50', 0.3632492358565147), ('goemon16', 0.28866942424193753), ('lebackpacker', 0.17609203794123626)]
andrew_icant img 1 most similar to [('andrew_icant', 0.85388645174046551), ('goemon16', 0.2287599897065633), ('instagramtop50', 0.22793891501897856), ('lebackpacker', 0.18418129981829387)]
andrew_icant img 2 most similar to [('andrew_icant', 0.87812249376385099), ('goemon16', 0.24174461896713587), ('instagramtop50', 0.2263863287797088), ('lebackpacker', 0.14836482736313714)]
andrew_icant img 3 most similar to [('andrew_icant', 0.76885345309808006), ('goemon16', 0.20630656052335242), ('lebackpacker', 0.16986353917591979), ('instagramtop50', 0.15015998515325005)]
andrew_icant img 4 most similar to [('andrew_icant', 0.78622180773425643), ('goemon16', 0.37743193651535228), ('instagramtop50', 0.3423017629781302), ('lebackpacker', 0.13644023798105112)]
andrew_icant img 5 most similar to [('andrew_icant', 0.89315398346345221), ('instagramtop50', 0.31044442071391959), ('goemon16', 0.30602375002011156), ('lebackpacker', 0.15739799069729718)]
andrew_icant img 6 most similar to [('andrew_icant', 0.83139797967318307), ('goemon16', 0.46168188631874091), ('instagramtop50', 0.43585509184512983), ('lebackpacker', 0.16148233050272406)]
andrew_icant img 7 most similar to [('andrew_icant', 0.94692571855953145), ('goemon16', 0.28014784536080573), ('instagramtop50', 0.25492819367584169), ('lebackpacker', 0.16540092406460422)]
andrew_icant img 8 most similar to [('andrew_icant', 0.88959244182411246), ('goemon16', 0.33228668775953812), ('instagramtop50', 0.27494470773868535), ('lebackpacker', 0.14190688924651404)]
andrew_icant img 9 most similar to [('andrew_icant', 0.87748567989658222), ('goemon16', 0.35705408756789037), ('instagramtop50', 0.31130645204136198), ('lebackpacker', 0.17122328790201929)]
instagramtop50 img 0 most similar to [('instagramtop50', 0.80825913405667915), ('goemon16', 0.48084047762939591), ('lebackpacker', 0.2335282887978718), ('andrew_icant', 0.18057531714115879)]
instagramtop50 img 1 most similar to [('instagramtop50', 0.84870765748866883), ('goemon16', 0.59416135764205791), ('andrew_icant', 0.24853496140978054), ('lebackpacker', 0.22413194168516598)]
instagramtop50 img 2 most similar to [('instagramtop50', 0.87551788912731865), ('goemon16', 0.64004822043293064), ('andrew_icant', 0.24953449267806296), ('lebackpacker', 0.17128072686036469)]
instagramtop50 img 3 most similar to [('instagramtop50', 0.81530434932972584), ('goemon16', 0.67875274697032872), ('andrew_icant', 0.42946994707251118), ('lebackpacker', 0.15365175905229242)]
instagramtop50 img 4 most similar to [('instagramtop50', 0.67532254688500692), ('goemon16', 0.34700313050261644), ('lebackpacker', 0.26764538306628316), ('andrew_icant', 0.22282355366892076)]
instagramtop50 img 5 most similar to [('instagramtop50', 0.71277361726446553), ('goemon16', 0.68433421152950091), ('andrew_icant', 0.30066708133054681), ('lebackpacker', 0.14105662552784198)]
instagramtop50 img 6 most similar to [('instagramtop50', 0.76409529431393253), ('goemon16', 0.5067533251644164), ('andrew_icant', 0.4580368849687852), ('lebackpacker', 0.20175036646482303)]
instagramtop50 img 7 most similar to [('lebackpacker', 0.58034911194819616), ('instagramtop50', 0.50102518535892115), ('andrew_icant', 0.32723926212095511), ('goemon16', 0.24266258246953987)]
instagramtop50 img 8 most similar to [('instagramtop50', 0.77708505891127155), ('goemon16', 0.61015499409826945), ('lebackpacker', 0.27276697706453967), ('andrew_icant', 0.25976220780115927)]
lebackpacker img 0 most similar to [('lebackpacker', 0.79684408479612689), ('instagramtop50', 0.15544487063824045), ('andrew_icant', 0.10778324971189435), ('goemon16', 0.086748281715565478)]
lebackpacker img 1 most similar to [('lebackpacker', 0.85474127844849856), ('instagramtop50', 0.26034085912488425), ('goemon16', 0.14691026845891092), ('andrew_icant', 0.10796402402851654)]
lebackpacker img 2 most similar to [('lebackpacker', 0.63720896968093699), ('instagramtop50', 0.27707472578674086), ('goemon16', 0.24731798451573581), ('andrew_icant', 0.12542976559345206)]
lebackpacker img 3 most similar to [('lebackpacker', 0.77815385221413857), ('andrew_icant', 0.24316681953049857), ('instagramtop50', 0.11117412702906772), ('goemon16', 0.078238668568577668)]
lebackpacker img 4 most similar to [('lebackpacker', 0.56270412433354411), ('instagramtop50', 0.26177220912955479), ('goemon16', 0.18227935257246097), ('andrew_icant', 0.13354925510877877)]
lebackpacker img 5 most similar to [('lebackpacker', 0.58475397308917842), ('andrew_icant', 0.26616169965383901), ('goemon16', 0.2514512336353657), ('instagramtop50', 0.16450568113575947)]
lebackpacker img 6 most similar to [('lebackpacker', 0.45158877295714794), ('andrew_icant', 0.29746264889982743), ('instagramtop50', 0.24046763870977195), ('goemon16', 0.22235623147371936)]
lebackpacker img 7 most similar to [('lebackpacker', 0.67776019369419438), ('instagramtop50', 0.14051011099022195), ('andrew_icant', 0.11413172302658038), ('goemon16', 0.11297099281467893)]
lebackpacker img 8 most similar to [('lebackpacker', 0.85482110589711791), ('instagramtop50', 0.11958711032035657), ('andrew_icant', 0.11396274035629636), ('goemon16', 0.075715025079724205)]
lebackpacker img 9 most similar to [('lebackpacker', 0.60893467490066966), ('instagramtop50', 0.26429434737530771), ('goemon16', 0.16831695532638749), ('andrew_icant', 0.13720210295896909)]


tfidf pilot testing #2:
sample_users = ['goemon16', 'andrew_icant', 'instagramtop50', 'lebackpacker']
sample 100 images per user
each user is represented by the sum of their images (not mean)
Results:
