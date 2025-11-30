import requests
class Weather:
    def __init__(self, place):
        self.place = place
    def data(self,lat,lon):
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )
        response = requests.get(url)
        if response.status_code != 200:
            print("data is not available")
            return None
        data = response.json()
        current=data.get("current_weather",{})
        temp = current.get("temperature")
        wind = current.get("windspeed")
        code = current.get("weathercode")

        print(f"Temperature: {temp}°C")
        print(f"Wind Speed: {wind} km/h")
        print(f"Weather Code: {code}")

    def get_coordinates(self):
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": self.place,
            "format": "json"
        }

        response = requests.get(url, params=params, headers={"User-Agent": "MyPythonApp"})

        if response.status_code != 200:
            print("Geocoding API is having a bad day:", response.status_code)
            return -1,-1

        data = response.json()

        if not data:
            return -1,-1

        lat = data[0]["lat"]
        lon = data[0]["lon"]
        print(lat, lon)
        #print(data)

        return round(float(lat),2), round(float(lon),2)
place=input("Enter your place here: ")
d=Weather(place)
lat=d.get_coordinates()
if lat[0]==-1 or lat[1]==-1:
    print("No such place found. Maybe spell it right this time.")
else:
    d.data(lat[0],lat[1])







