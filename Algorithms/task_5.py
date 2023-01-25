import requests
from pprint import pprint

def use_api():
   name = "apache/spark"
   url = f"https://api.github.com/repos/{name}"
   
   response = requests.get(url)
   if response.status_code == 200:
      with open("get_json_data.txt", encoding="utf-8", mode="w+") as file:
           data = response.json()
           file.dump(data["company"], data["id"], data["email"], data["creat_at"], data["name"],data["url"]) 
   else:
      return "Соединение не удалось"


use_api()
