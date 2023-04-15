from tkinter import *
import customtkinter as ctk
import tkintermapview
import requests
import json
from ipregistry import IpregistryClient

#google maps starter code from https://github.com/TomSchimansky/TkinterMapView

#create tkinter window
import search

root = ctk.CTk()
root.geometry(f"{800}x{600}")
root.resizable(width=False, height=False)

#create a map widget

map_widget = tkintermapview.TkinterMapView(root, width=1800, height=1200, corner_radius=0)

map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

#set map to google maps
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

ipInfo_key = key #REMOVE KEY
client = IpregistryClient(ipInfo_key)
ipInfo = client.lookup()
ipInfo_access = json.loads(str(ipInfo))
latitude = ipInfo_access['location']['latitude']
longitude = ipInfo_access['location']['latitude']

#set current widget position by address
map_widget.set_position(latitude, longitude)

markers = []
for i in range(len(search.locations)):
    marker = "marker" + str(i)
    markers.append(marker)

print(markers)

for i in range(len(search.locations)):
    markers[i] = map_widget.set_position(search.locations[i][2], search.locations[i][3], marker=True)
    markers[i].set_text(search.locations[i][0])


root.mainloop()

