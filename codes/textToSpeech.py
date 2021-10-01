# IMPORTING MODULE
import pyttsx3

# INITIALIZING AND SETTING PROPERTIES
eng = pyttsx3.init()
# print(eng.getProperty("rate"))
eng.setProperty("rate", 125)
voices = eng.getProperty("voices")

while 1:
    text = input("Enter the text u want to hear: ")
    voiceChoice = int(input("\nPlease select the gender of the u want to hear\n1.Male\n2.Female\n"))
    eng.setProperty("voice", voices[voiceChoice-1].id)
    eng.say(text)
    eng.runAndWait()
    run = input("Do You Want To Run It Again? (y/n)")
    if run == "n":
        break
