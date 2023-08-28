
from pyowm import OWM

api_key="ee2798328aa7160fd1a37d3ad3a29b1a"

own =OWM(api_key)

mgr = own.weather_manager()

observation=mgr.weather_at_place("Tokyo,JPN")

w=observation.weather

wind =w.wind()
humidity= w.humidity

print(f"wind:{wind}\nHumidity:{humidity}")

