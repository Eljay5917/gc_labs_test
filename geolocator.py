from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import math
geolocator =Nominatim(user_agent="geolocator")
#location=geolocator.geocode("koforidua")
#print(location.address)
#location2=geolocator.geocode("lagos")
#print((location.latitude,location.longitude))
#print((location2.latitude,location2.longitude))
lagos=geolocator.geocode(input("location"))
koforidua=geolocator.geocode(input("Koforidua"))
koforidua=((koforidua.latitude,koforidua.longitude))
lagos=((lagos.latitude,lagos.longitude))
print(geodesic(lagos,koforidua).miles)


