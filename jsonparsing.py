import json

with open("C://Users//dasari.anirudh//Downloads//sample_data (1).json", "r") as file:
    json_data = file.read()
data = json.loads(json_data)

a = []
parameter_data = data['parametersList']
for parameter in parameter_data:
    dictionary = {}
    key = parameter["parameterName"]
    key1 = parameter["max"]
    key2 = parameter["min"]
    key3 = parameter["avg"]
    dictionary["parameterName"] = parameter["parameterName"]
    dictionary["max_value"] = parameter["max"]
    dictionary["min_value"] = parameter["min"]
    dictionary["avg_value"] = parameter["avg"]
    a.append(dictionary)
print(a)
with open("C://Users//dasari.anirudh//Downloads//out.json", "w") as file:
    parameter1 = file.write(json.dumps(a, indent=2))
    print(parameter1)
