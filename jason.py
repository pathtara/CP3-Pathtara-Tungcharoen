import json

def reaJson():
    x = '{"name": "Aum", "age": 99, "pet": "dog"} '
    y = json.load(x)
    print(y["age"])

reaJson()