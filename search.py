from tkinter import *
import customtkinter as ctk
import tkintermapview
import requests
import json


key = "AIzaSyCRkh-Rq03zC0Leg6McXYuqsEYRM4f6Tok" #REMOVE KEY

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
params = {
    'location': '38.0293,-78.4767',
    'radius': '32186.9',
    'type': 'restaurant',
    'keyword': 'plant based',
    'key': key
}

response = requests.get(url, params=params)

data = json.loads(response.text)
print(data)

locations = []

for result in data['results']:
    name = result['name']
    address = result['vicinity']
    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']
    locations.append([name, address, lat, lng])

print(locations)