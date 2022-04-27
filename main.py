import requests
planets={"Mercury":
             ["Caloris","Lares","Odin","Apollodorus",
                    "Elion","Suisei","Tolstoj"],
         "Venus":["Montes","V Prime","Cytherean"],
         }
planetsList=["Mercury","Venus","Earth","Mars","Phobos","Deimos","Ceres","Jupiter",
             "Europa","Saturn","Uranus"]


response=requests.get("http://drops.warframestat.us/data/all.json")

relic_list=response.json()

##print(planent_selected)
##print(relic_list["missionRewards"]["Mercury"][planent_selected[0]])



def getFarmlocation(relic: str):

    print(f"ItemName:{relic}")

    for planet in planetsList:
        try:
            chosen_planet=planets.get(planet)
            ##print(planet)
            ##print(chosen_planet)
            for planetNodes in chosen_planet:
                gamemode=relic_list["missionRewards"][planet][planetNodes]['gameMode']
                rewards=relic_list["missionRewards"][planet][planetNodes]["rewards"]

                if len(rewards["A"])!=0:
                    for infoA in rewards["A"]:
                        if infoA["itemName"]==relic:
                            chance = infoA["chance"]
                            print(f"Rotation:A\nPlanet:{planet}\nPlanetNode:{planetNodes}\nGameMode:{gamemode}\nChance:{chance}%")


                if len(rewards["B"])!=0:
                    for infoB in rewards["B"]:
                        if infoB["itemName"] == relic:
                            chance=infoB["chance"]
                            print(f"Rotation:B\nPlanet:{planet}\nPlanetNode:{planetNodes}\nGameMode:{gamemode}\nChance:{chance}%")
                            ##print(planet, planetNodes,gamemode)

                print("---------------------------------------------------------------------------------------")








        except TypeError:
            pass
        except AttributeError:
            pass






def findPrimePartLocation(part: str):
    relics = relic_list["relics"]
    for relic in range(0,len(relics)):
        for rewards in relics[relic]["rewards"]:
            if rewards["itemName"]==part:
                tier=relics[relic]["tier"]
                relicName=relics[relic]["relicName"]
                state=relics[relic]["state"]
                rarity=rewards["rarity"]
                chanceOfGettingItem=rewards["chance"]
                print(part)
                print(f"Name:{tier+' '+relicName}\nState:{state}\nRarity:{rarity}\nChance:{chanceOfGettingItem}%")
                print("----------------------------------------------------------")













getFarmlocation("FFFF")












