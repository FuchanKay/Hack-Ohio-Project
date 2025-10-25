import pypsa
import requests
import json
import map
import calc_load
import line_ratings

def get_current_temp_and_wind_speed(api_key, latitude, longitude):
    call = f"{base_url}/current.json?q={latitude},{longitude}"

    response = requests.get(call)

    table = json.loads(response.text)
        
    wind_fps = 1.4666 * table["current"]["wind_mph"]
    
    temp_and_wind = {
        "wind_speed": wind_fps,
        #temperature in celcius
        "temp": table["current"]["temp_c"],
        #date and time of when it was last updated
        "last_updated": table["current"]["last_updated"]
    }
    return temp_and_wind

base_url = "http://api.weatherapi.com/v1"
api_key = "746b28d32b274a39bac190105252510"
latitude, longitude = 40.7127281,-74.0060152

temp_and_wind = get_current_temp_and_wind_speed(api_key, latitude, longitude)

print(temp_and_wind["wind_speed"], temp_and_wind["temp"])
map.generate_map()