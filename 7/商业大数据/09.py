import openweather
from datetime import datetime

# create client
ow = openweather.OpenWeather('3f14d26ebe5502a831e98067ae851b99')

# find weather stations near me
stations = ow.find_stations_near(
    7.0,  # longitude
    50.0, # latitude
    100   # kilometer radius
)