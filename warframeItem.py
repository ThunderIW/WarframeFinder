import requests
import json
f=open("WarframeItem.txt","w")

warframeMarket=requests.get("https://api.warframe.market/v1/items").json()
with open("WarframeItem.json","w") as outfile:
    json.dump(warframeMarket["payload"]["items"],outfile)




