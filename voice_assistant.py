import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that. Could you repeat?")
        except sr.RequestError:
            speak("Network error. Please check your connection.")
        except sr.WaitTimeoutError:
            speak("It seems like you didn't say anything. Please try again.")
        return None

def contains_keyword(query, keywords):
    return any(keyword in query for keyword in keywords)

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def tell_date():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today is {today}")

def search_web(query):
    speak("Searching the web...")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why was the math book sad? It had too many problems.",
        "What do you call fake spaghetti? An impasta!",
    ]
    joke = random.choice(jokes)
    speak(joke)

def set_reminder(task):
    speak(f"Reminder set for {task}. I’ll remind you soon!")

def weather_update():
    speak("Let me check the weather for you.")
    webbrowser.open("https://www.google.com/search?q=current+weather")

def system_control(action):
    if action == "shutdown":
        speak("Shutting down the system. Goodbye!")
        os.system("shutdown /s /t 1")
    elif action == "restart":
        speak("Restarting the system. See you soon!")
        os.system("shutdown /r /t 1")

def main():
    speak("Hello! How can I assist you?")
    while True:
        query = get_audio()
        if query:
            if contains_keyword(query, ["hello"]):
                speak("Hello! How can I help you?")
            elif contains_keyword(query, ["time", "what time is it"]):
                tell_time()
            elif contains_keyword(query, ["date", "what is today's date"]):
                tell_date()
            elif contains_keyword(query, ["search for", "google", "look up"]):
                search_query = query.replace("search for", "").replace("google", "").replace("look up", "").strip()
                search_web(search_query)
            elif contains_keyword(query, ["joke", "tell me a joke"]):
                tell_joke()
            elif contains_keyword(query, ["reminder", "set a reminder"]):
                speak("What should I remind you about?")
                task = get_audio()
                if task:
                    set_reminder(task)
            elif contains_keyword(query, ["weather", "weather update"]):
                weather_update()
            elif contains_keyword(query, ["shutdown", "shut down"]):
                system_control("shutdown")
                break
            elif contains_keyword(query, ["restart"]):
                system_control("restart")
                break
            elif contains_keyword(query, ["stop", "exit", "thank you", "thanks"]):
                speak("You're welcome! Goodbye!")
                break
            else:
                speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
