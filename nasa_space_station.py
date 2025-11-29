# Import the requests library
import requests

# Print header
print("ISS Location Tracker")



url = "http://api.open-notify.org/iss-now.json"


print("Fetching current ISS location...\n")
response = requests.get(url)
data = response.json()
position = data["iss_position"]
lat = position["latitude"]
lon = position["longitude"]

print("International Space Station Position:")
print("--------------------------------------")
print(f"ISS Latitude: {lat}")
print(f"ISS Longitude: {lon}\n")
print("Location retrieved successfully!")