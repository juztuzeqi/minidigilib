#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

stories = [
    {
        "num": 1,
        "title": "Aquarium Fishes",
        "file": "01-aquarium-fishes.html",
        "key": "aquariumFishes",
        "audio": "Aquarium Fishes.mp3",
        "text": "Peter and his brother, Paul, like Aquarium fishes. They love to go to the small aquarium near their home. They like to look at all the fishes in the shop. Peter's favourite is the bright orange goldfish. Paul prefers the fighting fish."
    },
    {
        "num": 2,
        "title": "Collin's Puppy",
        "file": "02-collin-puppy.html",
        "key": "collinPuppy",
        "audio": "Collin's Puppy.mp3",
        "text": "Colin has a puppy. He loves his little puppy. It is all white. Colin names his puppy 'Snowy'. Snowy is very playful. It likes to jump on Colin and lick him on his nose. Snowy likes Colin to roll it over and tickle it. Snowy enjoys going for walks with Colin. Snowy waits for Colin to come back from school every evening. It barks and wags its tail happily when it sees Colin. It knows that Colin is going to take it out for a walk."
    },
    {
        "num": 3,
        "title": "My Pet Hoppy",
        "file": "03-pet-hoppy.html",
        "key": "petHoppy",
        "audio": "My Pet Hoppy.mp3",
        "text": "I have a pet. My pet's name is Hoppy. I named him Hoppy because he likes to hop. My pet is a rabbit. My parents gave it to me for my birthday. He likes to eat carrots and vegetables. I feed him after school. In the evening, I play with him. My younger sister also likes to play with him. Sometimes, I take him to the park in the evenings. My friends like to play with him. My father built a hutch for him. He stays there. He also sleeps there. I help my father clean the hutch every day. I like Hoppy very much."
    },
    {
        "num": 4,
        "title": "Going Fishing",
        "file": "04-going-fishing.html",
        "key": "goingFishing",
        "audio": "Going Fishing.mp3",
        "text": "Kenny and his father went fishing last week. They went to the nearby river. They took along some worms, fishing rods and a pail. They also brought some food to eat. When they reached the river, his father looked for a good spot. Then he put some worms in the fishing line. After that he threw the line into the river. They both sat at the river bank. Suddenly, the line moved. 'There is a fish', he said. They both pulled the fish out. It was a big fish. They were very happy. They went home with a big fish."
    },
    {
        "num": 5,
        "title": "Samantha and Kelly",
        "file": "05-samantha-kelly.html",
        "key": "samanthaKelly",
        "audio": "Samantha and Kelly.mp3",
        "text": "Samantha and Kelly are cousins. Samantha is older than Kelly. She takes good care of Kelly when she comes to visit. Sometimes, Samantha reads to Kelly. Sometimes, she takes her to the playground. Kelly likes to play on the swings. She also enjoys playing hide-and-seek with Samantha."
    },
    {
        "num": 6,
        "title": "Bryan's New Bicycle",
        "file": "06-bryan-bicycle.html",
        "key": "bryanBicycle",
        "audio": "Bryan's New Bicycle.mp3",
        "text": "It's Bryan's seventh birthday. His parents bought him a birthday present. It is a shiny blue bicycle. Bryan loves his new bicycle. He cycles to the park every evening. He lets his friends take turns to ride on it too."
    },
    {
        "num": 7,
        "title": "At a Bookshop",
        "file": "07-at-bookshop.html",
        "key": "atBookshop",
        "audio": "At a Bookshop.mp3",
        "text": "Jenny and her mother are at a bookshop. They want to buy some story books. Jenny is in the Children's Section. She looks at all the books. She carefully picks three books to buy. The three books are 'The Little Pigs', 'The Enormous Turnip' and 'Peter Pan'. Jenny and her mother go to the cashier to pay for the books."
    },
    {
        "num": 8,
        "title": "Playground Nearby",
        "file": "08-playground-nearby.html",
        "key": "playgroundNearby",
        "audio": "Playground Nearby.mp3",
        "text": "Mary, Amir and Sumei are neighbours. They live in the same block of flats in Bedok. Mary and Sumei both live on the eighth floor. Amir lives on the tenth floor. Every evening, the three children go to the playground near their flats. There are swings, see-saws, a climbing frame, a slide and a small sandpit at the playground. Amir loves to climb to the top of the climbing frame. Mary and Sumei like to go on the see-saw. Up and down, up and down, what fun they have!"
    }
]

# Template dari Grade 4
with open('../supp4/stories/04-hardworking-courier.html', 'r', encoding='utf-8') as f:
    template = f.read()

os.makedirs("stories", exist_ok=True)

for i, story in enumerate(stories):
    prev_page = stories[i-1]["file"] if i > 0 else ""
    next_page = stories[i+1]["file"] if i < len(stories)-1 else ""
    
    content = template
    content = content.replace("const STORY_KEY = 'courier';", f"const STORY_KEY = '{story['key']}';")
    content = content.replace("const NEXT_PAGE = '05-alice-jungle.html';", f"const NEXT_PAGE = '{next_page}';")
    content = content.replace("const PREV_PAGE = '03-may-disney.html';", f"const PREV_PAGE = '{prev_page}';")
    content = content.replace('<title>The Hardworking Courier · Grade 4</title>', f'<title>{story["title"]} · Grade 2</title>')
    content = content.replace('<h2>📖 The Hardworking Courier</h2>', f'<h2>📖 {story["title"]}</h2>')
    content = content.replace('src="../audio/The Hardworking Courier.mp3"', f'src="../audio/{story["audio"]}"')
    content = content.replace('href="../index-supp4.html"', 'href="../index-supp2.html"')
    
    old_story = "Mr. Lim is a courier and he delivers packages to many homes every day. Mr. Lim is a hardworking man and he starts work early in the morning. His job is not easy as he has to work in the rain and under the hot sun. Once, a very fierce dog chased him and he was almost bitten. Since then, he looks around whenever he hears a dog bark."
    content = content.replace(f'const originalStory = `{old_story}`;', f'const originalStory = `{story["text"]}`;')
    
    with open(os.path.join("stories", story["file"]), 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ {story['file']}")

print(f"\n🎉 {len(stories)} files created!")
