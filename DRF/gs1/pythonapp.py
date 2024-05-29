import requests
import json

URL = 'http://127.0.0.1:8000/studata/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(URL, data=json_data)
    data = r.json()
    print(data)

# get_data()


def post_data():
    data={
        'name':'Ravi',
        'roll':'104',
        'city':'deoband'
    }
    json_data = json.dumps(data)
    r = requests.post(URL, data=json_data)
    data = r.json()
    print(data)

# post_data()
    

def update_data():
    data={
        'id': 4,
        'name':'Rohit ranchaddas',
        'roll':210,
        'city':'gurgown'
    }
    json_data = json.dumps(data)
    r = requests.put(URL, data=json_data)
    data = r.json()
    print(data)

update_data()
    

def delete_data():
    data={'id': 3 }
    json_data = json.dumps(data)
    r = requests.delete(URL, data=json_data)
    data = r.json()
    print(data)

# delete_data()