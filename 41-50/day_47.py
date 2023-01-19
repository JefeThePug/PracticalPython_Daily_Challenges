#Challenge 47: Save a JSON
import json

def save_json(d):
    with open('day_47_myjson.json', 'w') as f:
        json.dump(d, f)

def read_json():
    with open('day_47_myjson.json') as f:
        print(json.load(f))


names = {'name': 'Carol','sex': 'female','age': 55}
save_json(names)
read_json()
