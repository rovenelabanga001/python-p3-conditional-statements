dog = "thirsty"

dict_map = {
    "hungry":"Refilling the food bowl",
    "thirsty":"Refilling water bowl",
    "playful":"Playing tug of war",
    "cuddly":"Snuggling"
}

owner = dict_map.get(dog, "Reading newspaper.")
print(owner)