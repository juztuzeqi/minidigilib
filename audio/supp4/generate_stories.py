#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# ==================== DATA 17 CERITA ====================
stories = [
    {
        "num": 1,
        "title": "The Tan Family's Chinese New Year",
        "file": "01-tan-family.html",
        "key": "tanFamily",
        "audio": "The Tan's family Chinese New Year.mp3",
        "text": "The Tan family is celebrating Chinese New Year. They are inviting their neighbours, Mr and Mrs Lee, to their house. Mrs Tan has already cleaned and tidied their house. She bought cookies and sweets for her guests. Jane and John Lim are happy because they will receive red packets soon. The family is always busy during the Chinese New Year period."
    },
    {
        "num": 2,
        "title": "Meet A Liang",
        "file": "02-meet-liang.html",
        "key": "meetLiang",
        "audio": "Meet A Liang.mp3",
        "text": "Hi! My name is A Liang. I am eleven years old. I go to school in the morning. I have a younger sister. I like to watch cartoons when I am free. I swim every Sunday and I fly kites with my family every week. I like to eat burgers and drink orange juice. Sometimes, I help my mother to clean the kitchen."
    },
    {
        "num": 3,
        "title": "May's Trip to Disneyland",
        "file": "03-may-disney.html",
        "key": "mayDisney",
        "audio": "May's Trip to Disneyland.mp3",
        "text": "May was excited. Her family was going on a holiday to Disneyland USA. It took them eighteen hours to get to the USA. May was bored on the airplane. Fortunately, the flight attendant gave her and her brother some books to read and a board game to play. When they reached the USA, they took a taxi to their hotel. They stayed at that hotel for five days. In Disneyland, they went to an amusement park. There were many kinds of rides. There were roller coaster rides, Viking boat rides and rides on the ferris wheel. She also met many different cartoon characters and took photographs with them. May enjoyed herself very much. Soon, it was time to go home. May was sad, but she also wanted to come back to Singapore."
    },
    {
        "num": 4,
        "title": "The Hardworking Courier",
        "file": "04-hardworking-courier.html",
        "key": "courier",
        "audio": "The Hardworking Courier.mp3",
        "text": "Mr. Lim is a courier and he delivers packages to many homes every day. Mr. Lim is a hardworking man and he starts work early in the morning. His job is not easy as he has to work in the rain and under the hot sun. Once, a very fierce dog chased him and he was almost bitten. Since then, he looks around whenever he hears a dog bark."
    },
    {
        "num": 5,
        "title": "Alice's Fall in the Jungle",
        "file": "05-alice-jungle.html",
        "key": "aliceJungle",
        "audio": "Alice's Fall in the Jungle.mp3",
        "text": "One day, Alice was picking flowers in a jungle when she fell into a big hole. She shouted for help, but nobody came to help her. She could hear the animals making a lot of noise. She also felt thirsty and hungry. Alice was so frightened that she began to cry. Suddenly, she heard someone talking. It was her father! He had come to rescue her. Alice was very happy to see him. Soon, they were on their way home."
    },
    {
        "num": 6,
        "title": "A New Home in Sunshine Neighbourhood",
        "file": "06-sunshine-neighbourhood.html",
        "key": "sunshine",
        "audio": "A New Home in Sunshine Neighbourhood.mp3",
        "text": "Mr Ng, a factory worker, moved to Sunshine Neighbourhood last week. He and his family are happy there. Andy and Mike like their new school. They take five minutes to walk to school. The library is not far away either. \"We can read more now,\" Mike tells his mother. \"Good,\" his mother says. \"Can we play in the playground, Father?\" Andy asks. \"It's safe. The police post is in front of it.\" \"I know,\" their father says. \"But don't play there by yourselves. Ask some of the children in the neighbourhood to play with you. We have friendly neighbours.\" \"Aren't we lucky?\" Mike says."
    },
    {
        "num": 7,
        "title": "Raju's Family",
        "file": "07-raju-family.html",
        "key": "rajuFamily",
        "audio": "Raju's Family.mp3",
        "text": "Raju's family lives in Jurong. His father is a taxi-driver and his mother is a housewife. Raju has a sister and a brother. Raju's family goes to the park every Sunday. Sometimes, Raju lets his pet dog run around freely. On Raju's birthday, his mother gave him a toy car. His grandmother baked him a cake. Raju's family will be going on holiday in Malaysia next week. His cousin, Samy, is joining them."
    },
    {
        "num": 8,
        "title": "A Lesson Learned",
        "file": "08-lesson-learned.html",
        "key": "lessonLearned",
        "audio": "A Lesson Learned.mp3",
        "text": "Eng Keat and Henry are from the same class. One day, as they are walking past an orchard, Henry sees some ripe rambutans and wants to steal them. Eng Keat warns Henry that stealing is wrong. It will bring them trouble. Henry does not listen to him. While Henry is climbing the rambutan tree, the owner of the plantation, Mr Lee, comes out. He sees Henry on the tree and immediately shouts at him. Henry tries to escape but falls from the tree. He breaks his leg. Eng Keat takes him to the hospital. Now Henry has learnt that it does not pay to steal."
    },
    {
        "num": 9,
        "title": "The Filial Daughter",
        "file": "09-filial-daughter.html",
        "key": "filialDaughter",
        "audio": "The Filial Daughter.mp3",
        "text": "Meizhen sells vegetables in a market. She wakes up at five o'clock every morning. She walks to the market as it is near her house. After cleaning the stall, she arranges the vegetables nicely. Many people like to buy vegetables from her because they are cheap and fresh. By eleven o'clock, all her vegetables are sold. Meizhen then rushes home to look after her sick and old mother. She cooks lunch for her mother. Meizhen's mother is glad to have such a filial daughter."
    },
    {
        "num": 10,
        "title": "Walking to School",
        "file": "10-walking-school.html",
        "key": "walkingSchool",
        "audio": "Walking to School.mp3",
        "text": "Every morning, Bala goes to school with his sister. They walk to school together. Bala and his sister are in the same school. Bala is in Primary Five and his sister is in Primary One. Both of them like to go to school. They have many friends there. They like to play with their friends. Bala likes to play football but his sister likes skipping."
    },
    {
        "num": 11,
        "title": "Mrs Sim Goes to Market",
        "file": "11-mrs-sim-market.html",
        "key": "mrsSim",
        "audio": "Mrs Sim Goes to Market.mp3",
        "text": "Mrs Sim goes to the market every morning after her breakfast. She eats two slices of bread and drinks a cup of coffee for her breakfast. After that, she carries a basket and walks to the market with her grandson. At the market, she usually buys fish, some meat and vegetables. She usually spends about half an hour in the market. Her grandson helps her to carry the heavy basket home."
    },
    {
        "num": 12,
        "title": "The Strange Soup",
        "file": "12-strange-soup.html",
        "key": "strangeSoup",
        "audio": "The Strange Soup.mp3",
        "text": "Mark is drinking a bowl of vegetable soup. The soup is very hot and Mark has to drink it slowly. He drinks a spoonful of it and finds that it tastes strange. He stops drinking and tells his mother about it. Mrs Wong tastes a little of it. She realizes that the soup is tasteless because she has forgotten to put salt in it."
    },
    {
        "num": 13,
        "title": "Flying Kites",
        "file": "13-flying-kites.html",
        "key": "flyingKites",
        "audio": "Flying Kites.mp3",
        "text": "The day is windy and cool. Baowen and Baomin are playing in the garden. They are flying kites. Baomin does not know how to fly a kite, so Baowen shows him how to do it. Their sister comes to the garden. She wants to fly kites too. Her brothers do not want her to join in. She walks away angrily."
    },
    {
        "num": 14,
        "title": "Lost on the Way Home",
        "file": "14-lost-way-home.html",
        "key": "lostWayHome",
        "audio": "Lost on the Way Home.mp3",
        "text": "Peihua and Peilian go to a bookshop near their school. They want to buy some coloured pencils. On their way home, they stop at a bakery. Peihua buys a chicken pie. Peilian wants a chicken pie too but she has only fifty cents. \"Do you want a slice of fruit cake instead?\" the salesgirl asks her. \"Yes, please,\" Peilian says. \"I'll come back and buy a chicken pie tomorrow.\" The sisters walk past a bank and a library. Then Peihua says, \"I don't think this is the way to our house, Peilian.\" \"You're right, Peihua. It isn't. We're lost!\" Peilian says. The girls stop at a police post. Peilian gives a policeman their address. He takes the girls to their house. \"Thank you for the ride,\" the girls say."
    },
    {
        "num": 15,
        "title": "Recess Time Fun",
        "file": "15-recess-time.html",
        "key": "recessTime",
        "audio": "Recess Time Fun.mp3",
        "text": "It is time for recess. The children talk loudly as they walk out of the classroom. Janet, Lily and Peihua go to the tuckshop to buy some food. They eat their food quickly. After that, they play hide-and-seek in the field. They enjoy themselves very much. Soon, the bell rings. The children stop playing at once. They walk back to their classroom."
    },
    {
        "num": 16,
        "title": "Linda's English Class",
        "file": "16-linda-english.html",
        "key": "lindaEnglish",
        "audio": "Linda's English Class.mp3",
        "text": "Linda is in Elementary English class. Fanny, Nunun and Namik are her classmates. Her teacher is Mr Herry. She likes to buy them food when she comes to class. She is very busy every day because she has to fetch her daughters before and after school. She hopes she will be able to speak English soon."
    },
    {
        "num": 17,
        "title": "Jan's Stage Fright",
        "file": "17-jan-stage.html",
        "key": "janStage",
        "audio": "Jan's Stage Fright.mp3",
        "text": "Jan waited behind the stage for her turn to dance in the school concert. Her knees felt wobbly and her legs were shaking like jelly. There were butterflies in her stomach and goose pimples on the skin of her arms. Her chest felt so tight that she had to breathe slowly. There were tiny drops of perspiration on Jan's face. She licked her dry lips and wiped her wet eyes gently. Her whole body felt as if it was about to collapse. Suddenly, Jan heard her teacher announcing the title of her dance. It was her turn to face the crowd."
    }
]

# ==================== TEMPLATE HTML ====================
def get_template(story, prev_page, next_page):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{story["title"]} · Grade 4</title>
  <style>
    * {{ box-sizing: border-box; }}
    body {{ font-family: 'Courier New', monospace; background: #f5f5dc; margin: 10px; text-align: center; min-height: 100vh; }}
    .container {{ max-width: 650px; margin: 0 auto; }}
    h2 {{ color: #2c3e50; margin: 10px 0; font-size: 1.3rem; }}
    .mode-tab {{ display: flex; gap: 5px; margin: 15px 0; }}
    .mode-btn {{ flex: 1; padding: 12px 8px; background: #e2e8f0; border: none; border-radius: 40px; font-weight: bold; cursor: pointer; font-size: 0.9rem; }}
    .mode-btn.active {{ background: #3b82f6; color: white; }}
    .story-box {{ background: white; border: 3px solid #333; border-radius: 20px; padding: 20px; margin: 15px 0; text-align: left; font-size: 16px; line-height: 1.6; max-height: 350px; overflow-y: auto; }}
    textarea {{ width: 100%; height: 200px; padding: 15px; font-size: 16px; border: 2px solid #333; border-radius: 20px; font-family: 'Courier New', monospace; margin: 15px 0; }}
    .check-btn {{ padding: 15px 30px; background: #2ecc71; color: white; border: none; border-radius: 40px; font-weight: bold; cursor: pointer; font-size: 18px; width: 100%; }}
    .nav-btn {{ padding: 12px 20px; background: white; border: 2px solid #7f8c8d; border-radius: 40px; cursor: pointer; font-weight: bold; margin: 5px; }}
    .back-link {{ display: block; margin: 20px auto; padding: 12px; background: white; border-radius: 40px; text-decoration: none; color: #333; border: 1px solid #cbd5e1; }}
    .hidden {{ display: none; }}
    .feedback {{ margin: 15px 0; font-weight: bold; font-size: 1.2rem; }}
    .diff-correct {{ background: #d4edda; color: #155724; padding: 2px 4px; border-radius: 4px; }}
    .diff-wrong {{ background: #f8d7da; color: #721c24; padding: 2px 4px; border-radius: 4px; text-decoration: line-through; }}
    .diff-missing {{ background: #fff3cd; color: #856404; padding: 2px 4px; border-radius: 4px; }}
  </style>
</head>
<body>
<div class="container">
  <h2>📖 {story["title"]}</h2>
  
  <div class="mode-tab">
    <button class="mode-btn active" data-mode="read">👂 Listen & Read</button>
    <button class="mode-btn" data-mode="write">✏️ Listen & Write</button>
    <button class="mode-btn" data-mode="check">✅ Self-Check</button>
  </div>

  <div id="readMode">
    <audio controls src="../audio/{story["audio"]}" style="width:100%; margin:10px 0;"></audio>
    <div class="story-box" id="storyText"></div>
    <div style="display: flex; gap: 10px; margin-top: 10px;">
      <button class="nav-btn" id="prevStoryBtn" style="flex:1;">◀ Prev</button>
      <button class="nav-btn" id="nextStoryBtn" style="flex:1;">Next ▶</button>
    </div>
  </div>

  <div id="writeMode" class="hidden">
    <audio controls src="../audio/{story["audio"]}" style="width:100%; margin:10px 0;"></audio>
    <textarea id="dictationInput" placeholder="Type the story as you hear it..."></textarea>
    <button class="check-btn" id="saveDictation">💾 Save & Check</button>
    <p style="color:#7f8c8d; margin-top:10px; font-size:0.9rem;">💡 Tip: Play → Pause → Write → Repeat</p>
  </div>

  <div id="checkMode" class="hidden">
    <div class="story-box" style="max-height: none;">
      <p><strong>📝 Original:</strong></p>
      <p id="originalTextDisplay" style="background:#f1f5f9; padding:10px; border-radius:10px;"></p>
      <p><strong>✏️ Yours:</strong></p>
      <p id="userTextDisplay" style="background:#fef3c7; padding:10px; border-radius:10px;"></p>
      <p><strong>🔍 Differences (highlighted):</strong></p>
      <p id="diffDisplay" style="background:white; padding:10px; border-radius:10px; border:1px solid #cbd5e1;"></p>
    </div>
    <div class="feedback" id="checkFeedback"></div>
    <button class="nav-btn" id="backToWrite">← Back to Write</button>
  </div>
  
  <a class="back-link" href="../index.html">⬅ Back to Story List</a>
</div>

<script>
  const STORY_KEY = '{story["key"]}';
  const NEXT_PAGE = '{next_page}';
  const PREV_PAGE = '{prev_page}';
  
  const originalStory = `{story["text"]}`;

  document.getElementById('storyText').innerHTML = originalStory.replace(/\\n/g, '<br>');
  document.getElementById('originalTextDisplay').innerHTML = originalStory.replace(/\\n/g, '<br>');

  function generateDiff(original, user) {{
    const origWords = original.split(/\\s+/);
    const userWords = user.split(/\\s+/);
    let diffHtml = '';
    for (let i = 0; i < origWords.length; i++) {{
      if (i < userWords.length) {{
        if (origWords[i].toLowerCase() === userWords[i].toLowerCase()) {{
          diffHtml += `<span class="diff-correct">${{origWords[i]}}</span> `;
        }} else {{
          diffHtml += `<span class="diff-wrong" title="You wrote: ${{userWords[i]}}">${{origWords[i]}}</span> `;
        }}
      }} else {{
        diffHtml += `<span class="diff-missing">${{origWords[i]}}</span> `;
      }}
    }}
    if (userWords.length > origWords.length) {{
      for (let i = origWords.length; i < userWords.length; i++) {{
        diffHtml += `<span class="diff-wrong" title="Extra word">${{userWords[i]}}</span> `;
      }}
    }}
    return diffHtml;
  }}

  document.querySelectorAll('.mode-btn').forEach(btn => {{
    btn.addEventListener('click', function() {{
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      document.getElementById('readMode').classList.add('hidden');
      document.getElementById('writeMode').classList.add('hidden');
      document.getElementById('checkMode').classList.add('hidden');
      if (this.dataset.mode === 'read') {{
        document.getElementById('readMode').classList.remove('hidden');
      }} else if (this.dataset.mode === 'write') {{
        document.getElementById('writeMode').classList.remove('hidden');
        const saved = localStorage.getItem(STORY_KEY);
        if (saved) document.getElementById('dictationInput').value = saved;
      }} else if (this.dataset.mode === 'check') {{
        showComparison();
        document.getElementById('checkMode').classList.remove('hidden');
      }}
    }});
  }});

  function showComparison() {{
    const saved = localStorage.getItem(STORY_KEY) || '';
    document.getElementById('userTextDisplay').innerHTML = saved.replace(/\\n/g, '<br>') || '(No writing yet)';
    if (!saved) {{
      document.getElementById('diffDisplay').innerHTML = '<em>No writing to compare.</em>';
      document.getElementById('checkFeedback').textContent = '';
      return;
    }}
    const diffHtml = generateDiff(originalStory, saved);
    document.getElementById('diffDisplay').innerHTML = diffHtml;
    const origWords = originalStory.split(/\\s+/).length;
    const correctCount = (diffHtml.match(/diff-correct/g) || []).length;
    const percent = Math.round((correctCount / origWords) * 100);
    if (percent === 100) {{
      document.getElementById('checkFeedback').innerHTML = '🎉 Perfect! 100% match! Excellent work!';
      document.getElementById('checkFeedback').style.color = '#27ae60';
    }} else if (percent >= 80) {{
      document.getElementById('checkFeedback').innerHTML = `👍 Good job! ${{percent}}% match. Keep practicing!`;
      document.getElementById('checkFeedback').style.color = '#e67e22';
    }} else {{
      document.getElementById('checkFeedback').innerHTML = `📝 ${{percent}}% match. Listen again and try again.`;
      document.getElementById('checkFeedback').style.color = '#e74c3c';
    }}
  }}

  document.getElementById('saveDictation').addEventListener('click', function() {{
    const text = document.getElementById('dictationInput').value.trim();
    localStorage.setItem(STORY_KEY, text);
    document.querySelector('[data-mode="check"]').click();
  }});

  document.getElementById('backToWrite').addEventListener('click', function() {{
    document.querySelector('[data-mode="write"]').click();
  }});

  document.getElementById('prevStoryBtn').addEventListener('click', function() {{
    if (PREV_PAGE) window.location.href = PREV_PAGE;
  }});
  
  document.getElementById('nextStoryBtn').addEventListener('click', function() {{
    if (NEXT_PAGE) window.location.href = NEXT_PAGE;
  }});

  const saved = localStorage.getItem(STORY_KEY);
  if (saved) document.getElementById('dictationInput').value = saved;
</script>
</body>
</html>'''

# ==================== GENERATE FILES ====================
os.makedirs("stories", exist_ok=True)

for i, story in enumerate(stories):
    prev_page = stories[i-1]["file"] if i > 0 else ""
    next_page = stories[i+1]["file"] if i < len(stories)-1 else ""
    
    html_content = get_template(story, prev_page, next_page)
    
    filepath = os.path.join("stories", story["file"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"✅ Generated: {story['file']}")

print(f"\n🎉 Done! {len(stories)} files created in 'stories/' folder.")
