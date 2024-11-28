import json


with open("JASON DERULO.json", "r", encoding="utf-8-sig") as file:
    data=json.load(file)
    print(data)
print("Datnes nosaukums ir:", file.name) 