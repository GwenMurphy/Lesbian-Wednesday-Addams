import random

gaytired = random.randint(1,200)/10

minutes_2lz = '%02d' % (random.randint(1,60),)

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### The arrays below help to randomise the strings in the #####
##### master array (tweetlist) located at the bottom of     #####
##### this Python file. They are also referenced by other   #####
##### arrays, hence their location at the top of the file.  #####
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

as_useful_as_a = [
    'a catflap on a submarine.',
    'a chocolate teapot in the equatorial regions of Venus.',
    'a glass hammer.',
    'handles on a snowball.',
    'ejection seats on a helicopter.',
    'a concrete parachute.',
    'an ashtray on a bike.',
    'red lights in GTA.',
    'a Windows Vista installation disk.',
    'nipples on Batman\'s suit.',
    'an inflatable dartboard.',
    'a fart in a spacesuit.'
]

MCU_geniuses = [
    'Tony Stark', ## Genius Billionaire Playboy Philanthropist
    'Shuri', ## Wakanda's ultimate authority on meme culture must be protected at all costs.
    'Riri Williams' ## Ironheart.
]

virus_list = [
    'adware',
    'malware',
    'ransomware',
    'spyware'
]

##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### Imagine, if you will, an ambitious attempt at so much #####
##### fanfiction that it warrants its own alternate         #####
##### universe. This bit contains references to it and to   #####
##### understand the references, you need to be me.         #####
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####

dreamscen_pLR_facts_AceOfSpades = [
    'and she\'s also a Starfleet Admiral.',
    f'and in terms of intellect she\'s basically Star Trek\'s answer to {random.choice(MCU_geniuses)}.',
    'and thanks to her friend\'s training, she defeated eight Zhat Vash agents singlehandedly.',
    'and she\'s friends with the reigning monarchs of at least four worlds, including Xahea.',
    'and she loves shawarma.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and she\'s a goth cinnamon roll.',
    'and she\'s a professional poker player, having won the bracelet 9 times.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_AceOfHearts = [
    'and she\'s the Number 1 enemy of the Tal Shiar.',
    'and she plans on one day becoming Proconsul of the Romulan Republic.',
    'and her wife\'s the Romulan doppelgänger of Kristen Stewart.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and she\'s a goth cinnamon roll.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_AceOfDiamonds = [
    'and Tilly is her soulmate separated by time.',
    'and a friend of hers guessed that she\'d run for President of the United Federation of Planets.',
    'and she can\'t go a fortnight without the Ace of Spades sneaking in a Kakegurui reference.',
    'and she\'s also a Starfleet Admiral',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_AceOfClubs = [
    'and she\'s a sailor scout and a Dahar Master.',
    'and she has the eternal gratitude of House Martok.',
    'and she singlehandedly defeated Molor and his Fek\'Ihri hordes.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and she\'s got the hots for Adet\'pa and L\'Rell.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_QueenOfSpades = [
    'and she\'s the Xahean answer to John Wick.',
    'and she has been described as a walking Final Destination film.',
    'and she once defeated seven Klingons with a pencil defending someone who she sees as a sister.',
    'and she\'s Samoan on her dad\'s side, Xahean on her mum\'s.',
    'and she\'s a sister figure to the Ace of Spades.',
    'and she loved cucumber sandwiches.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_MonarchOfHearts = [
    'and they\'re an administrative powerhouse on a scale that fair boggles the mind.',
    'and they loved khachapuri so much they decided to learn Georgian.',
    'and like the other Royals, they\'re fluent in 19 languages.'
]

dreamscen_pLR_facts_QueenOfDiamonds = [
    'and rumour has it she stopped a group of traitorous Klingons with a single stare.',
    'and alongside her sisters (as well as alone), she\'s a force to be reckoned with.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_QueenOfClubs = [
    'and she\'s Vulcan\'s expert on radiating mom energy.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_JackOfSpades = [
    'and alongside her sisters (as well as alone), she\'s a force to be reckoned with.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_JackOfHearts = [
    'and alongside her sisters (as well as alone), she\'s a force to be reckoned with.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_JackOfDiamonds = [
    'she\'s the must successful Andorian DJ of all time.',
    'and she loved khachapuri so much she decided to learn Georgian.'
    'and she\'s got at least half a dozen albums gone platinum.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_pLR_facts_JackOfClubs = [
    'and she\'s got the ability to keep the Klingon chancellor on their toes.',
    'and she loved khachapuri so much she decided to learn Georgian.',
    'and like the other Royals, she\'s fluent in 19 languages.'
]

dreamscen_prompts_LesRoyales = [
    f'Chloë Grace Moretz is the Ace of Spades {random.choice(dreamscen_pLR_facts_AceOfSpades)}',
    f'Brie Larson is the Ace of Hearts {random.choice(dreamscen_pLR_facts_AceOfHearts)}',
    f'Minami Hamabe is the Ace of Diamonds {random.choice(dreamscen_pLR_facts_AceOfDiamonds)}',
    f'Elsa Pataky is the Ace of Clubs {random.choice(dreamscen_pLR_facts_AceOfClubs)}',
    f'Frankie Adams is the Queen of Spades {random.choice(dreamscen_pLR_facts_QueenOfSpades)}',
    f'Asia Kate Dillon is the Monarch of Hearts {random.choice(dreamscen_pLR_facts_MonarchOfHearts)}',
    f'Su-Metal is the Queen of Diamonds {random.choice(dreamscen_pLR_facts_QueenOfDiamonds)}',
    f'Awkwafina is the Queen of Clubs {random.choice(dreamscen_pLR_facts_QueenOfClubs)}',
    f'Yui-Metal is the Jack of Spades {random.choice(dreamscen_pLR_facts_JackOfSpades)}',
    f'Moa-Metal is the Jack of Hearts {random.choice(dreamscen_pLR_facts_JackOfHearts)}',
    f'Cara Delevingne is the Jack of Diamonds {random.choice(dreamscen_pLR_facts_JackOfDiamonds)}',
    f'Lena Headey is the Jack of Clubs {random.choice(dreamscen_pLR_facts_JackOfClubs)}'
]


##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####
##### The arrays below help to randomise the strings in the #####
##### master array (tweetlist) located at the bottom of     #####
##### this Python file.                                     #####
##### ##### ##### ##### ##### ##### ##### ##### ##### ##### #####



bad_os = [
    'Windows ME',
    'Windows Vista'
]

bad_writing_obsrv = [
    'Shit looks like Imhotep\'s homework',
    'Shit looks like seismographic readings.',
    'Shit makes a doctor\'s handwriting look legible.',
    'Shit looks like an attempt at calligraphy done in the back of a moving rally car.'
]

cch_insults = [
    'were the Human equivalent of participation awards.',
    'were impossible to underestimate.',
    'continued to meet everyone\'s expectations.',
    'made everyone wish they were better strangers.',
    'could be used as a bad example.',
    'needed to apologise to the tree creating the oxygen they wasted on that puerile, underdramatized play that lacked anything resembling the Aristotelian unities. In short, it was shit.',
    'were unique in such that being with them was like wearing wet socks.',
    'seemed like they were unable to pour water out of a boot with the instructions on the heel.',
    f'were about as useful as {random.choice(as_useful_as_a)}'
]

cch_gary_insults_sentient = [
    'participation award',
    f'{random.choice(bad_os)} installaiton disc',
    'bottle of Eau de Escherichia coli',
    'bottle of Eau de Staphylococcus epidermidis',
    'McAfee subscription',
    f'{random.choice(virus_list)} infection'
]

cch_gary_insults = [
    f'sentient {random.choice(cch_gary_insults_sentient)}',
    'stale loaf of bread',
    'forgotten sandwich covered in mold'
]

cat_scenario = [
    f'If they developed opposable thumbs tomorrow, within {random.randint(1,20)} they would have achieved world domination.',
    f'I sometimes like to imagine how chaotic things would be if they had telekinesis.'
]

celeb = [
    'Karen Gillan', ## My Number 1 celebrity crush.
    'Ella Balinska', ## She was fantastic in Charlie's Angels. She's also my Number 2 celebrity crush.
    'Alexandra Daddario', ## My Number 3 celebrity crush
    'Daisy Ridley', ## My number 4 celebrity crush
    'Kristen Stewart',
    'Aura Garrido', ## Amelia Folch in El Ministerio del Tiempo
    'Úrsula Corberó', ## Tokyo in Money Heist
    'Emilia Clarke',
    'Tessa Thompson',
    'Scarlett Johansson',
    'Ana de Armas',
    'Léa Seydoux', ## Celebrity crush
    'Kate Beckinsale',
    'Elizabeth Banks', ## Bosley 342 gives off Mom energy.
    'Naomi Scott',
    'Sonequa Martin-Green',
    'Florence Pugh',
    'Evanna Lynch',
    'Emma Watson',
    'Maya Hawke',
    'Chloë Grace Moretz', ## Creator's transition goals.
    'Nathalie Emannuel',
    'Dominique Tipper',
    'Frankie Adams',
    'Taylor Swift',
    'Billie Piper',
    'Jodie Whittaker',
    'Margot Robbie',
    'Rihanna',
    'Awkwafina',
    'Anne Hathaway',
    'Elsa Pataky'
]

cold_things = [
    'the Svalbard Global Seed Vault',
    'an ice cube',
    'gazpacho soup',
    'an Icelandic winter',
    'a Greenlandic winter',
    'an Antarctic winter',
    'nighttime on Pluto',
    'liquid nitrogen',
    'liquid helium',
    'liquid oxygen',
    'ice cream'
]

cold_weather_comment = [
    'If only it fucking snowed once in a while.',
    'It\'s almost at that point where I can see my own breath. It\'s like a tiny ghost.'
]

dentistcomments = [
    'It satisfies me to no end when such circumstances arise that cause it to be rescheduled for a later date',
    'I could not think of a worse way to spend my time',
    'Half the equipment sounds like those mandrakes from Harry Potter',
    'It\'s expensive and painful.'
]

distancelist = [
    'half an acre',
    'half a mile',
    f'{random.randint(3, 81)} kilometres',
    f'{random.randint(2, 51)} miles'
]

dreamscen_location = [
    f'in the {random.randint(24,26)}th century Star Trek universe'
]

dreamscen_prompt = [
    f'there\'s a group of benevolent HBICs called Les Royales where {random.choice(dreamscen_prompts_LesRoyales)}'
]

dreamscenario = [
    f'It\'s set {random.choice(dreamscen_location)} where {random.choice(dreamscen_prompt)}'
]

earth_languages = [
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Bengali',
    'Chinese',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto', ## Conlang
    'Farsi',
    'Finnish',
    'French',
    'German',
    'Greek',
    'Hawaiian',
    'Hebrew',
    'Hungarian',
    'Hindi',
    'Icelandic',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Korean',
    'Latin',
    'Navajo',
    'Norwegian',
    'Polish',
    'Portuguese',
    'Russian',
    'Scottish Gaelic',
    'Spanish',
    'Swahili',
    'Swedish',
    'Thai',
    'Turkish',
    'Ukrainian',
    'Vietnamese',
    'Welsh', ## Cymru am byth!
    'Xhosa', ## Shuri must be protected at all costs.
    'Yiddish',
    'Zulu'
]

except_maybe_one_thing = [ 
    'kittens',
    'cats',
    'rainy days', ## Or as they call it in Britain, "a day ending in a Y."
    'spiders',
    'scaring the shit out of people',
    'Halloween',
    'some good food', ## In the name of all that is holy, avoid having a cuppa at Keele Services. It was horrible.
    f'{random.choice(celeb)}'
]

favefilm_scen = [
    'Charlie\'s Angels (2019)', ## One of my favoruite films from 2019.
    'Ocean\'s 8',
    'Doctor Strange',
    'Doctor Strange and the Multiverse of Madness',
    'Shang-Chi',
    'all three John Wick films', ## The Adjudicator needs to be showered in love, imho.
    'Hitchhiker\'s Guide to the Galaxy',
    'Gunpowder Milkshake',
    'Star Trek',
    'Black Widow',
    'Black Panther'
]

gamingpeeves = [
    'griefers on GTA Online',
    'lag on GTA Online',
    f'failing a timed mission on GTA Online by something like {random.randint(1,1000)/1000} seconds',
    'failing a hard mission on GTA Online', ## Looking at you, Cayo Perico. It's a tough bitch trying to do it w/o being detected.
    f'high ping rates of something like {random.randint(1000,5000)}ms in World of Warships',
    'lag in World of Warships',
    'my computer bluescreening', ## It runs on Windows, but at least my home one can have more than 4 tabs opening w/o hanging like my work one does.
    'my game slowing to a crawl because another game decided it wanted to update then and there',
    'the internet cutting out', ## Only thing worse is slow internet that's just fast enough for an internet connection to be registered.
]

gta_v_obsrv = [
    'Has anyone told Michael De Santa he looks like he\'s holding in a fart for the whole game?', ## He does, though.
    f'I like the chaos. I\'d say the odds of summoning Loki Odinson are {random.randint(8750,10000)/100}%.',
    'I almost always tune the radio to the one with Cara Delevingne on.',
    'Regardless of the car, an attempt at drifting round corners always happens.'
]

namesforbras = [
    'over the shoulder boulder holders',
    'boob jail',
    'booby traps'
]

ofpeople_insults = [
    'Gary, Indiana',
    'Fiat Multipla Mk I', ## It's ugly, and that's an understatement.
    f'{random.choice(bad_os)}'
]

phrases_if_cats_could_talk = [
    'Puny mortals, I summon thee!',
    f'Human, bring me {random.randint(6,48)} fish, and I want it {random.randint(1,16)} minutes ago!',
    'The Duolingo owl can\'t stop me now!'
]

sailorscouts = [
    ##### ##### Outer Sol Senshi
    'Sailor Mercury',
    'Sailor Venus',
    'Sailor Moon',
    'Sailor Mars',
    'Sailor Jupiter',
    'Sailor Saturn',
    'Sailor Uranus',
    'Sailor Neptune',
    'Sailor Pluto'
]

song_list = [
    ##### ##### ##### ##### ##### Songs in List - 46

    ##### ##### A-Ha
    'The Living Daylights',
    ##### ##### Agnes Obel
    'September Song - Agnes Obel',
    ##### ##### Alex Gaudino
    'Destination Calabria',
    ##### ##### Babymetal
    'PA PA YA',
    'Megitsune',
    'Awadema Fever',
    ##### ##### Billie Eilish
    'Bad Guy',
    'Ocean Eyes',
    'You Should See Me in a Crown',
    'All the Good Girls Go to Hell',
    'Ilomilo',
    ##### ##### Blue Swede
    'Hooked on a Feeling',
    ##### ##### Caroline Polachek
    'Bunny is a Rider',
    ##### ##### Cornershop
    'Brimful of Asha',
    ##### ##### Dire Straits
    'Sultans of Swing',
    'Walk of Life',
    'Heavy Fuel',
    'Calling Elvis',
    ##### ##### Duran Duran
    'A View To A Kill',
    ##### ##### ELO
    'Mr Blue Sky',
    ##### ##### Elton John
    'Saturday Night\'s Alright For Fighting',
    ##### ##### Gladys Knight
    'Licence to Kill',
    ##### ##### Gorillaz
    'Doncamatic',
    'Feel Good Inc.',
    'The Apprentice - Gorillaz',
    ##### ##### Gustav Holst
    'The Planets',
    ##### ##### Jamiroquai
    'Alright - Jamiroquai',
    ##### ##### Kekra
    'Rien du tout - Kekra',
    ##### ##### Lady Gaga
    'Paparazzi',
    ##### ##### Lana Del Rey
    'Season Of The Witch - Lana Del Rey',
    ##### ##### Lordi
    'Hard Rock Hallelujah',
    ##### ##### Marvin Gaye
    'Ain\'t No Mountain High Enough',
    ##### ##### O-Zone
    'Dragostea Din Tei',
    ##### ##### Queen
    'Radio Ga Ga',
    'Bohemian Rhapsody',
    ##### ##### Rammstein
    'Ausländer',
    ##### ##### Sabaton
    'Primo Victoria',
    'Aces in Exile',
    'Attero Dominatus',
    'To Hell and Back',
    'Resist and Bite',
    'Night Witches',
    ##### ##### Shivaree
    'Goodnight Moon',
    ##### ##### Sianna
    'N\'essaie pas - Sianna',
    ##### ##### Siouxsie and the Banshees
    'Hall of Mirrors',
    ##### ##### Stereophonics
    'Handbags and Gladrags'
]

sto_women = [
    'Rinna Khev', ## I imagine her looking like Kate Beckinsale.
    'Satra',
    'Syvith',
    'Tiaru Jarok', ## I imagine her looking like Alexandra Daddario.
    'T\'Manda', ## I imagine her looking like Saoirse Ronan.
    'T\'Par'
]

streetfood = [
    ##### ##### Europe
    
    ##### ##### North America
    ##### Mexico
    'memelas',
    'tlayudas',

    ##### ##### South America
    ##### Argentina
    'choripán',
    'empanadas',
    'fugazzeta',
    ##### Bolivia
    'salteñas',
    'helado de canela',
    'buñuelos',
    'sanduíche de chola',
    ##### Brazil
    'acarejé',
    'feijoada',
    ##### Colombia
    'ajiaco',
    'arepa',
    'rompe colchón',
    ##### Peru
    'anticucho',
    'ceviche',
    'picarones',

    ##### ##### Asia
    ##### India
    'chaat',
    'parathas',
    'chole bhature',
    'nihari',
    'seekh kebabs',
    'aloo tikki',
    ##### Indonesia

    ##### Japan
    'takoyaki',
    'okonomiyaki',
    'kushikatsu',
    'udon',
    'yakitori',
    ##### Lebanon
    'shawarma',
    'manaqish'
    ##### Philippines
    
    ##### Taiwan

    ##### Thailand
    'tom yum'
    ##### Singapore
    
    ##### South Korea
    
    ##### Vietnam

    ##### ##### Africa

    ##### ##### Oceania
]

scenarios = [
    'listening to the sounds of someone in tech support yeeting a printer into the stratosphere',
    f'enjoying some {random.choice(streetfood)} as the sun sets',
    'taking the piss out of Windows Vista on account of how monumentally shit it was', ## SideshowBobShuddering.mp4
    'watching a good film in the cinema',
    'gaming for hours on end',
    f'watching {random.choice(favefilm_scen)} for the twentieth time',
    'enjoying that feeling when code runs the way it should on the first try',
    'messing with people by leaving dice at the zoo so they think we\'re playing Jumanji',
    'binging Star Trek until the early hours', ## We need more Xaheans. They are adorable.
    'watching Lord of the Rings in one sitting', ## Takes 12 hours.
    'watching the Addams Family with a inkling that the Droste effect is in motion',
    'introducing them to Sailor Moon (the Japanese dub w/ English subtitles is the best)',
    'making Zombocom references every time a welcome sign is spotted',
    'playing pool and having a few beers',
    'reading a fuckton of IronDad fanfiction'
]

startrek_cinnamonrolls = [
    'Adira Tal',
    'Exri Dax',
    'Jadzia Dax',
    'Me Hani Ika Hali Ka Po', ## "Is that spumoni?" - Po
    'Michael Burnham',
    'Seven of Nine',
    'Tilly',
]

startrek_xaheans = [
    'Xahean Adira',
    'Me Hani Ika Hali Ka Po' ## "Is that spumoni?" - Po
]

startrek_0_obsrv = [
    f'I\'ve decided that all Xaheans are adorable, especially {random.choice(startrek_xaheans)}.',
    f'{random.choice(startrek_cinnamonrolls)} is a cinnamon roll.',
    f'{random.choice(startrek_xaheans)} must be protected at all costs.'
]

stupidly_obvious_things = [
    'Water is wet',
    'Elizabeth Banks radiated mom energy in Charlie\'s Angels',
    f'Cats are plotting world domination and I\'m {random.randint(75,101)}% sure they\'ve formed a hive mind at some point', ## They defo have.
    'Trans women are women',
    'Trans men are men',
    'Cousin Itt is hairy',
    'Chewbacca has hair',
    'Thanos resembles a California raisin that overdid it on the protein', ## I'm surprised Tony Stark didn't say that to his face.
    'Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch is in Wales',
    'Most people in the IT industry hate printers',
    'Every sixty seconds, a minute passes' ## "Together, we can stop this."
]

techproblem = [ ## ...could occur
    'Password problems',
    'An internet outage',
    'A failed update',
    f'A successful {random.choice(bad_os)} installation'
]

voldemort_insult = [
    'he should hide from HowToBasic', ## Tales of the uneggspected.
    'he comes from an egg carton',    ## Yes, I live for bad puns, especially if they're mine.
    'the worst Dr Eggman cosplayer the world has ever known', ## Did not meet eggspectations.
    'an off-brand Kojak'
]

whats_worse_than_x = [
    'A printer',
    f'{random.randint(2,100)} printers',
    'A dirty, dilapidated hotel',
    'Ellesmere Port',
    'Gary, Indiana',
    'New Jersey',
    'A Fiat Multipla Mk I',
    'A neon green Fiat Multipla Mk I',
    'A Moskvitch 412 with fake eyelashes and a go-faster stripe',
    'A Lada with a spoiler', ## Why the fuck would that even be a thing?
    f'A successful {random.choice(bad_os)} installation'
]

file_extension = [
    'sh',
    'py',
    'exe'
]

afraid_examples = [
    'Like someone in tech support when confronted with a printer.',
    'Like most people playing Resident Evil with the lights off.', ## Claire Redfield in the remastered RE2 is defo my fictional transition goal.
    'Like someone in tech support when an update fucks up.', ## Every day, probably.
    f'Like practically everyone when they notice the Duolingo owl following them when they missed their lesson in {random.choice(earth_languages)}.' ## Mofo got tired of listening to The Who, so he opted for vengeance.
    'Like someone when their parents say their full name.'
]

worse_than_pastels = [
    'neon green with bright orange polka dots',
    'tiled with those \'live, laugh, love\' things everywhere' ## That shit not only ugly, but pointless too.
]


##### ##### ##### ##### ##### ##### ##### ##### ##### #####  ##### #####
##### Below is the master array, containing all the things that    #####
##### will actually be tweeted. I try to expand on them and give   #####
##### them a bit of variety, but that is a bit challenging at      #####
##### times.                                                       #####
##### ##### ##### ##### ##### ##### ##### ##### ##### #####  ##### #####

tweetlist = [
    ##### ##### Tweets 1 to 5 • Conditional Tweets
    'I await Wednesday with great interest.', ##### [1] Go to conditional tweetlist.
    'Still isn\'t Halloween yet...', ##### [2] Go to conditional tweetlist.
    'I\'ll be sad when October is gone.', ##### [3] Go to conditional tweetlist.
    'I can\'t wait for October.', ##### [4] Go to conditional tweetlist.
    'Got a 1 in 7 of posting this on the right day, but thank goth it\'s Wednesday.', ##### [5] Go to conditional tweetlist.

    ##### ##### Tweets 6 to 7 • Song Tweets
    f'Why do I have {random.choice(song_list)} stuck in my head all of a sudden?', ##### [6] Go to song tweetlist
    f'I\'m sitting there doing fuck-all and all of a sudden {random.choice(song_list)} plays in my head. Pretty sure my brain\'s a radio station at this point.', ##### [7] Go to song tweetlist

    ##### ##### Tweets 8 to 9 • Street Food Tweets
    f'I\'ve got street food stuck on my mind right now. I think my brain\'s telling me to have some {random.choice(streetfood)}.', ##### [8] Go to streetfood tweetlist
    f'If I could summon food out of thin air, I\'d probably have some {random.choice(streetfood)} in front of me right now.', ##### [9] Go to streetfood tweetlist

    ##### ##### Tweets 10 to 10 • Celebrity Tweets
    f'Mother\'s been trying to guess who has been on my mind today. {random.choice(celeb)} was her latest guess.', ##### [10] Go to celeb tweetlist

    ##### ##### Tweets 11 to 11 • Gaming Peeves
    f'I don\'t know what the worst thing I\'ve personally experienced while gaming is, but {random.choice(gamingpeeves)} ranks high on the list.',

    ##### ##### Tweets 12 to 122 • Generic Tweets
    f'I\'ve been counting how many times Father has said "cara mia" to Mother today. {random.randint(1, 144)} times and counting...',
    f'Pugsley tried to guess what I dreamt about the other night. He guessed it involved {random.choice(celeb)} and some {random.choice(streetfood)} while {random.choice(song_list)} played quietly in the background.',
    f'I\'m craving {random.choice(streetfood)} right now. Where\'s Dr Strange and that sling ring of his? It\'ll save me having to walk to get the food.',
    f'For {random.randint(1, 751)/1000} seconds I imagined Father spending some time in France. As for how dramatic he\'d be on a scale of 1 to 10 when he notices everyone speaking French, I\'d say at least {random.randint(50, 1000)}.',
    f'Where\'s a thunderstorm when you need one? It\'s been at least {random.randint(3,8)} days since the last one.',
    f'There\'s nothing better than a peaceful night, a gentle breeze and a temperature of {random.randint(16,22)}°C',
    f'Thing\'s had a guess at what I dreamt of the other day. "A day out with {random.choice(celeb)}, {random.choice(scenarios)}" was what he wrote down.',
    f'Someone just guessed what\'s on my mind now. They said, "{random.choice(celeb)}, some {random.choice(streetfood)}, and watching {random.choice(favefilm_scen)}". They\'re not far off.',
    f'What I need is a sling ring and some highly advanced technology so that I can give Sailor Pluto some {random.choice(streetfood)} and a much needed hug.',
    f'Sometimes, my internet wants to run like it was made in {random.randint(1327,1933)}.',
    f'Trying to get VS Code, WSL and GitHub to play ball together\'s a pain in the ass. At least {random.randint(95,175)}% pure frustration.',
    f'Why do people make doing certain processes hard? I swear it ends up taking {random.randint(2,6)} hours to do something that should take minutes.',
    f'Woe to the Republic. First republic that comes to mind however\'s the Romulan Republic from STO. {random.choice(sto_women)}... phwaor. Guess that\'s what I get for being a Trekkie.',
    f'I can\'t tell of there\'s a thunderstorm coming or Pugsley\'s had beans again. {random.randint(2,13)} cans of air freshener won\'t be enough if it\'s not thunder.',
    f'Ah, what I would not give for {random.choice(celeb)} to look me in the eye and say \'Cara mia\'.',
    f'Five minutes into Star Trek and all I can say is {random.choice(startrek_0_obsrv)}',
    f'I don\'t know who is on my mind more right now - {random.choice(celeb)} or {random.choice(celeb)}.',
    f'I dreamt something that sounded like fanfiction. {random.choice(dreamscenario)}',
    f'Took me {random.randint(1,2500)/10000} seconds to join the #wenclair fandom.',
    f'I hope they make #wenclair canon.'
    f'Dreamt I was looking at {random.choice(celeb)} the way Mother and Father look at one another. I\'m about as surprised as I would be if you said the sun was hotter than {random.choice(cold_things)}.'
    f'Found myself waiting {random.randint(45,195)} minutes for a meal at a restaurant once. Not going there again.',
    'This Voldemort fellow looks as though Uncle Fester forgot his nose.',
    'Remind me to ask Cousin Itt if that\'s a relative of his next to Han Solo.',
    'I am not perky.',
    'A spider is a girl\'s best friend.',
    f'What\'s worse than Camp Chippewa? {random.choice(whats_worse_than_x)}, according to someone whose comment I overheard the other day.',
    'On Wednesdays, we wear black.',
    f'{random.choice(sailorscouts)}? I like her.',
    f'Cats are homicidal furballs. {random.choice(cat_scenario)}.',
    f'I hate everything... except maybe {random.choice(except_maybe_one_thing)}',
    'I\'ll stop wearing black when they make a darker color.',
    'You severely underestimate my apathy.',
    f'Be afraid. Be very afraid. {random.choice(afraid_examples)}',
    f'Damn, Lestrange. You could\'ve picked a man with a nose at least. Dude looks like {random.choice(voldemort_insult)}.',
    'Still waiting on that full moon.',
    'I heard someone saying that Thing used to be Luke Skywalker\'s hand. I\'m not so sure about that yet.',
    '\'Wednesday\'s child is full of woe.\' Sounds about right.',
    'I heard that someone described Camp Chippewa as the Windows Vista of camps. I tried that once when learning how to use a computer. They\'re not wrong.',
    'Okay, I admit it. I like Billie Eilish.',
    f'That moment when you look at {random.choice(celeb)} and you feel the last vestiges of your heterosexuality disappearing. Yes. Mother noticed.',
    'Okay, I admit it, I am officially gay for Ella Balinska. I liked that one part of the quarry scene and I didn\'t blame Sabina for covering her eyes. None of them seem the macabre type.',
    'Who\'s that off-brand Uncle Fester playing at in the East?',
    'That feeling you get when you take your bra off after a long day. I can agree with that.',
    'Have you ever lied there thinking about something and the next thing you know it\'s the next morning? Only caffeine and the works of Poe sustain me from then on.',
    f'Sometimes, {random.randint(7,10)}:{minutes_2lz}am feels like it\'s too early.',
    f'I\'m gay for {random.choice(celeb)}. I\'m pretty sure Mother knows.',
    'Sometimes I get bored enough that I see no other thing to do than to look through memes for hours on end. The creativity is... impressive.',
    f'There\'s nothing worse than a bad internet connection, especially when I\'m trying to game. {random.randint(250,10000)/1000}Mbps? Seriously?',
    f'I sometimes find myself drinkng tea as much as Captain Janeway drinks coffee. She drank coffee at Warp {random.randint(750,997)/100}',
    f'I wonder whose idea was it to call bras \'{random.choice(namesforbras)}\'.',
    f'I don\'t like dentists. {random.choice(dentistcomments)}.',
    'Sometimes, there\'s no better thing than a lie in.',
    'I want nothing more than to just chill on some days. Today seems to be one of them.',
    'I can\'t tell whether it\'s going to rain or not some days.',
    'I can almost hear people watching the Addams Family films. So this is what the Droste effect is. Interesting.',
    f'Man, those two at Camp Chippewa were the {random.choice(ofpeople_insults)} of people.',
    f'Those two at Camp Chippewa {random.choice(cch_insults)}',
    'It\'s frustrating when you\'re in a hurry and things don\'t go to plan.',
    'Chloë Grace Moretz voiced me well.',
    'I can hear that counterfeit Uncle Fester shitting bricks after what I\'ve been hearing.',
    f'./wednesday-addams.{random.choice(file_extension)}? Do they think I\'m emotionless like Data? I\'ll gladly have a cat, however.',
    'Those clouds had better not be mushroom shaped. I enjoy the macarbe, but not that.',
    f'Linux intrigues me for some reason, though I am not quite sure why. Could you imagine a sysadmin in the Addams Family? {random.choice(techproblem)} could occur and Father would challenge the computer to a duel.',
    f'Gay and tired? That sounds like me in the evenings. {100-gaytired}% gay, {gaytired}% tired.',
    'Sometimes I just want to sleep after a long day.',
    f'"Men is too headache." I couldn\'t agree more, especially if the man in question is that {random.choice(cch_gary_insults)} from Camp Chippewa.',
    f'If cats could talk, I wonder what they\'d say. Probably something like "{random.choice(phrases_if_cats_could_talk)}"',
    'I sometimes wish I was in the Townsend Agency. Someone should make fanfiction of that, come to think of it. The Addams Family x 2019 Charlie\'s Angels would be an interesting combination',
    'Tea is the only thing keeping me awake sometimes.',
    'I just saw Emma Stone\'s portrayal of Cruella and all I can say is that I want to be in her arms.',
    'Being normal is boring.',
    'I overheard someone saying that some company\'s headquarters was their version of hell. I can only assume they work in tech support, so it\'s fortunate I don\'t bother with printers. Sounds like more trouble than they\'re worth.',
    f'I\'m still getting over Debbie\'s choice to use pastels. Like, seriously? Could be worse. It could be {random.choice(worse_than_pastels)}.',
    'I\'ve got the music from Sailor Moon stuck in my head. Not gonna lie, though, I like it.',
    'A friend of mine told me I should cosplay as Sailor Saturn. I\'ll give it some thought. She\'s my favourite sailor scout, after all.',
    'Could you imagine if Uncle Fester went to an anime convention? They\'d say One Punch Man let himself go.',
    f'I hate it when I want a lie in and something wakes me up. {random.randint(1/101)/100}/10 - do not recommend.',
    f'I want a lie in. I\'m {random.randint(9000,10000)/100}% sure I\'m mentally still in bed.',
    f'Spotted a black cat out of the window. It\'s probably thinking about purrgatory, either that or one of their {random.randint(1,100000)} plans for world domination.',
    f'I doubt Father could handle a trip to France. I can hear "Tish, that\'s French!" from {random.choice(distancelist)} away.',
    f'What in the fresh fuck is this Barbie thing? I\'ve sat there for {random.randint(1, 9)} hours trying to understand it only to still be confused.',
    'I forget to sleep sometimes, and I always end up paying for it the next day, moreso if I rise early. What\'s worse is rising early for no reason when you want a lie in.',
    f'When the weather app says it\'s going to rain and then it doesn\'t. Ugh... {random.randint(60,90)}% chance, my ass.',
    'A litle but of sudden rain is nice.',
    'I like Fridays too.',
    'I tried to upgrade my computer once but it hung at the wrong moment. The end result was a catastophe that required reinstalling the operating system and half a day of recovery.',
    f'I think I\'m the most prepared in the Addams clan. Pugsley\'s guess of {random.randint(1, 1000)} million of them was quite the overstatement.',
    'Why did they choose November 23rd? I\'d\'ve released it on October 31st. Halloween\'s a much better date.',
    'I think Jenna Ortega will do well as Wednesday.',
    f'A wig from a bargain store and a pinafore is not an ideal cosplay - it\'s more like {random.randint(1,300)/100}/10 - though kudos for the effort at least.',
    f'I\'ve had the same song stuck in my head for the last {random.randint(2, 14)} days... {random.choice(song_list)}',
    'What is this \'uwu\' energy people keep mentioning? I\'m aware kittens possess that energy, but still...',
    'Fuck. It\'s sunny. Where\'s my umbrella?',
    f'It\'s a bit cold outside. {random.choice(cold_weather_comment)}',
    f'It\'s quite a pain in the ass when there\'s short deadline in which to do something and I have to rewrite the entirety of something in the space of a day.',
    'It was foggy this morning, and I liked it. Now it\'s sunny... damn it.',
    f'Ask me to write something down in a hurry and you can guarantee that in a week\'s time, I\'ll need the Rosetta Stone just to read what the fuck I\'ve written. {random.choice(bad_writing_obsrv)}.',
    'It\'s warmer than I expected it to be today. All that\'s missing is a blanket, a girlfriend, and some nice horror films.',
    f'It\'s colder than I expected it to be today. A reminder of the cold embrace of death. {random.choice(cold_weather_comment)}',
    f'I want something to eat, but I don\'t know what I want. At least {random.randint(25,75)}% of me wants {random.choice(streetfood)}.',
    f'I\'m thinking about food. Odds are it\'s because I can smell it cooking. I hope whoever cooked it hasn\'t burned it, though knowing some people, there\'s a {random.randint(35,65)}% chance they have.',
    'Sometimes I get halfway through the day and mentally I go back to bed.',
    'They had men doing construction work out the window once. At least their radio choices were decent.',
    f'Been playing a lot of GTA V recently. {random.choice(gta_v_obsrv)}',
    f'I\'m not surprised that lettuce won. I give myself {random.randint(2, 30)} days before I have some surreal dream about a civilization of sentient pieces of lettuce.',
    'I\'ve been playing games so much I expect Cara Delevingne\'s voice to be heard every time I turn the radio on.',
    'I tried brussels sprouts once. No thanks. What madman brought those things into existence?',
    'No idea what I wan\'t to do right now.',
    f'Asking myself whether I should make myself a cup of tea or wait until later. I give it {random.randint(30,150)} minutes before the urge for a cup of tea becomes overwhelming.',
    f'My brain plays random elevator music if I stand there long enough. Makes me sound like an NPC. Kicks in {random.randint(1000,3000)/1000} seconds after the doors close.',
    f'I sometimes have those momemts when all I can hear is someone shouting loudly at something out of pure frustration. I\'d say it\'s probably at around {random.randint(110,145)} decibels.',
    f'Sometimes, you just have to tell people things that are stupidly obvious. "{random.choice(stupidly_obvious_things)}", for example.'
]

conditional_tweetlist = [
    'I\'m quite enjoying Wednesday.', ##### conditional_tweet[0]
    'It\'s Halloween. Finally.', ##### conditional_tweet[1]
    'Halloween\'s not for some time yet. Still, another year closer to death\'s cold embrace.', ##### conditional_tweet[2]
    'October. The best month of all.', ##### conditional_tweet[3]
    'Thank goth it\'s Wednesday. The best day of the week, though I may be a bit biased on that one.' ##### conditional_tweet[4]
]

