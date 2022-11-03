import random

song_list = [
    ##### ##### ##### ##### ##### Songs in List - 29

    ##### ##### A-Ha
    'The Living Daylights',
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
    ##### ##### Gustav Holst
    'The Planets',
    ##### ##### Jamiroquai
    'Alright by Jamiroquai',
    ##### ##### Lady Gaga
    'Paparazzi',
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
    ##### ##### Siouxsie and the Banshees
    'Hall of Mirrors',
    ##### ##### Stereophonics
    'Handbags and Gladrags'
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
    ##### Colombia
    'ajiaco',
    'arepa',
    'rompe colchón',
    ##### Peru
    'anticucho',
    'ceviche',
    'picarones'

    ##### ##### Asia

    ##### ##### Africa

    ##### ##### Oceania
]

celeb = [
    'Karen Gillan',
    'Ella Balinska',
    'Alexandra Daddario',
    'Daisy Ridley',
    'Kristen Stewart',
    'Aura Garrido', ## Amelia Folch in El Ministerio del Tiempo
    'Úrsula Corberó', ## Tokyo in Money Heist
    'Emilia Clarke',
    'Tessa Thompson',
    'Scarlett Johansson',
    'Ana de Armas',
    'Léa Seydoux',
    'Kate Beckinsale',
    'Elizabeth Banks',
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
    'Anne Hathaway'
]

gamingpeeves = [
	'griefers on GTA Online',
	'lag on GTA Online',
    f'failing a timed mission on GTA Online by something like {random.randint(1,1000)/1000} seconds',
    'failing a hard mission on GTA Online',
	f'high ping rates of something like {random.randint(1000,5000)}ms in World of Warships',
    'lag in World of Warships',
    'my computer bluescreening',
    'my game slowing to a crawl because another game decided it wanted to update at that specific moment when I\'m trying to do something',
    'the internet cutting out',
]
sailorscouts = [
    ##### ##### Outer Sol Senshi
    'Sailor Saturn',
    'Sailor Uranus',
    'Sailor Neptune',
    'Sailor Pluto'
]

ofpeople_insults = [
    'Gary, Indiana',
    'Windows Vista',
    'Fiat Multipla Mk I',
    'Windows ME'
]

distancelist = [
    'half an acre',
    'half a mile',
    f'{random.randint(3, 81)} kilometres',
    f'{random.randint(2, 51)} miles'
]

favefilm_scen = [
    'Charlie\'s Angels (2019)',
    'Ocean\'s 8',
    'Doctor Strange',
    'Doctor Strange and the Multiverse of Madness',
    'Shang-Chi',
    'all three John Wick films',
    'Hitchhiker\'s Guide to the Galaxy',
    'Gunpowder Milkshake',
    'Star Trek',
    'Black Widow'
]

scenarios = [
    'listening to the sounds of someone in tech support yeeting a printer into the stratosphere',
    f'enjoying some {random.choice(streetfood)} as the sun sets',
    'taking the piss out of Windows Vista on account of how monumentally shit it was',
    'watching a good film in the cinema',
    'gaming for hours on end',
    f'watching {random.choice(favefilm_scen)} for the twentieth time',
    'enjoying that feeling when code runs the way it should on the first try',
    'messing with people by leaving dice at the zoo so they think we\'re playing Jumanji',
    'binging Star Trek until the early hours',
    'watching Lord of the Rings in one sitting',
    'watching the Addams Family, half of us wondering whether the Droste Effect is happening like something out of the Twilight Zone',
    'introducing them to Sailor Moon (the Japanese dub w/ English subtitles is the best)',
    'making Zombocom references every time a welcome sign is spotted',
    'playing pool and having a few beers',
    'reading a fuckton of IronDad fanfiction'
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
    'A Lada with a spoiler'
]

phrases_if_cats_could_talk = [
    'Puny mortals, I summon thee!',
    f'Human, bring me {random.randint(6,48)} fish, and I want it {random.randint(1,16)} minutes ago!'
]

tweetlist = [
    ##### ##### Tweets 1 to 5 • Conditional Tweets
    'I await Wednesday with great interest.', ##### [1] Go to conditional tweetlist.
    'Still isn\'t Halloween yet...', ##### [2] Go to conditional tweetlist.
    'I\'ll be said when October is gone.', ##### [3] Go to conditional tweetlist.
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

    ##### ##### Tweets 12 to 113 • Generic Tweets
    f'I\'ve been counting how many times Father has said "cara mia" to Mother today. {random.randint(1, 144)} times and counting...',
    f'Pugsley just tried to guess what I dreamt about the other night for reasons I can\'t quite fathom. He\'s under the impression it involved {random.choice(celeb)} and some {random.choice(streetfood)} while {random.choice(song_list)} played quietly in the background.',
    f'I\'m craving {random.choice(streetfood)} right now. Where\'s Dr Strange and that sling ring of his? It\'ll save me having to walk to get the food.',
    f'For {random.randint(1, 751)/1000} seconds I imagined Father spending some time in France. As for how dramatic he\'d be on a scale of 1 to 10 when he notices everyone speaking French, I\'d say at least {random.randint(50, 1000)}.',
    f'Where\'s a thunderstorm when you need one? It\'s been at least {random.randint(3,8)} days since the last one.',
    f'There\'s nothing better than a peaceful night, a gentle breeze and a temperature of {random.randint(16,22)}°C',
    f'Thing\'s had a guess at what I dreamt of the other day. "A day out with {random.choice(celeb)}, {random.choice(scenarios)}" was what he wrote down.',
    f'Someone\'s just tried to guess what\'s on my mind now. They said, "{random.choice(celeb)}, a decent serving of {random.choice(streetfood)}, and watching {random.choice(favefilm_scen)}". They\'re not far off...',
    f'What I need is a sling ring and some highly advanced technology so that I can give Sailor Pluto some {random.choice(streetfood)} and a much needed hug.',
    f'Sometimes, my internet wants to run like it was made in {random.randint(1327,1933)}.',
    f'Trying to get VS Code, WSL and GitHub to play ball together\'s a pain in the ass. At least {random.randint(95,175)}% pure frustration.',
    f'Why do people make doing certain processes hard? I swear it ends up taking {random.randint(2,6)} hours to do something that should take minutes.',
    'Woe to the Republic.',
    f'I can\'t tell of there\'s a thunderstorm coming or Pugsley\'s had beans again. {random.randint(2,13)} cans of air freshener won\'t be enough if it\'s not thunder.',
    f'Ah, what I would not give for {random.choice(celeb)} to look me in the eye and say \'Cara mia\'.',
    'This Voldemort fellow looks as though Uncle Fester forgot his nose.',
    'Remind me to ask Cousin Itt if that\'s a relative of his next to Han Solo.',
    'I am not perky.',
    'A spider is a girl\'s best friend.',
    f'What\'s worse than Camp Chippewa? {random.choice(whats_worse_than_x)}, according to someone whose comment I overheard the other day.',
    'On Wednesdays, we wear black.',
    f'{random.choice(sailorscouts)}? I like her.',
    'Cats are homicidal furballs.',
    'I hate everything.',
    'I\'ll stop wearing black when they make a darker color.',
    'You severely underestimate my apathy.',
    'Be afraid. Be very afraid.',
    'Damn, Lestrange. You could\'ve picked a man with a nose at least.',
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
    f'Sometimes, {random.randint(7,10)}am feels like it\'s too early.',
    f'I\'m gay for {random.choice(celeb)}. I\'m pretty sure Mother knows.',
    'Sometimes I get bored enough that I see no other thing to do than to look through memes for hours on end. The creativity is... impressive.',
    f'There\'s nothing worse than a bad internet connection, especially when I\'m trying to game. {random.randint(250,10000)/1000}Mbps? Seriously?',
    'I sometimes find myself drinkng tea as much as Captain Janeway drinks coffee.',
    'I wonder whose idea was it to call bras \'over the shoulder boulder holders\'.',
    'I don\'t like dentists.',
    'Sometimes, there\'s no better thing than a lie in.',
    'I want nothing more than to just chill on some days. Today seems to be one of them.',
    'I can\'t tell whether it\'s going to rain or not some days.',
    'I can almost hear people watching the Addams Family films everywhere. So this is what the Droste effect is. Interesting.',
    f'Man, those two at Camp Chippewa were the {random.choice(ofpeople_insults)} of people.',
    'It\'s frustrating when you\'re in a hurry and things don\'t go to plan.',
    'Chloë Grace Moretz voiced me well.',
    'I can hear that counterfeit Uncle Fester shitting bricks after what I\'ve been hearing.',
    './wednesday-addams.sh? Do they think I\'m emotionless like Data? I\'ll gladly have a cat, however.',
    'Those clouds had better not be mushroom shaped. I enjoy the macarbe, but not that.',
    'Linux intrigues me for some reason, though I am not quite sure why. Could you imagine a sysadmin in the Addams Family?',
    'Gay and tired? That sounds like me in the evenings.',
    'Sometimes I just want to sleep after a long day.',
    '"Men is too headache." I couldn\'t agree more.',
    f'If cats could talk, I wonder what they\'d say. Probably something like "{random.choice(phrases_if_cats_could_talk)}"',
    'I sometimes wish I was in the Townsend Agency. Someone should make fanfiction of that, come to think of it. The Addams Family x 2019 Charlie\'s Angels would be an interesting combination',
    'Tea is the only thing keeping me awake sometimes.',
    'I just saw Emma Stone\'s portrayal of Cruella and all I can say is that I want to be in her arms.',
    'Being normal is boring.',
    'I overheard someone saying that some company\'s headquarters was their version of hell. I can only assume they work in tech support, so it\'s fortunate I don\'t bother with printers. Sounds like more trouble than they\'re worth.',
    'I\'m still getting over Debbie\'s choice to use pastels. Like, seriously?',
    'I\'ve got the music from Sailor Moon stuck in my head. Not gonna lie, though, I like it.',
    'A friend of mine told me I should cosplay as Sailor Saturn. I\'ll give it some thought. She\'s my favourite sailor scout, after all.',
    'Could you imagine if Uncle Fester went to an anime convention? They\'d say One Punch Man let himself go.',
    'I hate it when I want a lie in and something wakes me up.',
    'I want a lie in.',
    'Spotted a black cat out of the window. It\'s probably thinking about purrgatory.',
    f'I doubt Father could handle a trip to France. I can hear "Tish, that\'s French!" from {random.choice(distancelist)} away.',
    f'What in the fresh fuck is this Barbie thing? I\'ve sat there for {random.randint(1, 9)} hours trying to understand it only to still be confused.',
    'I forget to sleep sometimes, and I always end up paying for it the next day, moreso if I rise early.',
    'When the weather app says it\'s going to rain and then it doesn\'t. Ugh...',
    'A litle but of sudden rain is nice.',
    'I like Fridays too.',
    'I tried to upgrade my computer once but it hung at the wrong moment. The end result was a catastophe that required reinstalling the operating system and half a day of recovery. My plans for sleeping were fucked. Must\'ve been four in the morning by the time everything was sorted again.',
    f'I think I\'m the most prepared in the Addams clan. Pugsley\'s guess of {random.randint(1, 1000)} million of them was quite the overstatement.',
    'Why did they choose November 23rd? I\'d\'ve released it on October 31st. Halloween\'s a much better date.',
    'I think Jenna Ortega will do well as Wednesday.',
    'A wig from a bargain store and a pinafore is not an ideal cosplay, though kudos for the effort at least.',
    f'I\'ve had the same song stuck in my head for the last {random.randint(2, 14)} days...',
    'What is this \'uwu\' energy people keep mentioning? I\'m aware kittens possess that energy, but still...',
    'Fuck. It\'s sunny. Where\'s my umbrella?',
    'It\'s a bit cold outside.',
    'It\'s quite a pain in the ass when there\'s short deadline in which to do something and I have to rewrite the entirety of something in the space of a day.',
    'It was foggy this morning, and I liked it. Now it\'s sunny... damn it.',
    'Ask me to write something down in a hurry and you can guarantee that in a week\'s time, I\'ll need the Rosetta Stone just to read what the fuck I\'ve written.'
    'It\'s warmer than I expected it to be today. All that\'s missing is a blanket, a girlfriend, and some nice horror films.',
    'It\'s colder than I expected it to be today. A reminder of the cold embrace of death.',
    'I want something to eat, but I don\'t know what I want.',
    'I\'m thinking about food. Odds are it\'s because I can smell it cooking. I hope whoever cooked it hasn\'t burned it.',
    'Sometimes I get halfway through the day and mentally I go back to bed.',
    'They had men doing construction work out the window once. At least their radio choices were decent.',
    'Been playing a lot of GTA V recently. I like the chaos.',
    f'I\'m not surprised that lettuce won. I give myself {random.randint(2, 30)} days before I have some surreal dream about a civilization of sentient pieces of lettuce.',
    'I\'ve been playing games so much I expect Cara Delevingne\'s voice to be heard every time I turn the radio on.',
    'I tried brussels sprouts once. No thanks. What madman brought those things into existence?',
    'No idea what I wan\'t to do right now.',
    'Asking myself whether I should make myself a cup of tea or wait until later.',
    'My brain plays random elevator music if I stand there long enough. Makes me sound like an NPC.'
]

conditional_tweetlist = [
    'I\'m quite enjoying Wednesday.', ##### [1] Go to conditional tweetlist.
    'It\'s Halloween. Finally.', ##### [2] Go to conditional tweetlist.
    'Halloween\'s not for some time yet. Still, another year closer to death\'s cold embrace.', ##### [3] Go to conditional tweetlist.
    'October. The best month of all.', ##### [4] Go to conditional tweetlist.
    'Thank goth it\'s Wednesday. The best day of the week, though I may be a bit biased on that one.' ##### [5] Go to conditional tweetlist.

]


## west space oak motor crater aim typical exercise frown tray plug awful