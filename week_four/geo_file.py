from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="specify_your_app_name_here")
location = geolocator.geocode("15 JALAN Antinahapan 6 60000")
print(location.address)

print((location.latitude, location.longitude))

lat = location.latitude