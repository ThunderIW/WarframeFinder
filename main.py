import json

import requests

warframeItems = []
with open('WarframeItem.json') as json_file:
    data = json.load(json_file)

    for items in range(0, len(data)):
        warframeItems.append(data[items]["item_name"])

planets = {"Mercury":
               ["Caloris", "Lares", "Odin", "Apollodorus","Elion", "Suisei", "Tolstoj"],
           "Venus": ["Montes", "V Prime", "Cytherean","Linea","Ishtar (Caches)"]
           }
planetsList = ["Mercury", "Venus", "Earth", "Mars", "Phobos", "Deimos", "Ceres", "Jupiter",
               "Europa", "Saturn", "Uranus"]

response = requests.get("http://drops.warframestat.us/data/all.json")
missonRewards=requests.get("http://drops.warframestat.us/data/missionRewards.json").json()

relic_list = response.json()
##print(missonRewards["missionRewards"]["Mercury"])


##print(planent_selected)
##print(relic_list["missionRewards"]["Mercury"][planent_selected[0]])


def getFarmlocation(relic: str):
    print("Item: "+relic)
    print("-----------------------------")
    for planet in planetsList:
        try:
            chosen_planet = planets.get(planet)

            ##print(chosen_planet)

            for planetNodes in chosen_planet:
                gamemode =missonRewards["missionRewards"][planet][planetNodes]['gameMode']
                rewards = missonRewards["missionRewards"][planet][planetNodes]["rewards"]
                if isinstance(rewards, list):
                    for i in range(0,len(rewards)):

                        if rewards[i]["itemName"]==relic:
                            rarity=rewards[i]["rarity"]
                            chance=rewards[i]["chance"]
                            print(f"planet: {planet} {planetNodes}\nGame mode: {gamemode}\nRarity:{rarity}\nChance:{chance}%")
                if isinstance(rewards,dict):
                    for key,values in rewards.items():
                        for v in range(0,len(values)):
                            if values[v]["itemName"]==relic:
                                chance=values[v]["chance"]
                                rarity=values[v]["rarity"]
                                print(f"Planet: {planet} {planetNodes}\nGameMode: {gamemode}\nRotation: {key}\nRarity: {rarity}\nChance:{chance}%")
            print("-----------------------------")


        except TypeError:
            pass
        except AttributeError:
            pass




def findPrimePartLocation(part: str):
    relics = relic_list["relics"]
    for relic in range(0, len(relics)):
        for rewards in relics[relic]["rewards"]:
            if rewards["itemName"] == part:
                tier = relics[relic]["tier"]
                relicName = relics[relic]["relicName"]
                state = relics[relic]["state"]
                rarity = rewards["rarity"]
                chanceOfGettingItem = rewards["chance"]
                print(part)
                print(f"Name:{tier + ' ' + relicName}\nState:{state}\nRarity:{rarity}\nChance:{chanceOfGettingItem}%")
                print("----------------------------------------------------------")



getFarmlocation("Vapor Specter Blueprint")