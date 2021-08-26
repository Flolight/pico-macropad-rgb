import json

def read_configuration():
    f = open('configuration.json',)
    data = json.load(f)
    for i in data['conf']:
        print(i)

    f.close()

read_configuration()