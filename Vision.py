import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
1
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speak (audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")

    else:
        speak("good evening!")

    speak("I am vision. so whats your plan")        

def takeCommand():
    # It takes input from the user and returns string output
    
    print("Do you want to give command via text or speech?")
    speak("Do you want to give command via text or speech?")
    print("1. Text")
    print("2. Speech")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # Text input
        query = input("Enter your command: ").lower()
    elif choice == '2':
        # Speech input
        r = sr.Recognizer()
        with sr.Microphone() as source: 
            print("I Am Listening...")
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = r.listen(source)

        try:
            print("Wait A Minute...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said: {query}\n")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            speak("Sorry, I couldn't understand what you said.")
            return "None"

        except sr.RequestError:
            print("Sorry, there was an issue with the speech recognition service.")
            speak("Sorry, there was an issue with the speech recognition service.")
            return "None"
    else:
        print("Invalid choice.")
        return "None"

    return query
 
if __name__ == "__main__":
    wishMe()
    while True:# or if 1 if like you want vision to run only one time 
        query = takeCommand().lower()

        #logic for executing task based on query
        #to search something from wikipedia say ________ According to wikipedia
        if 'wikipedia' in query:
            speak('Let me check...')
            query = query.replace("wikipedai", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to my Knolodge")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            break 

        elif 'hello' in query:
            speak("Hi there how are you")
            
        elif 'vision' in query:
            speak("My aim is to help the people on every level , right now i am a smaller version of myself later i will be updated. this is the reason i was created.")



        elif 'how are you' in query:
            speak("I am fine , Nice to meet you.") 

        elif 'open google' in query:
            webbrowser.open("www.google.com")
            break  

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'open insta' in query:
            webbrowser.open("www.instagram.com")
            break

        elif 'open wix' in query:
            webbrowser.open("www.wix.com")
            break
            
        elif 'open spotify' in query:
            webbrowser.open("www.spotify.com")
            break

        elif 'open gmail' in query:
            webbrowser.open("www.gamil.com")
            break

        elif 'play music' in query:
            music_dir = 'C:\\Users\\ASUS\\Desktop\\xxx\\songs\\fav songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            break 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            break
        
        elif 'open game' in query:
            gamePath = "C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam"
            os.startfile(gamePath)
            break

        elif 'bye' in query:
            speak("bye bye , let me sleep now")
            exit
            print("Sayonara")
            speak("sayonara")
            break
        
            

      
