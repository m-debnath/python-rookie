import random
import subprocess
import webbrowser

def main():
    greet_req = ["hey", "hi", "hello", "sup", "oi", "good morning", "good evening", "ehllo", "hlo"]
    greet_res = ["How do you do?", "What's up?", "Hello.", "sup bro", "Greetings master."]
    thank_req = ["thank", "cheers", "thq", "thx", "thnks", "ty", "tx", "tq"]
    thank_res = ["You are welcome.", "It was my pleasure.", "No problem.", "Anything for you.", "Pleased to serve."]
    web_req = ["google", "facebook", "fb", "twitter", "idbi", "sbi", "abn", "movies", "hobby", "git", "citi", "gmail", "youtube", "yt", "router", "amazon", "shop", "xvideos", "xnxx", "pornhub", "heavyr", "youporn"]
    web_resp = ["Opening ", "Here you go, ", "Requesting ", "Loading "]
    bye_req = ["bye", "quit", "exit", "shutdown", "tata", "q", "good day", "good night", "gn"]
    bye_res = ["Goodbye.", "Have a nice one.", "See ya.", "It was a pleasure working for you.", "Catch you later.", "Word.", "Adios motherfucker!"]

    tts(random.choice(greet_res)) # Say hello

    while 1 == 1:
        resp = False
        resp1 = input("$")
        if say_response(greet_req, greet_res, resp1):
            continue
        if say_response(thank_req, thank_res, resp1):
            continue
        if web_response(web_req, web_resp, resp1):
            continue
        if say_response(bye_req, bye_res, resp1):
            break
        tts("I am sorry. I do not know about " + resp1 + ".")
  
def say_response(a, b, query):
    resp = False
    for word in a:
        if word in query:
            resp = True
            tts(random.choice(b))
    return resp

def web_response(a, b, query):
    resp = False
    sURL = "www.google.com"
    for word in a:
        if word in query:
            resp = True
            # firefox www.mozilla.com
            if word == "google":
                sURL = "www.google.com"
            if word == "facebook" or word == "fb":
                sURL = "https://www.facebook.com/"
            if word == "twitter":
                sURL = "https://twitter.com/"
            if word == "idbi":
                sURL = "https://inet.idbibank.co.in/corp/BANKAWAY?Action.RetUser.Init.001=Y&AppSignonBankId=IBKL&AppType=corporate"
            if word == "sbi":
                sURL = "https://www.onlinesbi.com/retail/login.htm"
            if word == "movies":
                sURL = "https://fmovies.se/"
            if word == "hobby":
                sURL = "http://hobbycodes.com/"
            if word == "git":
                sURL = "https://github.com/m-debnath"
            if word == "citi":
                sURL = "http://www.online.citibank.co.in/"
            if word == "gmail":
                sURL = "https://mail.google.com/mail/ca/u/0/#inbox"
            if word == "youtube" or word == "yt":
                sURL = "http://www.youtube.com/"
            if word == "router":
                sURL = "http://192.168.0.1/"
            if word == "amazon" or word == "shop":
                sURL = "http://www.amazon.in/"
            if word == "xvideos":
                sURL = "https://www.xvideos.com/"
            if word == "youporn":
                sURL = "https://www.youporn.com/"
            if word == "xnxx":
                sURL = "https://www.xnxx.com/"
            if word == "pornhub":
                sURL = "https://www.pornhub.com/"
            if word == "heavyr":
                sURL = "https://www.heavy-r.com/"
            webbrowser.open(sURL, new=2, autoraise=True)
            tts(random.choice(b) + word)
    return resp

def tts(str):
    print(str)
    str = str.replace("'", "''")
    subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + str + "');\""])

if __name__ == '__main__':
    main()