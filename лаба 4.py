stuff_all = [
    {"name": "r", "size": 3, "value": 25},
    {"name": "m", "size": 2, "value": 20},
    {"name": "a", "size": 1, "value": 10},
    {"name": "t", "size": 1, "value": 25},
    {"name": "ax", "size": 3, "value": 20},
    {"name": "p", "size": 2, "value": 15},
    {"name": "am", "size": 2, "value": 15},
    {"name": "k", "size": 1, "value": 15},
    {"name": "s", "size": 2, "value": 20},
    {"name": "f", "size": 1, "value": 15},
    {"name": "c", "size": 2, "value": 20},
]

sorted_stuff = sorted(stuff_all, key=lambda x: x["value"], reverse=True)
sorted_stuff.insert(0, {"name": "i", "size": 1, "value": 20})

a = 2
b = 4
free_space = a * b


taken_items = []


for item in sorted_stuff:
    if item["size"] <= free_space:
        taken_items.append(item["name"])
        free_space -= item["size"]


print("Упакованные предметы:", taken_items)
total_survival_points = sum(item["value"] for item in sorted_stuff if item["name"] in taken_items)
print("Итоговые очки выживания:", total_survival_points)