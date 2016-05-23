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
top score: 0.757042592684     top user: goemon16
top score: 0.792841070467     top user: goemon16
top score: 0.588241629436     top user: goemon16
top score: 0.907931003747     top user: goemon16
top score: 0.877619998522     top user: goemon16
top score: 0.663357593991     top user: goemon16
top score: 0.855900043374     top user: goemon16
top score: 0.831652631221     top user: goemon16
top score: 0.666199871153     top user: goemon16
top score: 0.801372130874     top user: goemon16
top score: 0.655317643676     top user: goemon16
top score: 0.561658842565     top user: goemon16
top score: 0.867856896792     top user: goemon16
top score: 0.750911435571     top user: goemon16
top score: 0.823586620944     top user: goemon16
top score: 0.435700897935     top user: goemon16
top score: 0.593144601852     top user: goemon16
top score: 0.676288539015     top user: goemon16
top score: 0.558694450163     top user: goemon16
top score: 0.616382780699     top user: goemon16
top score: 0.44015081673     top user: goemon16
top score: 0.829754952793     top user: goemon16
top score: 0.592405789226     top user: goemon16
top score: 0.75631695323     top user: goemon16
top score: 0.704520402371     top user: goemon16
top score: 0.621882046505     top user: goemon16
top score: 0.732071002488     top user: goemon16
top score: 0.627656399263     top user: goemon16
top score: 0.636508377818     top user: goemon16
top score: 0.769461747927     top user: goemon16
top score: 0.877548778015     top user: goemon16
top score: 0.8391141416     top user: goemon16
top score: 0.674530545748     top user: goemon16
top score: 0.755327470402     top user: goemon16
top score: 0.723913102145     top user: goemon16
top score: 0.654791560406     top user: lebackpacker
top score: 0.654539093025     top user: goemon16
top score: 0.842464297201     top user: goemon16
top score: 0.804676205097     top user: goemon16
top score: 0.852805483705     top user: goemon16
top score: 0.256254012527     top user: goemon16
top score: 0.683102487894     top user: goemon16
top score: 0.806625428855     top user: goemon16
top score: 0.817245480364     top user: goemon16
top score: 0.683276112299     top user: goemon16
top score: 0.430508807739     top user: instagramtop50
top score: 0.81345204056     top user: goemon16
top score: 0.727858269601     top user: goemon16
top score: 0.777695803091     top user: goemon16
top score: 0.620803809324     top user: goemon16
top score: 0.490082784161     top user: instagramtop50
top score: 0.800940192803     top user: goemon16
top score: 0.72390594974     top user: goemon16
top score: 0.718681797431     top user: goemon16
top score: 0.813405194882     top user: goemon16
top score: 0.789688273673     top user: goemon16
top score: 0.851766107988     top user: goemon16
top score: 0.5850003981     top user: goemon16
top score: 0.78905896875     top user: goemon16
top score: 0.807138487891     top user: goemon16
top score: 0.830399036485     top user: goemon16
top score: 0.787926215595     top user: goemon16
top score: 0.834718922986     top user: goemon16
top score: 0.76979986792     top user: goemon16
top score: 0.625281580377     top user: goemon16
top score: 0.805275625097     top user: goemon16
top score: 0.58574026306     top user: goemon16
top score: 0.709063221396     top user: goemon16
top score: 0.492332788616     top user: lebackpacker
top score: 0.545313339414     top user: goemon16
top score: 0.615723528952     top user: goemon16
top score: 0.710013748781     top user: goemon16
top score: 0.736662708482     top user: goemon16
top score: 0.554859803777     top user: goemon16
top score: 0.612707295094     top user: goemon16
top score: 0.844441474731     top user: goemon16
top score: 0.750916710684     top user: goemon16
top score: 0.785134194959     top user: goemon16
top score: 0.634798230281     top user: goemon16
top score: 0.726027049991     top user: goemon16
top score: 0.580081514723     top user: instagramtop50
top score: 0.742873310407     top user: goemon16
top score: 0.825933509996     top user: goemon16
top score: 0.758704530226     top user: goemon16
top score: 0.801382377802     top user: goemon16
top score: 0.774369063466     top user: goemon16
top score: 0.864807810394     top user: goemon16
top score: 0.848003062334     top user: goemon16
top score: 0.403769023086     top user: goemon16
top score: 0.586303457402     top user: goemon16
top score: 0.808995661891     top user: goemon16
top score: 0.785277928184     top user: goemon16
top score: 0.714485977052     top user: goemon16
top score: 0.671319608533     top user: goemon16
top score: 0.666188648637     top user: goemon16
top score: 0.821382608065     top user: goemon16
top score: 0.691075792693     top user: goemon16
top score: 0.802474145186     top user: goemon16
top score: 0.860397649576     top user: goemon16
top score: 0.515823019747     top user: lebackpacker
top score: 0.503448702979     top user: andrew_icant
top score: 0.73308961631     top user: andrew_icant
top score: 0.907876037025     top user: andrew_icant
top score: 0.899436072724     top user: andrew_icant
top score: 0.841244679692     top user: andrew_icant
top score: 0.891425876854     top user: andrew_icant
top score: 0.863822897465     top user: andrew_icant
top score: 0.872913120815     top user: andrew_icant
top score: 0.830842100855     top user: andrew_icant
top score: 0.80218636187     top user: andrew_icant
top score: 0.342113341487     top user: goemon16
top score: 0.890283312503     top user: andrew_icant
top score: 0.888155332518     top user: andrew_icant
top score: 0.794324026387     top user: andrew_icant
top score: 0.665730050763     top user: andrew_icant
top score: 0.654323742487     top user: andrew_icant
top score: 0.882748494937     top user: andrew_icant
top score: 0.558872773817     top user: andrew_icant
top score: 0.829049115176     top user: andrew_icant
top score: 0.878808627927     top user: andrew_icant
top score: 0.874361879895     top user: andrew_icant
top score: 0.65691572774     top user: andrew_icant
top score: 0.863545221348     top user: andrew_icant
top score: 0.914395874536     top user: andrew_icant
top score: 0.628929895027     top user: andrew_icant
top score: 0.86343967302     top user: andrew_icant
top score: 0.902648009099     top user: andrew_icant
top score: 0.884886119065     top user: andrew_icant
top score: 0.693915269675     top user: andrew_icant
top score: 0.870377157782     top user: andrew_icant
top score: 0.80182406728     top user: andrew_icant
top score: 0.88396707558     top user: andrew_icant
top score: 0.864522439908     top user: andrew_icant
top score: 0.878151679369     top user: andrew_icant
top score: 0.772909028075     top user: andrew_icant
top score: 0.857006508692     top user: andrew_icant
top score: 0.603254051894     top user: andrew_icant
top score: 0.834473421849     top user: andrew_icant
top score: 0.755139933205     top user: andrew_icant
top score: 0.742493231085     top user: andrew_icant
top score: 0.725674403727     top user: andrew_icant
top score: 0.87497764023     top user: andrew_icant
top score: 0.860360729487     top user: andrew_icant
top score: 0.879947177304     top user: andrew_icant
top score: 0.861687614665     top user: andrew_icant
top score: 0.622111218526     top user: andrew_icant
top score: 0.892212075128     top user: andrew_icant
top score: 0.924755977171     top user: andrew_icant
top score: 0.796796749395     top user: andrew_icant
top score: 0.401041403953     top user: andrew_icant
top score: 0.886113322877     top user: andrew_icant
top score: 0.912942319543     top user: andrew_icant
top score: 0.911144684157     top user: andrew_icant
top score: 0.923434120197     top user: andrew_icant
top score: 0.848731250762     top user: andrew_icant
top score: 0.749783163194     top user: andrew_icant
top score: 0.919177039434     top user: andrew_icant
top score: 0.7577411973     top user: andrew_icant
top score: 0.80931050547     top user: andrew_icant
top score: 0.78414157161     top user: andrew_icant
top score: 0.852855552286     top user: andrew_icant
top score: 0.758339974777     top user: andrew_icant
top score: 0.843873799784     top user: andrew_icant
top score: 0.861478049645     top user: andrew_icant
top score: 0.813341033489     top user: andrew_icant
top score: 0.682670156743     top user: andrew_icant
top score: 0.882616104595     top user: andrew_icant
top score: 0.825256603177     top user: andrew_icant
top score: 0.58028063557     top user: andrew_icant
top score: 0.880176113622     top user: andrew_icant
top score: 0.718644527194     top user: andrew_icant
top score: 0.395775501232     top user: goemon16
top score: 0.860464698569     top user: andrew_icant
top score: 0.857527692196     top user: andrew_icant
top score: 0.688865363292     top user: andrew_icant
top score: 0.881797028643     top user: andrew_icant
top score: 0.887903937975     top user: andrew_icant
top score: 0.925117228439     top user: andrew_icant
top score: 0.882597838423     top user: andrew_icant
top score: 0.906139292951     top user: andrew_icant
top score: 0.792475605073     top user: andrew_icant
top score: 0.860643714358     top user: andrew_icant
top score: 0.913003176075     top user: andrew_icant
top score: 0.899234734331     top user: andrew_icant
top score: 0.776786147055     top user: andrew_icant
top score: 0.826207067239     top user: andrew_icant
top score: 0.780913380291     top user: andrew_icant
top score: 0.715177383536     top user: andrew_icant
top score: 0.917333575049     top user: andrew_icant
top score: 0.586191100922     top user: andrew_icant
top score: 0.732342900704     top user: andrew_icant
top score: 0.835165578613     top user: andrew_icant
top score: 0.889423150562     top user: andrew_icant
top score: 0.785852435254     top user: andrew_icant
top score: 0.90195428714     top user: andrew_icant
top score: 0.919794811636     top user: andrew_icant
top score: 0.805288188226     top user: andrew_icant
top score: 0.90592937725     top user: andrew_icant
top score: 0.899139079322     top user: andrew_icant
top score: 0.777114047581     top user: andrew_icant
top score: 0.773579749591     top user: instagramtop50
top score: 0.389179288656     top user: instagramtop50
top score: 0.87675938301     top user: instagramtop50
top score: 0.838766399213     top user: instagramtop50
top score: 0.889664229148     top user: instagramtop50
top score: 0.845576942727     top user: instagramtop50
top score: 0.861352126676     top user: instagramtop50
top score: 0.906712851865     top user: instagramtop50
top score: 0.879876423919     top user: instagramtop50
top score: 0.743655813546     top user: instagramtop50
top score: 0.700939004066     top user: instagramtop50
top score: 0.865228067103     top user: instagramtop50
top score: 0.46894532851     top user: instagramtop50
top score: 0.801804563673     top user: instagramtop50
top score: 0.446947102215     top user: lebackpacker
top score: 0.523096349882     top user: andrew_icant
top score: 0.760355796767     top user: instagramtop50
top score: 0.547883500003     top user: instagramtop50
top score: 0.84506531768     top user: instagramtop50
top score: 0.825095824003     top user: instagramtop50
top score: 0.728760497171     top user: instagramtop50
top score: 0.881678588857     top user: instagramtop50
top score: 0.808462549861     top user: instagramtop50
top score: 0.483788761852     top user: lebackpacker
top score: 0.765569157537     top user: instagramtop50
top score: 0.68001543425     top user: instagramtop50
top score: 0.806692484089     top user: instagramtop50
top score: 0.736183196834     top user: instagramtop50
top score: 0.511322031282     top user: instagramtop50
top score: 0.87793753207     top user: instagramtop50
top score: 0.498196261548     top user: instagramtop50
top score: 0.692631572141     top user: instagramtop50
top score: 0.86340486475     top user: instagramtop50
top score: 0.72675833581     top user: instagramtop50
top score: 0.550101260559     top user: instagramtop50
top score: 0.801561167239     top user: instagramtop50
top score: 0.788561125935     top user: instagramtop50
top score: 0.687417333865     top user: instagramtop50
top score: 0.838668887553     top user: instagramtop50
top score: 0.850705653282     top user: instagramtop50
top score: 0.544006891452     top user: instagramtop50
top score: 0.874539852251     top user: instagramtop50
top score: 0.848885320422     top user: instagramtop50
top score: 0.868404618281     top user: instagramtop50
top score: 0.713661992834     top user: instagramtop50
top score: 0.705964836076     top user: instagramtop50
top score: 0.766951525141     top user: instagramtop50
top score: 0.845907816428     top user: instagramtop50
top score: 0.869180835972     top user: instagramtop50
top score: 0.563481740892     top user: instagramtop50
top score: 0.869138253609     top user: instagramtop50
top score: 0.671470958031     top user: instagramtop50
top score: 0.794709361009     top user: instagramtop50
top score: 0.727429273041     top user: instagramtop50
top score: 0.861620009098     top user: instagramtop50
top score: 0.764665431887     top user: instagramtop50
top score: 0.871365732637     top user: instagramtop50
top score: 0.686797155401     top user: andrew_icant
top score: 0.730284259549     top user: instagramtop50
top score: 0.644583763693     top user: instagramtop50
top score: 0.844195475489     top user: instagramtop50
top score: 0.782480089153     top user: instagramtop50
top score: 0.718501841526     top user: instagramtop50
top score: 0.797457450922     top user: instagramtop50
top score: 0.823924155978     top user: instagramtop50
top score: 0.770755463428     top user: instagramtop50
top score: 0.451213631484     top user: instagramtop50
top score: 0.655148345909     top user: instagramtop50
top score: 0.812391627222     top user: instagramtop50
top score: 0.835284523304     top user: instagramtop50
top score: 0.833775266953     top user: instagramtop50
top score: 0.740567496401     top user: instagramtop50
top score: 0.815005480594     top user: instagramtop50
top score: 0.879070007667     top user: instagramtop50
top score: 0.732527554575     top user: instagramtop50
top score: 0.70861031972     top user: instagramtop50
top score: 0.798528622882     top user: instagramtop50
top score: 0.906248584926     top user: instagramtop50
top score: 0.274831640853     top user: goemon16
top score: 0.651428633133     top user: instagramtop50
top score: 0.492409729154     top user: instagramtop50
top score: 0.363387012863     top user: lebackpacker
top score: 0.570597440249     top user: lebackpacker
top score: 0.46152792164     top user: instagramtop50
top score: 0.684713039626     top user: instagramtop50
top score: 0.876659980042     top user: instagramtop50
top score: 0.711057206441     top user: instagramtop50
top score: 0.751958458665     top user: instagramtop50
top score: 0.802461753705     top user: instagramtop50
top score: 0.466877911449     top user: goemon16
top score: 0.719207815023     top user: instagramtop50
top score: 0.917476176387     top user: instagramtop50
top score: 0.719988964322     top user: instagramtop50
top score: 0.858615518979     top user: instagramtop50
top score: 0.671104467236     top user: instagramtop50
top score: 0.520725780661     top user: andrew_icant
top score: 0.861468626157     top user: instagramtop50
top score: 0.839214577308     top user: instagramtop50
top score: 0.693796397478     top user: instagramtop50
top score: 0.872245199622     top user: lebackpacker
top score: 0.729699072748     top user: lebackpacker
top score: 0.756073481415     top user: lebackpacker
top score: 0.617417950149     top user: lebackpacker
top score: 0.882554122535     top user: lebackpacker
top score: 0.756404138886     top user: lebackpacker
top score: 0.782718531993     top user: lebackpacker
top score: 0.821708429192     top user: lebackpacker
top score: 0.847041449204     top user: lebackpacker
top score: 0.679001163229     top user: lebackpacker
top score: 0.834193668055     top user: lebackpacker
top score: 0.724810104142     top user: lebackpacker
top score: 0.760504420039     top user: lebackpacker
top score: 0.797149248091     top user: lebackpacker
top score: 0.512982750947     top user: lebackpacker
top score: 0.691234357542     top user: lebackpacker
top score: 0.833222338378     top user: lebackpacker
top score: 0.747863724173     top user: lebackpacker
top score: 0.45346667754     top user: goemon16
top score: 0.605657900735     top user: lebackpacker
top score: 0.407936264557     top user: lebackpacker
top score: 0.651847439149     top user: lebackpacker
top score: 0.815162818832     top user: lebackpacker
top score: 0.570100627408     top user: lebackpacker
top score: 0.69606814266     top user: lebackpacker
top score: 0.635332388977     top user: lebackpacker
top score: 0.888033382768     top user: lebackpacker
top score: 0.461460826881     top user: lebackpacker
top score: 0.64677555358     top user: lebackpacker
top score: 0.757917778028     top user: lebackpacker
top score: 0.748371410957     top user: lebackpacker
top score: 0.707096851783     top user: lebackpacker
top score: 0.808193954741     top user: lebackpacker
top score: 0.76629428073     top user: lebackpacker
top score: 0.442530384012     top user: lebackpacker
top score: 0.730085804811     top user: lebackpacker
top score: 0.585328734039     top user: lebackpacker
top score: 0.580292445903     top user: lebackpacker
top score: 0.809742679721     top user: lebackpacker
top score: 0.81934762018     top user: lebackpacker
top score: 0.872969170765     top user: lebackpacker
top score: 0.734397655022     top user: lebackpacker
top score: 0.810995162693     top user: lebackpacker
top score: 0.789369052162     top user: lebackpacker
top score: 0.781424509137     top user: lebackpacker
top score: 0.776255607582     top user: lebackpacker
top score: 0.64962142343     top user: lebackpacker
top score: 0.820466041468     top user: lebackpacker
top score: 0.268655152902     top user: goemon16
top score: 0.686728814834     top user: instagramtop50
top score: 0.770913199659     top user: lebackpacker
top score: 0.763363868228     top user: lebackpacker
top score: 0.721982335411     top user: lebackpacker
top score: 0.526651279328     top user: lebackpacker
top score: 0.661478925428     top user: lebackpacker
top score: 0.811295893094     top user: lebackpacker
top score: 0.670526300041     top user: lebackpacker
top score: 0.706406665488     top user: lebackpacker
top score: 0.600212589391     top user: lebackpacker
top score: 0.807946946373     top user: lebackpacker
top score: 0.547529820554     top user: instagramtop50
top score: 0.716939245804     top user: lebackpacker
top score: 0.741033390669     top user: lebackpacker
top score: 0.844085990507     top user: lebackpacker
top score: 0.749592230362     top user: lebackpacker
top score: 0.725474485728     top user: lebackpacker
top score: 0.816788146499     top user: lebackpacker
top score: 0.732747723007     top user: lebackpacker
top score: 0.697146403464     top user: lebackpacker
top score: 0.802817315503     top user: lebackpacker
top score: 0.713116968264     top user: lebackpacker
top score: 0.706108984673     top user: lebackpacker
top score: 0.861735755202     top user: lebackpacker
top score: 0.862079904599     top user: lebackpacker
top score: 0.649443983472     top user: lebackpacker
top score: 0.593396892915     top user: lebackpacker
top score: 0.64937560848     top user: lebackpacker
top score: 0.773915294587     top user: lebackpacker
top score: 0.912519474029     top user: lebackpacker
top score: 0.825289487543     top user: lebackpacker
top score: 0.427398478724     top user: instagramtop50
top score: 0.417418925538     top user: lebackpacker
top score: 0.787998894112     top user: lebackpacker
top score: 0.560886651289     top user: lebackpacker
top score: 0.590155903895     top user: lebackpacker
top score: 0.658226918799     top user: lebackpacker
top score: 0.769884910345     top user: lebackpacker
top score: 0.837084997107     top user: lebackpacker
top score: 0.845724461222     top user: lebackpacker
top score: 0.833543518631     top user: lebackpacker
top score: 0.580584459155     top user: lebackpacker
top score: 0.803467782619     top user: lebackpacker
top score: 0.806201629667     top user: lebackpacker
top score: 0.715625232223     top user: lebackpacker
top score: 0.612332526083     top user: lebackpacker
top score: 0.46200028016     top user: instagramtop50
top score: 0.528136591037     top user: lebackpacker
top score: 0.753126663885     top user: lebackpacker
