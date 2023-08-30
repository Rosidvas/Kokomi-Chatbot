
import nltk
import random
from template import response_templates
from template import intent_templates
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')  # Download the necessary tokenizer data
nltk.download('averaged_perceptron_tagger')

def get_Keywords(sentence):
    words = word_tokenize(sentence)
    print("Tokenized words:", words)
    return words

def get_intent(keywords):

    intent_scores = {intent: 0 for intent in intent_templates}

    for word in keywords:
        for intent, intent_keywords in intent_templates.items():
            if word.lower() in intent_keywords:
                intent_scores[intent] += 1

    max_score = max(intent_scores.values())
    most_probable_intent = [intent for intent, score in intent_scores.items() if score == max_score]
    
    #prints the scores
    print("Intent Scores:")
    for intent, score in intent_scores.items():
        print(f"{intent}: {score}")

    if max_score == 0:
        return 'unknown_intent'
    
    return most_probable_intent[0] if most_probable_intent else 'unknown_intent'

def get_Response(intent, username):
    if intent in response_templates:
        response_list = response_templates[intent]
        response = random.choice(response_list).format(user=username)

    else:
        response_list = response_list['unknown_intent']
        response = random.choice(response_list).format(user="Developer")

    return response

def analyze_Message(username, message):


    keywords = get_Keywords(message)
    if "Kokomi" in keywords:
        intent = get_intent(keywords)
        response = get_Response(intent, username)
    
    else:
        return False
    
    return response
