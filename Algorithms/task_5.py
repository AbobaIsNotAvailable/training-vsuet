import requests
import json
from pprint import pprint

def use_api():
   name = "apache/spark"
   url = f"https://api.github.com/repos/{name}"
   
   response = requests.get(url)
   if response.status_code == 200:
      with open("get_json_data.txt", encoding="utf-8", mode="w+") as file:
           data = response.json()


           data_items = {
               "data": {
                  "id": data["id"],
                  "created_at": data["created_at"],
                  "name": data["name"],
                  "url": data["url"],
               }
           }

           json.dump(data_items, file)

   else:
      return "Соединение не удалось"


use_api()
