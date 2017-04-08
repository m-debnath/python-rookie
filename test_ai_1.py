import random
import subprocess

def main():
    greet_req = ["hey", "hi", "hello", "sup"]
    greet_res = ["How do you do", "Whats up", "Hello", "sup bro", "Greetings master"]
    bye_req = ["bye", "quit", "exit", "shutdown", "tata"]
    bye_res = ["Goodbye, have a nice day", "Have a nice one", "See ya", "It was a pleasure working for you"]
    thank_req = ["thank", "cheers"]
    thank_res = ["You are welcome", "It was my pleasure", "No problem", "Anything for you"]
    tts(random.choice(greet_res))
    loop_run = True
    while loop_run:
        resp = False
        resp1 = input()
        for word in greet_req:
            if word in resp1:
                tts(random.choice(greet_res))
                resp = True
        for word in thank_req:
            if word in resp1:
                tts(random.choice(thank_res))
                resp = True
        for word in bye_req:
            if word in resp1:
                tts(random.choice(bye_res))
                resp = True
                loop_run = False
        if not resp:
            tts("I am sorry. I do not know about " + resp1)
  
def tts(str):
    print(str)
    subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + str + "');\""])

if __name__ == '__main__':
  main()