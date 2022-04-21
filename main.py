import requests
import os
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")

geo = OpenCageGeocode(KEY)


iss_api = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_api.raise_for_status()

data = iss_api.json()["iss_position"]

lng = data["longitude"]
lat = data["latitude"]
location = geo.reverse_geocode(lat, lng, no_annotations=1, pretty=1)
details = location[0]['components']

if details['_type'] == 'body_of_water':
	print(f"The ISS is currently over {details['body_of_water']}")
elif details['country'] == 'United States':
	print(f"The ISS is currently over {details['state']}")
else:
	print(f"The ISS is currently over {details['country']}")
