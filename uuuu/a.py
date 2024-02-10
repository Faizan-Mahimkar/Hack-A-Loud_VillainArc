import datetime
import wikipedia
import requests
import clipboard
import pyjokes
import string
import random
import time as tt
import requests
import webbrowser as wb


def speak(text):
    print(text)


    
def time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak("The current time is: " + current_time)


def date():
    date = datetime.datetime.now().strftime("%B %d, %Y")
    speak("Today's date is: " + date)


def find_doctor(location_or_specialty):
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"doctor {location_or_specialty}",
        "format": "json",
        "addressdetails": 1,
        "limit": 5  # Adjust the limit as needed
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            speak("Here are some doctors near your location:")
            for item in data:
                name = item.get("display_name", "Unknown")
                address = item.get("address", {}).get("display_name", "Unknown")
                speak(f"{name} - {address}")
        else:
            speak("No doctors found near your location.")
    else:
        speak("Error: Unable to connect to the server.")


def healthcare_info():
    speak("What healthcare information are you looking for?")
    topic = input("You: ")
    speak(f"Searching for information about {topic}.")
    # Use Wikipedia or other healthcare-related APIs to retrieve information about the specified topic
    try:
        summary = wikipedia.summary(topic, sentences=2)
        speak("According to Wikipedia: " + summary)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find information about that topic.")
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple pages with that name. Please specify your query further.")


def takeCommandText():
    return input("You: ").lower()


if __name__ == "__main__":
    speak("Hey!! My name is Jeet. I am a virtual health care chatbot. How may I assist you?")
    while True:
        query = takeCommandText()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        
        elif 'heartbreak' in query:
            wb.open('https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118')

        elif 'find' in query or 'doctor near me' in query:
            speak("Please provide your location or specify the type of doctor you're looking for.")
            location_or_specialty = input("You: ")
            find_doctor(location_or_specialty)


        elif 'disease' or 'symptoms' in query:
            healthcare_info()
        
        elif 'weather' in query:
            city = 'Thane'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=382962ca87c1d84b2159fe2425532d8f'
            
            res = requests.get(url)
            data = res.json()

            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            desp = data['weather'][0]['description']
            temp = round((temp - 32) *5/9)
            print(weather)
            print(temp)
            print(desp)
            speak(f'weather in {city} is like')
            speak('Temperature : {} degree celcius'. format(temp))
            speak('weather is {}'.format(desp))


        elif 'offline' in query:
            speak("Thank you for using the Healthcare Chatbot. Goodbye!")
            break
