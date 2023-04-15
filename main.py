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
root.title("EnvironMap")
root.geometry(f"{800}x{600}")
root.resizable(width=False, height=False)

#create a map widget
map_widget = tkintermapview.TkinterMapView(root, width=1800, height=1200, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

#set map to google maps
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

global latitude, longitude

ipInfo_key = 'tkln3hmqu74nehbl' #REMOVE KEY
client = IpregistryClient(ipInfo_key)
ipInfo = client.lookup()
ipInfo_access = json.loads(str(ipInfo))
latitude = ipInfo_access['location']['latitude']
longitude = ipInfo_access['location']['longitude']

#set current widget position by address
map_widget.set_position(latitude, longitude)

enterLocation = ctk.CTkEntry(master=root, placeholder_text="Search for a Location")
enterLocation.pack(padx=20, pady=20)
enterLocation.place(relx=0.5, rely=0.05, anchor=ctk.CENTER)
def get_location():
    global latitude, longitude
    wanted_area = enterLocation.get()
    coords = search.search_address(wanted_area)
    enterLocation.delete(0, END)
    latitude = coords[0]
    longitude = coords[1]
    map_widget.set_position(latitude, longitude)



get_location_button = ctk.CTkButton(master=root, width=120, height=32, border_width=0, corner_radius=8, text="Submit Location", command=get_location)
get_location_button.place(relx=0.68, rely=0.05, anchor=ctk.CENTER)

coords = str(latitude) + "," + str(longitude)
print(coords)

locations = search.restaurant(coords)

markers = []
for i in range(len(locations)):
    marker = "marker" + str(i)
    markers.append(marker)

print(markers)

for i in range(len(locations)):
    markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
    markers[i].set_text(locations[i][0])

#LightMode/DarkMode
#customtkinter.set_appearance_mode("System")

#Moving Side Menu - Source https://stackoverflow.com/questions/66858214/tkinter-side-bar
min_w = 50 # Minimum width of the frame
max_w = 365 # Maximum width of the frame
cur_width = min_w # Increasing width of the frame
expanded = False # Check if it is completely expanded

def expand():
    global cur_width, expanded
    cur_width += 10 # Increase the width by 10
    rep = root.after(5,expand) # Repeat this func every 5 ms
    frame.config(width=cur_width) # Change the width to new increase width
    if cur_width >= max_w: # If width is greater than maximum width
        expanded = True # Frame is expended
        root.after_cancel(rep) # Stop repeating the func
        fill()

def contract():
    global cur_width, expanded
    cur_width -= 10 # Reduce the width by 10
    rep = root.after(5,contract) # Call this func every 5 ms
    frame.config(width=cur_width) # Change the width to new reduced width
    if cur_width <= min_w: # If it is back to normal width
        expanded = False # Frame is not expanded
        root.after_cancel(rep) # Stop repeating the func
        fill()


def fill():
    if expanded:  # If the frame is exanded
    # Show a text, and remove the image
        food_b.configure(text='Food', font=(0, 21))
        shopping_b.configure(text='Shopping', font=(0, 21))
        transportation_b.configure(text='Transportation', font=(0, 21))
        nature_b.configure(text='Nature', font=(0, 21))
    else:
        # Bring the image back
        food_b.configure(text='', font=(0, 21),)
        shopping_b.configure(text='', font=(0, 21))
        transportation_b.configure(text='',font=(0, 21))
        nature_b.configure(text='', font=(0, 21))

root.update()  # For the width to get updated
frame = Frame(root, bg='orange', width=50, height=root.winfo_height())
frame.grid(row=0, column=0)

#Sub Menus
subframe = Frame(root, bg='blue', width=50, height=root.winfo_height())
subframe.grid(row=0, column=5)
#Food
def showFoodMenu():
    restaurant_b = Button(frame, text="", bg='orange', relief='flat', font=(0, 21))  # add command
    if expanded:
        restaurant_b.config(text='Restaurants', font=(0, 21)) #add command
        restaurant_b.grid(row=0, column=2, pady=10)
    else:
        restaurant_b.config(text='', font=(0, 21))  # add command
        restaurant_b.destroy() #don't have command here


# Make the buttons with the icons to be shown
food_b = ctk.CTkButton(frame,fg_color= 'orange', command=showFoodMenu)
shopping_b = ctk.CTkButton(frame, fg_color='orange')
transportation_b = ctk.CTkButton(frame, fg_color='orange')
nature_b = ctk.CTkButton(frame, fg_color='orange')

# Put them on the frame
food_b.grid(row=0, column=0, pady=10)
shopping_b.grid(row=1, column=0, pady=10)
transportation_b.grid(row=2, column=0, pady=10)
nature_b.grid(row=3, column=0)

# Bind to the frame, if entered or left
frame.bind('<Enter>', lambda e: expand())
frame.bind('<Leave>', lambda e: contract())

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)


root.mainloop()

