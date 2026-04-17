#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# ==================== DATA 13 CERITA GRADE 3 ====================
stories = [
    {
        "num": 1,
        "title": "Gary and the Boy at the Supermarket",
        "file": "01-gary-supermarket.html",
        "key": "garySupermarket",
        "audio": "Gary and the Boy at the Supermarket.mp3",
        "text": "Gary went to the supermarket to buy some eggs. He saw a suspicious-looking boy. He followed the boy. He saw the boy putting two chocolate bars into his pocket. Gary told the security guard about the boy. The boy was caught. The security guard thanked Gary for his help."
    },
    {
        "num": 2,
        "title": "Victor's Art Competition",
        "file": "02-victor-art.html",
        "key": "victorArt",
        "audio": "Victor's Art Competition.mp3",
        "text": "Last Saturday, Victor and his classmates took part in an art competition organized by the Ministry of Education. The competition was held at a shopping complex. More than eighty primary school pupils registered for the competition."
    },
    {
        "num": 3,
        "title": "Banana Fritters",
        "file": "03-banana-fritters.html",
        "key": "bananaFritters",
        "audio": "Banana Fritters.mp3",
        "text": "Most people like to eat banana fritters. It is a popular snack. Banana fritters are available almost anywhere in town. They are usually sold at hawker centres. Banana fritters are cheap and worth the money you pay for them."
    },
    {
        "num": 4,
        "title": "Chong's Scary Night",
        "file": "04-chong-scary.html",
        "key": "chongScary",
        "audio": "Chong's Scary Night.mp3",
        "text": "One night, Chong returned home late after watching a horror movie with his friends. As it was almost past midnight, he did not switch on the lights in his room. Quickly, he changed into his pyjamas and dived under the blanket. Suddenly, he felt something moving near his feet. He let out a shout and turned on the lights. He saw his pet dog lying on his bed."
    },
    {
        "num": 5,
        "title": "Our Precious Earth",
        "file": "05-precious-earth.html",
        "key": "preciousEarth",
        "audio": "Our Precious Earth.mp3",
        "text": "Earth is the only planet that supports life. The surroundings in which man lives is called the environment. The environment includes fresh air, sunlight, forests, rivers and animals. The environment is very important to man because it provides him with air, food, water and shelter. Without these elements, he cannot survive."
    },
    {
        "num": 6,
        "title": "The Snatch Theft",
        "file": "06-snatch-theft.html",
        "key": "snatchTheft",
        "audio": "The Snatch Theft.mp3",
        "text": "One day, a lady was walking in the car park. She was walking towards her car. Suddenly, a man came from behind and snatched her handbag. Then, the man ran away. She was shocked and shouted for help. A few men heard her screams and went to help her. They ran after the robber and caught him."
    },
    {
        "num": 7,
        "title": "A Hike Near the Reservoir",
        "file": "07-hike-reservoir.html",
        "key": "hikeReservoir",
        "audio": "A Hike Near the Reservoir.mp3",
        "text": "During the holidays, Seng Hooi, Jimmy and Rahim went for a hike near the reservoir. Each of them had a cap and a haversack. Jimmy was the leader. He used a compass to find their way around. They packed the food and drinks into their haversacks. They walked for two hours and finally they stopped to rest. They took out the food and drinks from their haversacks. After enjoying the food and drinks, they continued their journey."
    },
    {
        "num": 8,
        "title": "The Python in the Park",
        "file": "08-python-park.html",
        "key": "pythonPark",
        "audio": "The Python in the Park.mp3",
        "text": "Alan and his family always take a stroll in the park after dinner. One day, Alan saw a python curled around a branch of a tree. The police arrived five minutes later. They took a bamboo stick and gunny sack. The policemen shook the tree carefully to make the python fall off from the branch."
    },
    {
        "num": 9,
        "title": "Raju's New Roller-blades",
        "file": "09-raju-rollerblades.html",
        "key": "rajuRoller",
        "audio": "Raju's New Roller-blades.mp3",
        "text": "Raju had been asking his father to buy him a pair of Roller-blades. His father finally decided to buy him one. Raju and his father went to a sports shop; his father paid two hundred dollars for a pair. Raju was very happy. Later in the evening, he went to the park to try his new Roller-blades. As this was the first time he used the Roller-blades, he fell but he was not seriously hurt."
    },
    {
        "num": 10,
        "title": "The Road Accident",
        "file": "10-road-accident.html",
        "key": "roadAccident",
        "audio": "The Road Accident.mp3",
        "text": "Last week, as Mary was walking along a busy road, she saw an accident. A school bus had knocked down a motorcyclist. The motorcyclist was badly injured and his head and hands were bleeding. Mary quickly ran to the nearest phone to call for the ambulance. The ambulance arrived five minutes later. The motorcyclist was sent to hospital. Later, the police came to question the eye witnesses and control the traffic jam."
    },
    {
        "num": 11,
        "title": "The Big Bully",
        "file": "11-big-bully.html",
        "key": "bigBully",
        "audio": "The Big Bully.mp3",
        "text": "There was a big bully in Paul's school. The other children were very scared of him. He used to tease and punch them. He took their money and copied their homework. One day, he climbed a tree and fell from it. He was sent to hospital because he broke his leg. The other children visited him and passed him the teacher's note. The big bully was ashamed of himself and decided to be friends with the other children."
    },
    {
        "num": 12,
        "title": "Ali and the Broken Window",
        "file": "12-ali-broken-window.html",
        "key": "aliWindow",
        "audio": "Ali and the Broken Window.mp3",
        "text": "One Saturday afternoon, Ali was doing his homework when the telephone rang. It was his friend, Dennis. He asked Ali to meet him at the playground to play football. Ali agreed. There were some people jogging at the playground. Ali and his friends went to the field next to a house which belonged to Mr. Rama. The boys were very happy kicking the ball. Suddenly, Ali kicked the ball too hard and it broke Mr. Rama's window. All the boys ran away when Mr. Rama shouted. Ali went back home and told his mother about the incident. Later, Ali and his mother went to apologize to Mr. Rama."
    },
    {
        "num": 13,
        "title": "The Camping Trip",
        "file": "13-camping-trip.html",
        "key": "campingTrip",
        "audio": "The Camping Trip.mp3",
        "text": "Jack and his friends went on a camping trip in the jungle during the last holidays. Being the oldest, Jack was chosen to lead them. They packed their equipment and set out for the jungle. The hike was long and tedious. His younger friends were tired and their spirits were low. Jack led them on with some singing and encouragement. They came to a clearing by a stream and decided to camp there. They started a campfire which they hoped would keep the wild animals away. Jack gave them a briefing about camping rules. It was for the benefit of the newer and inexperienced members."
    }
]

# ==================== TEMPLATE (pakai 04-hardworking-courier.html sebagai dasar) ====================
with open('../supp4/stories/04-hardworking-courier.html', 'r', encoding='utf-8') as f:
    template = f.read()

os.makedirs("stories", exist_ok=True)

for i, story in enumerate(stories):
    prev_page = stories[i-1]["file"] if i > 0 else ""
    next_page = stories[i+1]["file"] if i < len(stories)-1 else ""
    
    content = template
    
    # Ganti data spesifik
    content = content.replace("const STORY_KEY = 'courier';", f"const STORY_KEY = '{story['key']}';")
    content = content.replace("const NEXT_PAGE = '05-alice-jungle.html';", f"const NEXT_PAGE = '{next_page}';")
    content = content.replace("const PREV_PAGE = '03-may-disney.html';", f"const PREV_PAGE = '{prev_page}';")
    content = content.replace('<title>The Hardworking Courier · Grade 4</title>', f'<title>{story["title"]} · Grade 3</title>')
    content = content.replace('<h2>📖 The Hardworking Courier</h2>', f'<h2>📖 {story["title"]}</h2>')
    content = content.replace('src="../audio/The Hardworking Courier.mp3"', f'src="../audio/{story["audio"]}"')
    content = content.replace('href="../index-supp4.html"', 'href="../index-supp3.html"')
    
    # Ganti originalStory
    old_story = "Mr. Lim is a courier and he delivers packages to many homes every day. Mr. Lim is a hardworking man and he starts work early in the morning. His job is not easy as he has to work in the rain and under the hot sun. Once, a very fierce dog chased him and he was almost bitten. Since then, he looks around whenever he hears a dog bark."
    content = content.replace(f'const originalStory = `{old_story}`;', f'const originalStory = `{story["text"]}`;')
    
    filepath = os.path.join("stories", story["file"])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {story['file']}")

print(f"\n🎉 {len(stories)} files created in 'stories/' folder.")
