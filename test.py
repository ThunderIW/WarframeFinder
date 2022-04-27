if len(rewards["A"]) != 0:
    for infoA in rewards["A"]:
        if infoA["itemName"] == relic:
            chance = infoA["chance"]
            print(
                f"Rotation:A\nPlanet:{planet}\nPlanetNode:{planetNodes}\nGameMode:{gamemode}\nChance:{chance}%")

if len(rewards["B"]) != 0:
    for infoB in rewards["B"]:
        if infoB["itemName"] == relic:
            chance = infoB["chance"]
            print(
                f"Rotation:B\nPlanet:{planet}\nPlanetNode:{planetNodes}\nGameMode:{gamemode}\nChance:{chance}%")
            ##print(planet, planetNodes,gamemode)

print("---------------------------------------------------------------------------------------")