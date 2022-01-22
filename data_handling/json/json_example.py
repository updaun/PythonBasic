# Javascript Object Notation
import json

with open("data_handling/dataset/json_example.json", "r", encoding="utf8") as f:
    contents = f.read()
    json_data = json.loads(contents)
    print(json_data["employees"])
    print(type(json_data))

for employee in json_data["employees"]:
    print(employee["firstName"], employee["lastName"])

dict_data = {'Name':'Zara', 'Age':7, 'Class':'First'}

with open("data_handling/dataset/json_write.json", "w", encoding="utf8") as f:
    json.dump(dict_data, f)