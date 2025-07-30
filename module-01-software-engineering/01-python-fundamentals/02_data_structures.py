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

armory_inventory = [
    {
        "name": "Widowmaker",
        "type": "sword",
        "weight": 2.5,
        "material": "valerian steel",
        "available": True,
    },
    {
        "name": "Excalibur",
        "type": "sword",
        "weight": 3.0,
        "material": "mythril",
        "available": False,
    },
    {
        "name": "Glamdring",
        "type": "sword",
        "weight": 2.8,
        "material": "mithril",
        "available": True,
    },
]
print("\nArmory Inventory:")
for weapon in armory_inventory:
    print(f"Weapon Name: {weapon['name']} (Type: {weapon['type']})")
