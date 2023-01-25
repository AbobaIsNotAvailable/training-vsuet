import requests
from pprint import pprint

def use_api():
   username = "spark"
   url = f"https://api.github.com/users/{username}"
   
   response = requests.get(url)
   if response.status == 200:
      with open("get_json_data.txt", encoding="utf-8", mode="w+") as file:
           file.dump(response.json())
   else:
      return "Соединение не удалось"


use_api()
