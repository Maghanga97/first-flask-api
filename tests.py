import re
from wsgiref import headers
import requests
import pprint

BASE_URL = "http://127.0.0.1:5000/"
r_headers = {}
r_headers['Content-Type'] = 'application/json'

# r_post = requests.post(BASE_URL+ "/add-person", {'p_id': 1, 'name': 'Eugene Fama','gender': 'Male', 'age': 25 })

post_career = requests.put(BASE_URL + "/add-career", {'career_id': 2, 'name': 'Pharmacist'})

# print("New person created:", r_post.json())
print("New career created:", post_career.json())

r_get = requests.get(BASE_URL + "/person/2")
print(r_get.json())