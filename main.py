from tkinter import *

import customtkinter
import customtkinter as ctk
import tkintermapview
import requests
import json

from PIL import Image, ImageTk
from ipregistry import IpregistryClient

#google maps starter code from https://github.com/TomSchimansky/TkinterMapView

#create tkinter window
import search

global right_labels
right_labels = []

root = ctk.CTk()
root.title("EnvironMap")
root.geometry(f"{1400}x{800}")
root.resizable(width=False, height=False)

#create a map widget
map_widget = tkintermapview.TkinterMapView(root, width=2100, height=1500, corner_radius=0)
map_widget.place(relx=0.45, rely=0.5, anchor=CENTER)

#set map to google maps
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

ipInfo_key = 'tkln3hmqu74nehbl' #REMOVE KEY

global latitude, longitude
client = IpregistryClient(ipInfo_key)
ipInfo = client.lookup()
ipInfo_access = json.loads(str(ipInfo))
latitude = ipInfo_access['location']['latitude']
longitude = ipInfo_access['location']['longitude']

#set current widget position by address
map_widget.set_position(latitude, longitude)

search_light = ImageTk.PhotoImage(Image.open('search_light.png').resize((70,70),Image.ANTIALIAS))

enterLocation = ctk.CTkEntry(master=root, placeholder_text="Search for a Location...", width=250)
enterLocation.pack(padx=20, pady=20)
enterLocation.place(relx=0.43, rely=0.05, anchor=ctk.CENTER)
def get_location():
    global latitude, longitude
    wanted_area = enterLocation.get()
    coords = search.search_address(wanted_area)
    enterLocation.delete(0, END)
    latitude = coords[0]
    longitude = coords[1]
    map_widget.set_position(latitude, longitude)



get_location_button = ctk.CTkButton(master=root, width=90, height=32, border_width=0, corner_radius=8, fg_color ='#80ed99', hover_color='#80ed99', image=search_light, text="", command=get_location)
get_location_button.place(relx=0.57, rely=0.05, anchor=ctk.CENTER)

rightSide = ctk.CTkFrame(master=root, height=1200, width=300, fg_color='#4de3e8')
rightSide.place(relx=1, rely=0.5, anchor=ctk.E)

places_label = ctk.CTkLabel(master=root, text="Places", width=120, height=25, fg_color=("white", "gray75"), font=('Arial', 24, 'bold'), corner_radius=8)
places_label.place(relx=0.9, rely=0.03, anchor=ctk.CENTER)

coords = str(latitude) + "," + str(longitude)
print(coords)
def click_restaurant():
    locations = search.restaurant(coords)
    markers = []
    map_widget.delete_all_marker()
    global right_labels
    for i in range(len(right_labels)):
        right_labels[i].destroy()
    right_labels = []
    y_val = 0.1
    for i in range(len(locations)):
        if (y_val > 1):
            break
        location_text = locations[i][0] + "\n" + locations[i][1]
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])

def click_secondHand():
    locations = search.shopping(coords)
    markers = []
    map_widget.delete_all_marker()
    global right_labels
    for i in range(len(right_labels)):
        right_labels[i].destroy()
    right_labels = []
    y_val = 0.1
    for i in range(len(locations)):
        if (y_val > 1):
            break
        location_text = locations[i][0] + "\n" + locations[i][1]
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])

def click_busStops():
    locations = search.busStops(coords)
    markers = []
    map_widget.delete_all_marker()
    global right_labels
    for i in range(len(right_labels)):
        right_labels[i].destroy()
    right_labels = []
    y_val = 0.1
    for i in range(len(locations)):
        if (y_val > 1):
            break
        location_text = locations[i][0] + "\n" + locations[i][1]
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])

def click_trainStations():
    locations = search.trainStations(coords)
    markers = []
    map_widget.delete_all_marker()
    global right_labels
    for i in range(len(right_labels)):
        right_labels[i].destroy()
    right_labels = []
    y_val = 0.1
    for i in range(len(locations)):
        if (y_val > 1):
            break
        location_text = locations[i][0] + "\n" + locations[i][1]
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])

def click_bikeRoutes():
    locations = search.bikeRoutes(coords)
    markers = []
    map_widget.delete_all_marker()
    global right_labels
    for i in range(len(right_labels)):
        right_labels[i].destroy()
    right_labels = []
    y_val = 0.1
    for i in range(len(locations)):
        if (y_val > 1):
            break
        location_text = locations[i][0] + "\n" + locations[i][1]
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])

def click_parks():
    locations = search.parks(coords)
    markers = []
    map_widget.delete_all_marker()
    global right_labels
    for i in range(len(right_labels)):
        right_labels[i].destroy()
    right_labels = []
    y_val = 0.1
    for i in range(len(locations)):
        if (y_val > 1):
            break
        location_text = locations[i][0] + "\n" + locations[i][1]
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])

def click_gardens():
    locations = search.publicgardens(coords)
    markers = []
    map_widget.delete_all_marker()
    global right_labels
    for i in range(len(right_labels)):
        right_labels[i].destroy()
    right_labels = []
    y_val = 0.1
    for i in range(len(locations)):
        if (y_val > 1):
            break
        location_text = locations[i][0] + "\n" + locations[i][1]
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])

def click_hiking():
    locations = search.hiking(coords)
    markers = []
    map_widget.delete_all_marker()
    global right_labels
    for i in range(len(right_labels)):
        right_labels[i].destroy()
    right_labels = []
    y_val = 0.1
    for i in range(len(locations)):
        if (y_val > 1):
            break
        location_text = locations[i][0] + "\n" + locations[i][1]
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])

#LightMode/DarkMode
#customtkinter.set_appearance_mode("System")

#Moving Side Menu - Source https://stackoverflow.com/questions/66858214/tkinter-side-bar
min_w = 240 # Minimum width of the frame
max_w = 500 # Maximum width of the frame
cur_width = min_w # Increasing width of the frame
expanded = False # Check if it is completely expanded

def expand():
    global cur_width, expanded
    cur_width += 10 # Increase the width by 10
    rep = root.after(5,expand) # Repeat this func every 5 ms
    frame.config(width=cur_width) # Change the width to new increase width
    foodSubframe.config(width=cur_width)
    shoppingSubframe.config(width=cur_width)
    transportationSubframe.config(width=cur_width)
    natureSubframe.config(width=cur_width)
    if cur_width >= max_w: # If width is greater than maximum width
        expanded = True # Frame is expended
        root.after_cancel(rep) # Stop repeating the func
        fill()

def contract():
    global cur_width, expanded
    cur_width -= 10 # Reduce the width by 10
    rep = root.after(5,contract) # Call this func every 5 ms
    frame.config(width=cur_width) # Change the width to new reduced width
    foodSubframe.config(width=cur_width)
    shoppingSubframe.config(width=cur_width)
    transportationSubframe.config(width=cur_width)
    natureSubframe.config(width=cur_width)
    if cur_width <= min_w: # If it is back to normal width
        expanded = False # Frame is not expanded
        root.after_cancel(rep) # Stop repeating the func
        fill()


def fill():
    if expanded:  # If the frame is expanded
    # Show a text, and remove the image
        food_b.configure(text='Food', image='', font=(0, 21))
        restaurant_b.configure(text='Restaurants', font=(0, 21))
        farmersMarket_b.configure(text='Farmers Market', font=(0, 21))

        shopping_b.configure(text='Shopping', image='', font=(0, 21))
        secondHand_b.configure(text='Second Hand Stores', font=(0, 21))

        transportation_b.configure(text='Transportation', image='', font=(0, 21))
        busStops_b.configure(text='Bus Stops', font=(0, 21))
        trainsStations_b.configure(text='Train Stations', font=(0, 21))
        bikeRoutes_b.configure(text='Bike Stores', font=(0, 21))

        nature_b.configure(text='Recreation', image='', font=(0, 21))
        parks_b.configure(text='Parks', font=(0, 21))
        publicGardens_b.configure(text='Campgrounds', font=(0, 21))
        hikingTrails_b.configure(text='Hiking Trails', font=(0, 21))

        back_food_b.configure(text='', font=(0, 21))
        back_shopping_b.configure(text='', font=(0, 21))
        back_transportation_b.configure(text='', font=(0, 21))
        back_nature_b.configure(text='', font=(0, 21))

    else:
        # Bring the image back
        food_b.configure(text='', image=food_light, font=(0, 21))
        restaurant_b.configure(text='', font=(0, 21))
        farmersMarket_b.configure(text='', font=(0, 21))

        shopping_b.configure(text='', image=shopping_light, font=(0, 21))
        secondHand_b.configure(text='', font=(0, 21))

        transportation_b.configure(text='', image=bike_light, font=(0, 21))
        busStops_b.configure(text='', font=(0, 21))
        trainsStations_b.configure(text='', font=(0, 21))
        bikeRoutes_b.configure(text='', font=(0, 21))

        nature_b.configure(text='', image=parks_light, font=(0, 21))
        parks_b.configure(text='', font=(0, 21))
        publicGardens_b.configure(text='', font=(0, 21))
        hikingTrails_b.configure(text='', font=(0, 21))

        back_food_b.configure(text='', font=(0, 21))
        back_shopping_b.configure(text='', font=(0, 21))
        back_transportation_b.configure(text='', font=(0, 21))
        back_nature_b.configure(text='', font=(0, 21))


root.update()  # For the width to get updated
frame = Frame(root, bg='#80ed99', width=170, height=root.winfo_height())
frame.grid(row=0, column=0)

#Sub Menus
foodSubframe = Frame(root, bg='#4de3e8', width=50, height=root.winfo_height())
shoppingSubframe = Frame(root, bg='#4de3e8', width=50, height=root.winfo_height())
transportationSubframe = Frame(root, bg='#4de3e8', width=50, height=root.winfo_height())
natureSubframe = Frame(root, bg='#4de3e8', width=50, height=root.winfo_height())

#Food
def showFoodMenu():
    frame.grid_remove()
    foodSubframe.grid(row=0, column=0)
    restaurant_b.grid(row=0, column=0, pady=10)

    back_food_b.grid(row=2, column=0, pady=425)
    foodSubframe.bind('<Enter>', lambda e: expand())
    foodSubframe.bind('<Leave>', lambda e: contract())

#Shopping
def showShoppingMenu():
    frame.grid_remove()
    shoppingSubframe.grid(row=0, column=0)
    secondHand_b.grid(row=0, column=0, pady=10)
    back_shopping_b.grid(row=1, column=0, pady=475)
    shoppingSubframe.bind('<Enter>', lambda e: expand())
    shoppingSubframe.bind('<Leave>', lambda e: contract())

#Transporation
def showTransportationMenu():
    frame.grid_remove()
    transportationSubframe.grid(row=0, column=0)
    busStops_b.grid(row=0, column=0, pady=10)
    trainsStations_b.grid(row=1, column=0, pady=10)
    bikeRoutes_b.grid(row=2, column=0, pady=10)
    back_transportation_b.grid(row=3, column=0, pady=375)
    transportationSubframe.bind('<Enter>', lambda e: expand())
    transportationSubframe.bind('<Leave>', lambda e: contract())

#Nature
def showNatureMenu():
    frame.grid_remove()
    natureSubframe.grid(row=0, column=0)
    parks_b.grid(row=0, column=0, pady=10)
    publicGardens_b.grid(row=1, column=0, pady=10)
    hikingTrails_b.grid(row=2, column=0, pady=10)
    back_nature_b.grid(row=3, column=0, pady=375)
    natureSubframe.bind('<Enter>', lambda e: expand())
    natureSubframe.bind('<Leave>', lambda e: contract())

def backFoodButton():
    foodSubframe.grid_remove()
    frame.grid(row=0, column=0)

def backShoppingButton():
    shoppingSubframe.grid_remove()
    frame.grid(row=0, column=0)

def backTransportationButton():
    transportationSubframe.grid_remove()
    frame.grid(row=0, column=0)

def backNatureButton():
    natureSubframe.grid_remove()
    frame.grid(row=0, column=0)

food_light = ImageTk.PhotoImage(Image.open('food_light.png').resize((120,120),Image.ANTIALIAS))
parks_light = ImageTk.PhotoImage(Image.open('parks_light.png').resize((120,120),Image.ANTIALIAS))
bike_light = ImageTk.PhotoImage(Image.open('bike_light.png').resize((120,120),Image.ANTIALIAS))
shopping_light = ImageTk.PhotoImage(Image.open('shopping_light.png').resize((120,120),Image.ANTIALIAS))


# Make the buttons with the icons to be shown #PUT SUBMENUCOMMANDS HERE!!!
food_b = ctk.CTkButton(frame,fg_color= '#80ed99',image=food_light, hover_color='#80ed99', command=showFoodMenu)
restaurant_b = ctk.CTkButton(foodSubframe, fg_color='#80ed99', hover_color='#80ed99',command=click_restaurant)
farmersMarket_b = ctk.CTkButton(foodSubframe, fg_color='#80ed99',hover_color='#80ed99',)

shopping_b = ctk.CTkButton(frame, fg_color='#80ed99', image=shopping_light, hover_color='#80ed99',command=showShoppingMenu)
secondHand_b = ctk.CTkButton(shoppingSubframe, fg_color='#80ed99', hover_color='#80ed99',command=click_secondHand)

transportation_b = ctk.CTkButton(frame, fg_color='#80ed99', image=bike_light, hover_color='#80ed99',command=showTransportationMenu)
busStops_b = ctk.CTkButton(transportationSubframe, fg_color='#80ed99', hover_color='#80ed99',command=click_busStops)
trainsStations_b = ctk.CTkButton(transportationSubframe, fg_color='#80ed99', hover_color='#80ed99',command=click_trainStations)
bikeRoutes_b = ctk.CTkButton(transportationSubframe, fg_color='#80ed99', hover_color='#80ed99',command=click_bikeRoutes)

nature_b = ctk.CTkButton(frame, fg_color='#80ed99', hover_color='#80ed99',image=parks_light,command=showNatureMenu)
parks_b = ctk.CTkButton(natureSubframe, fg_color='#80ed99',hover_color='#80ed99', command=click_parks)
publicGardens_b = ctk.CTkButton(natureSubframe, fg_color='#80ed99', hover_color='#80ed99', command=click_gardens)
hikingTrails_b = ctk.CTkButton(natureSubframe, fg_color='#80ed99', hover_color='#80ed99',command=click_hiking)

search_light = ImageTk.PhotoImage(Image.open('search_light.png').resize((70,70),Image.ANTIALIAS))

back_food_b = ctk.CTkButton(foodSubframe, fg_color='#80ed99', hover_color='#80ed99',image=search_light, command=backFoodButton)
back_shopping_b = ctk.CTkButton(shoppingSubframe, fg_color='#80ed99', hover_color='#80ed99',image=search_light, command=backShoppingButton)
back_transportation_b = ctk.CTkButton(transportationSubframe, fg_color='#80ed99', hover_color='#80ed99', image=search_light, command=backTransportationButton)
back_nature_b = ctk.CTkButton(natureSubframe, fg_color='#80ed99', image=search_light, hover_color='#80ed99',command=backNatureButton)

logo_light = ImageTk.PhotoImage(Image.open('logo_light.png'),Image.ANTIALIAS)
logo_label = ctk.CTkLabel(master=root, image=logo_light, text="")
logo_label.place(relx=0.45, rely=0.95, anchor=ctk.CENTER)

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
foodSubframe.grid_propagate(False)
shoppingSubframe.grid_propagate(False)
transportationSubframe.grid_propagate(False)
natureSubframe.grid_propagate(False)



root.mainloop()

