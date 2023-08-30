import requests
api_key="ee2798328aa7160fd1a37d3ad3a29b1a"
url =f'http://api.openweathermap.org/data/2.5/weather?q=Koforidua&appid={api_key}'

get_requests=requests.get(url)
print(get_requests.json()["rain"])


