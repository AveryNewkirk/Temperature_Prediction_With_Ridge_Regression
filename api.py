from dotenv import load_dotenv
import os
import requests

load_dotenv()



    
##returns the current min and max temp for the charlotte area 
def real_time_temp_data():
    key = os.getenv('API_KEY')
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    city = 'charlotte'
    units = 'imperial'


    url = BASE_URL + "appid=" + key + "&q=" + city + "&units=" + units


    response = requests.get(url).json()
    
    important = response['main']    

    temp_min = int(important['temp_min'])
    temp_max = int(important['temp_max'])

    return temp_min, temp_max


    


