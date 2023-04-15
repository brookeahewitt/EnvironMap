from tkinter import *
import customtkinter as ctk
import tkintermapview
import requests
import json


key = "AIzaSyCRkh-Rq03zC0Leg6McXYuqsEYRM4f6Tok"

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
params = {
    'location': '38.0293,78.4767',
    'radius': '100',
    'type': 'restaurant',
    'key': key
}

response = requests.get(url, params=params)

data = json.loads(response.text)
for result in data['results']:
    name = result['name']
    address = result['vicinity']
    print(name, address)

#google maps starter code from https://github.com/TomSchimansky/TkinterMapView

#create tkinter window
root = ctk.CTk()
root.geometry(f"{800}x{600}")
root.resizable(width=False, height=False)

#create a map widget

map_widget = tkintermapview.TkinterMapView(root, width=1800, height=1200, corner_radius=0)

map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

#set map to google maps
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

#set current widget position by address (change to current)
map_widget.set_position(38.033554, -78.507980)


root.mainloop()

