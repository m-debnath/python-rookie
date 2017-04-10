import subprocess

def main():
    str = ""
    while 1 == 1:
        str = input()
        tts(str)
        if str == "quit":
            break
        
def tts(str):
    print(str)
    str = str.replace("'", "''")
    subprocess.call(["C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", "PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + str + "');\""])

if __name__ == '__main__':
    main()