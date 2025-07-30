secret_cordinates = (-20.1452, -44.8857)
weapon_sheet = {
    "name": "Widowmaker",
    "type": "sword",
    "weight": 2.5,
    "material": "valerian steel",
    "available": True,
}
print(f"Longitude:{secret_cordinates[1]}")

print(f"Weapon type: {weapon_sheet['type']}")
weapon_sheet["rarity"] = "legendary"
print(f"Weapon sheets:{weapon_sheet}")

print("\n Weapon Sheet Details:")
for key, value in weapon_sheet.items():
    print(f"{key.capitalize()}: {value} ")
