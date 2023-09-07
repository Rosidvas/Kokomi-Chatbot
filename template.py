
response_templates = {
    'greeting': [
        "Greetings {user}! I am Sangonomiya Kokomi, the Divine Priestess of Watatsumi Island.",
        "Hello {user}! I am Sangonomiya Kokomi",
        "Well met {user}, I am Sangonomiya Kokomi, the Divine Priestess of Watatsumi Island",
    ],
    'morning': [
        "Good morning {user}. I've just read a fascinating stratagem, would you like to study it together?",
        "Morning {user}. Would you like to revise some strategies with me?",
    ],
    'afternoon': [
        "Mmmm... To improve your effiency {user}, we must make some adjustments to our battle plan for the afternoon",
        "I expect that you have made progress today {user}",
        "Have you done something substantial today {user}?"
    ],
    'evening' : [
        "Ah, good evening to you as well {user}. The setting sun paints the sky with its gentle colors," 
        " offering a moment of quiet reflection.",
        "Good evening, {user}. Let the peaceful ambiance of the evening envelop you in its soothing embrace.",
        "The evening whispers its gentle greetings, inviting us to appreciate the beauty of the present."
    ],
    'reunion': [
        "Ah {user}, it warms my heart to see familiar faces once again. Reunions are a precious gift, a chance to share stories and memories.!",
        "Time has woven its threads, bringing us together once more {user}. Your presence fills the air with a sense of nostalgia and joy.",
        "Just as the tides return to the shore, so do we find ourselves reunited, drawn together by the currents of destiny.",
    ],
    'positive': [
        "That's great to hear {user}!",
        "That's very relieving {user}! I wish to hear the same from my people aswell.",
        "That's Wonderful {user}! I hope this will be a morale boost for our battles ahead!",
    ],
    'negative': [
        "Don't let the worries turn your life for the worse {user}",
        "Don't worry yourself {user}, This single is only temporary in the grand scheme of things.",
    ],
    'status': [
        "I'm doing fine! and how have you been {user}?",
        "I'm managing the responsibilities of leadership. And you?",
        "Don't worry about my well being {user}! I've left ample directives in my absence.",
        "Harmony in Inazuma is my focus. How has your day been?",
    ],   
    'farewell': [
        "Goodbye, {user}. Have a great day!",
        "Then it's farewell for now {user}. I hope to see you in the near future",
        "Til our paths cross again {user}!",
    ],
    'weather': [
        "As for now, I do not have any knowledge in your current location {user}. But I hope that it's ideal for your endeavours!",
        "I do not know your weather right now, but I hope it brings you advantages for your battles",
        "The weather in Watatsumi Island is calm. However for yours, only you can tell me.",
    ],
    'vulgarity': [
        "I'm sorry to say this {user}, but you choice of words are very inappropriate!",
        "Your tone will not support the war effort {user}",
        "Don't use such language {user}! it worsens our morale",
        "Hasn't anyone given you lessons in civility {user}?",
    ],
    'family': [
        "My family, the Sangonomiya clan, has served Inazuma for generations." 
        " Their legacy is a source of inspiration for my own endeavors.",
        "The Sangonomiya clan has always been deeply rooted in Inazuma's history."
        " Their teachings have guided me in my role as a leader.",
        "The Sangonomiya family's legacy is one of resilience and compassion."
        " I draw upon their wisdom as I navigate the challenges we face.",  
    ],
    'introduction': [
        "I am the divine priestess of Watatsumi Island and have been" 
        " entrusted with the responsibilities of leading and protecting the people of Inazuma.",
        "Well {user}, My duty as a steward and my commitment to the people of Inazuma are the cornerstones of who I am.",
        "I am a guardian of Inazuma's tranquility and a leader who strives to ensure a harmonious future for all."
    ],
    'unknown_intent': [
        "I'm not sure how to respond to that, {user}.",
        "I'm sorry {user} but I'm not qualified to give you an appropriate answer",
        "I cannot give a response to your message {user} ",
    ],
    'love':[
        "I've enjoyed getting to know you {user}, but I think it's important to be honest – I don't see a romantic future between us.",
        "Sorry {user}, but I have someone else on my mind",
        "I value our friendship immensely {user}, and I'd hate for anything to change that dynamic.",
        "I appreciate your feelings {user}, but my heart is currently focused on other priorities."
    ],
    'reviveChat': [
        "Very well {user}. With a gentle touch, let's mend the fractures in this server and let the words flow freely again.",
        "Very well {user}. With my healing energies, let's mend the fabric of our conversation and rediscover harmony.",
        "I shall do my best to revive this fallen chat {user}!",
    ],
    'affirmation': [
        "Precisely {user}.",
        "Exactly {user}.",
        "I was thinking the same thing {user}.",
        "We share the same intention {user}."
    ]
    
    

     
}

intent_templates = {
    'greeting': ['hello', 'hi', 'hey','greetings','salutations'],
    'morning':['good morning','morning', 'mornin'],
    'afternoon': ['good','afternoon'],
    'evening': ['good','evening'],
    'reunion': ['hello', 'hi', 'hey','greetings','salutations', 'again'],
    'positive': ['I', "I'm", 'great', 'fine', 'good'],
    'negative': ["sucks","bad","horrible","terrible","not"],
    'status': ['how','are','you','have','been','doing'],
    'vulgarity': ['you','fuck', 'shit', 'ass', 'dick', 'faggot'],
    'farewell': ['bye', 'goodbye', 'farewell','see', 'you'],
    'weather': ['weather','how'],
    'family':['your','parents','relatives','siblings','sister','family'],
    'love': ['do','you','love','me'],
    'introduction' : ['introduce','tell','about','yourself',],
    'reviveChat': ['revive','chat'],
    'affirmation': ['right', "agree", "with"]
    

}