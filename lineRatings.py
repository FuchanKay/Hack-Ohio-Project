import pypsa
import ieee738
from ieee738 import ConductorParams

"""
ambient will be the same for ALL conductors in a region; different RESISTANCE
For ambient temp info need: 
Ta: ambient air temp **variable
Wind velocity **
Wind angle in deg **
Time of day **
Elevation ** not included in data
Latitude
Time of day again **
Emmisivity
Absorptivity 
Wind direction (doesn't really matter)
Atmosphere description (worst case is clear)
Date

outside: MOT
"""

"""
VARIABLES TO ACCOUNT FOR LATER: 
Ta, wind velocity, wind angle, time of day, date
"""
# dictionary of ambient defaults- will be the same for all conductors in a region
ambient_defaults = {
    'Ta': 25,
    'WindVelocity': 2.0, 
    'WindAngleDeg': 90,
    'SunTime': 12,
    'Elevation': 1000,
    'Latitude': 27,
    'SunTime': 12,
    'Emissivity': 0.8,
    'Absorptivity': 0.8,
    'Direction': 'EastWest',
    'Atmosphere': 'Clear',
    'Date': '12 Jun',
    }
MOT = 75 # Maximum operating temperature of conductor in deg C
