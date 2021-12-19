import requests
from pprint import pprint
import folium
from geopy.distance import distance

BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'
postcode = 'E1 6AN'
zipcode = '2601'
response = requests.get(f"{BASE_URL}&postalcode={postcode}")
response_zipcode = requests.get(f"{BASE_URL}&postalcode={zipcode}")
response_zipcode_data = response_zipcode.json()
latitude_it = response_zipcode_data[0].get('lat')
longitude_it = response_zipcode_data[0].get('lon')


data = response.json() #LONDON
latitude = data[0].get('lat')
longitude = data[0].get('lon')

print(latitude, longitude)
print(latitude_it, longitude_it)

print(response_zipcode_data)

location_london = float(latitude), float(longitude)
location_italy = float(latitude_it), float(longitude_it)

m_london = folium.Map(location=location_london,  width = 800, height= 400)
m_italy = folium.Map(location= location_italy)

folium.Marker(location_london, popup="London").add_to(m_london)
folium.Marker(location_italy, popup= "Italy").add_to(m_london)
folium.PolyLine((location_london, location_italy)).add_to(m_london)
m_london.save('map.html')

km = distance(location_london, location_italy)
miles = distance(location_london, location_italy).miles

print(km)
print(miles, "miles")

