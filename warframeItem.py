import requests

warframeMarket=requests.get("https://api.warframe.market/v1/items").json()
for item in warframeMarket["payload"]["items"]:
    print(item["item_name"])

