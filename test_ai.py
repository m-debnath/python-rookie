# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    resp = ""
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            if word == "sup":
                resp = GREETING_RESPONSES[0]
            elif word == "hi" or word == "hello":
                resp = GREETING_RESPONSES[1]
            elif word == "greetings":
                resp = GREETING_RESPONSES[2]
            elif word == "what's up":
                resp = GREETING_RESPONSES[3]
            return resp
