import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import openai

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voice[1].id)
engine.setProperty('voice', voice[1].id)

openai.api_key = "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"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    



#greating 
def wishMe():  
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")

        else:
            speak("Good Evening!")

        speak("i am your assistance sir. Please tell me how may I help you")




# command handling funcation
def takecommand():  
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        audio = r.listen(source,0,8)
   
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("say that again please...")
        return "None"
    return query
        

if __name__ == "__main__":
    wishMe()

    conversation = ""
 

  
  
    # user command 
    while True:  
        query = takecommand().lower()

        # query for wikipedia search eg: sarhu khna according to wikipedia
        if 'wikipedia' in query: 
            speak('Searching Wilipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        # query for open youtube
        elif 'open youtube' in query: 
            speak("opening youtube sir....")
            webbrowser.open("youtube.com")


        # query for open w3 school
        elif 'open w3 school' in query: 
            speak("opening w3school sir....")
            webbrowser.open("w3schools.com")


        # query for open github
        elif 'open github' in query:
            speak("opening github sir....")
            webbrowser.open("https://github.com/")


        # query for exit
        elif 'exit' in query:
            speak("okay sir")
            break
            

     