table = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
}
while(True):
    s = input("Item ")
    if(s.strip().lower() in table):
        print(f"Calories: {table[s.strip().lower()]}")