import requests


get_data = requests.get('https://ipinfo.io/')

data_loc = get_data.json()
# print(data_loc)

city_d = data_loc['city']

location_la_lo = data_loc['loc'].split(',')
latitude = location_la_lo[0]
longitude = location_la_lo[1]
ip = data_loc['ip']

print("Latitude : ", latitude)
print("Longitude : ", longitude)
print("City : ", city_d)
print("Current IP",ip)