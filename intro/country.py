import requests
import json

print("Country Info Search")
name = input("Input the name of the country you wish to search for: ")

print(f"Results for '{name}'")
try:
    response = requests.get(f"https://restcountries.eu/rest/v2/name/{name}")
    response.raise_for_status()
    countries = response.json()
    print()
    for country in countries:
        print(country["name"])
        print("-----------------------------")
        print(json.dumps(country, indent=4))
except requests.HTTPError as e:
    print(f"Unable to get country info. Status Code: {e.response.status_code}")
