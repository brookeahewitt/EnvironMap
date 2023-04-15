from tkinter import *
import customtkinter as ctk
import tkintermapview
import requests
import json




url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
params = {
    'location': '38.0293,78.4767',
    'radius': '200000',
    'type': 'restaurant',
    'key': key
}

response = requests.get(url, params=params)


data = json.loads(response.text)

print(data)

for result in data['results']:
    name = result['name']
    address = result['vicinity']
    print(name, address)