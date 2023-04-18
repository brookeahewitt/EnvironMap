from tkinter import *

import customtkinter
import customtkinter as ctk
import tkintermapview
import requests
import json

from PIL import Image, ImageTk
from ipregistry import IpregistryClient

# google maps starter code from https://github.com/TomSchimansky/TkinterMapView

# create tkinter window
import search

global right_labels
right_labels = []

root = ctk.CTk()
root.title("EnvironMap")
root.geometry("1400x800")
# root.resizable(width=False, height=False)
root.grid_rowconfigure(0, weight=1)  # configure grid system
root.grid_columnconfigure(0, weight=1)

category_frame = ctk.CTkFrame(master=root, width=325, height=900)
category_frame.grid(row=0, column=0, padx=20, pady=20)
category_frame.grid_propagate(False)
main_frame = ctk.CTkFrame(master=root, width=2000, height=8000)
main_frame.grid(row=0, column=1, padx=20)

places_frame = ctk.CTkFrame(master=root, width=300, height=900)
places_frame.grid(row=0, column=2, padx=20, pady=20)
places_frame.grid_propagate(False)

foodSubframe = ctk.CTkFrame(master=root, width=325, height=900)
shoppingSubframe = ctk.CTkFrame(master=root, width=325, height=900)
transportationSubframe = ctk.CTkFrame(master=root, width=325, height=900)
natureSubframe = ctk.CTkFrame(master=root, width=325, height=900)

# create a map widget
map_widget = tkintermapview.TkinterMapView(main_frame, width=2000, height=1600, corner_radius=8)
map_widget.grid(row=1, column=0, padx=20, pady=20)
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

search_img = ctk.CTkImage(light_image=Image.open('search_light.png'), dark_image=Image.open('search_dark.png'),
                          size=(30, 30))
enterLocation = ctk.CTkEntry(master=root, placeholder_text="Search for a Location...", width=250, height=35,
                             font=("Helvetica", 20))
enterLocation.place(relx=0.48, rely=0.05, anchor=ctk.CENTER)

ipInfo_key = 'tkln3hmqu74nehbl'
global latitude, longitude
client = IpregistryClient(ipInfo_key)
ipInfo = client.lookup()
ipInfo_access = json.loads(str(ipInfo))
latitude = ipInfo_access['location']['latitude']
longitude = ipInfo_access['location']['longitude']

map_widget.set_position(latitude, longitude)


def get_location():
    global latitude, longitude, coords
    wanted_area = enterLocation.get()
    coords = search.search_address(wanted_area)
    enterLocation.delete(0, END)
    latitude = coords[0]
    longitude = coords[1]
    map_widget.set_position(latitude, longitude)
    if type(coords) == list:
        coords = str(latitude) + "," + str(longitude)
    print(coords)


logo_img = ctk.CTkImage(Image.open('logo_dark.png'), size=(290, 100))
logo_label = ctk.CTkLabel(master=root, image=logo_img, text="")
logo_label.place(relx=0.48, rely=0.94, anchor=ctk.CENTER)

get_location_button = ctk.CTkButton(master=root, width=60, height=32, border_width=0, corner_radius=8,
                                    fg_color='#57CC99', hover_color='#3F8F6C', text="", image=search_img,
                                    command=get_location)
get_location_button.place(relx=0.58, rely=0.05, anchor=ctk.CENTER)

places_label = ctk.CTkLabel(master=places_frame, text="Nearby Locations", width=120, height=25,
                            text_color=("black", "white"), font=('Helvetica', 20, 'bold'), corner_radius=8)
places_label.grid(row=0, column=0, pady=20, padx=67)

coords = str(latitude) + "," + str(longitude)
print(coords)


def click_restaurant():
    global coords
    print(coords)
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
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color='#57CC99', corner_radius=8,
                             font=("Helvetica", 12, 'bold'), text_color=("white", "black"))
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
    global coords
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
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color='#57CC99', corner_radius=8,
                             text_color=("white", "black"))
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
    global coords
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
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color='#57CC99', corner_radius=8,
                             text_color=("white", "black"))
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
    global coords
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
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color='#57CC99', corner_radius=8,
                             text_color=("white", "black"))
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
    global coords
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
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color='#57CC99', corner_radius=8,
                             text_color=("white", "black"))
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
    global coords
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
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color='#57CC99', corner_radius=8,
                             text_color=("white", "black"))
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
    global coords
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
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color='#57CC99', corner_radius=8,
                             text_color=("white", "black"))
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
    global coords
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
        label = ctk.CTkLabel(master=root, text=location_text, width=120, height=25, fg_color='#57CC99', corner_radius=8,
                             text_color=("white", "black"))
        label.place(relx=0.9, rely=y_val, anchor=ctk.CENTER)
        right_labels.append(label)
        y_val += 0.05
    for i in range(len(locations)):
        marker = "marker" + str(i)
        markers.append(marker)
    for i in range(len(locations)):
        markers[i] = map_widget.set_position(locations[i][2], locations[i][3], marker=True)
        markers[i].set_text(locations[i][0])


def showFoodMenu():
    category_frame.grid_remove()
    foodSubframe.grid(row=0, column=0, padx=20, pady=20)
    foodSubframe.grid_propagate(False)
    restaurant_b = ctk.CTkButton(master=foodSubframe, text="Restaurant", text_color=("white", "black"), height=60,
                                 width=260, font=("Helvetica", 25), fg_color='#57CC99',
                                 hover_color='#3F8F6C', command=click_restaurant)
    back_food_b = ctk.CTkButton(master=foodSubframe, image=back, text="", height=60, width=150,
                                fg_color='#57CC99', hover_color='#3F8F6C', command=backFoodButton)
    restaurant_b.grid(row=0, column=0, pady=10, padx=20)
    back_food_b.grid(row=2, column=0, pady=680)


# Shopping
def showShoppingMenu():
    category_frame.grid_remove()
    shoppingSubframe.grid(row=0, column=0, padx=20, pady=20)
    shoppingSubframe.grid_propagate(False)
    secondHand_b = ctk.CTkButton(master=shoppingSubframe, text="Second Hand", text_color=("white", "black"), height=60,
                                 width=260, font=("Helvetica", 25), fg_color='#57CC99',
                                 hover_color='#3F8F6C', command=click_secondHand)
    back_shopping_b = ctk.CTkButton(master=shoppingSubframe, image=back, text="", height=60, width=150,
                                    fg_color='#57CC99', hover_color='#3F8F6C',
                                    command=backShoppingButton)
    secondHand_b.grid(row=0, column=0, pady=10, padx=20)
    back_shopping_b.grid(row=1, column=0, pady=680)


# Transporation
def showTransportationMenu():
    category_frame.grid_remove()
    transportationSubframe.grid(row=0, column=0, padx=20, pady=20)
    transportationSubframe.grid_propagate(False)
    busStops_b = ctk.CTkButton(master=transportationSubframe, text="Bus Stops", text_color=("white", "black"),
                               height=60,
                               width=260, font=("Helvetica", 25), fg_color='#57CC99',
                               hover_color='#3F8F6C', command=click_busStops)
    trainsStations_b = ctk.CTkButton(master=transportationSubframe, text="Train Stations",
                                     text_color=("white", "black"), height=60,
                                     width=260, font=("Helvetica", 25), fg_color='#57CC99',
                                     hover_color='#3F8F6C', command=click_trainStations)
    bikeRoutes_b = ctk.CTkButton(master=transportationSubframe, text="Bike Routes", text_color=("white", "black"),
                                 height=60,
                                 width=260, font=("Helvetica", 25), fg_color='#57CC99',
                                 hover_color='#3F8F6C', command=click_bikeRoutes)
    back_transportation_b = ctk.CTkButton(master=transportationSubframe, image=back, text="", height=60, width=150,
                                          fg_color='#57CC99', hover_color='#3F8F6C',
                                          command=backTransportationButton)
    busStops_b.grid(row=0, column=0, pady=10, padx=20)
    trainsStations_b.grid(row=1, column=0, pady=10, padx=20)
    bikeRoutes_b.grid(row=2, column=0, pady=10, padx=20)
    back_transportation_b.grid(row=3, column=0, pady=525)


# Nature
def showNatureMenu():
    category_frame.grid_remove()
    natureSubframe.grid(row=0, column=0, padx=20, pady=20)
    natureSubframe.grid_propagate(False)
    parks_b = ctk.CTkButton(master=natureSubframe, text="Parks", text_color=("white", "black"), height=60,
                            width=260, font=("Helvetica", 25), fg_color='#57CC99',
                            hover_color='#3F8F6C', command=click_parks)
    publicGardens_b = ctk.CTkButton(master=natureSubframe, text="Public Gardens", text_color=("white", "black"),
                                    height=60,
                                    width=260, font=("Helvetica", 25), fg_color='#57CC99',
                                    hover_color='#3F8F6C', command=click_gardens)
    hikingTrails_b = ctk.CTkButton(master=natureSubframe, text="Hiking Trails", text_color=("white", "black"),
                                   height=60,
                                   width=260, font=("Helvetica", 25), fg_color='#57CC99',
                                   hover_color='#3F8F6C', command=click_hiking)
    back_nature_b = ctk.CTkButton(master=natureSubframe, image=back, text="", height=60, width=150,
                                  fg_color='#57CC99', hover_color='#3F8F6C',
                                  command=backNatureButton)
    parks_b.grid(row=0, column=0, pady=10, padx=20)
    publicGardens_b.grid(row=1, column=0, pady=10, padx=20)
    hikingTrails_b.grid(row=2, column=0, pady=10, padx=20)
    back_nature_b.grid(row=3, column=0, pady=525)


def backFoodButton():
    foodSubframe.grid_remove()
    category_frame.grid(row=0, column=0)


def backShoppingButton():
    shoppingSubframe.grid_remove()
    category_frame.grid(row=0, column=0)


def backTransportationButton():
    transportationSubframe.grid_remove()
    category_frame.grid(row=0, column=0)


def backNatureButton():
    natureSubframe.grid_remove()
    category_frame.grid(row=0, column=0)


food = ctk.CTkImage(light_image=Image.open('food_light.png'), dark_image=Image.open('food_dark.png'), size=(60, 60))
shopping = ctk.CTkImage(light_image=Image.open('shopping_light.png'), dark_image=Image.open('shopping_dark.png'),
                        size=(60, 60))
transportation = ctk.CTkImage(light_image=Image.open('bike_light.png'), dark_image=Image.open('bike_dark.png'),
                              size=(80, 55))
recreation = ctk.CTkImage(light_image=Image.open('parks_light.png'), dark_image=Image.open('parks_dark.png'),
                          size=(60, 60))
back = ctk.CTkImage(light_image=Image.open('back_light.png'), dark_image=Image.open('back_dark.png'), size=(60, 40))

food_button = ctk.CTkButton(master=category_frame, image=food, text="Food", text_color=("white", "black"), height=60,
                            width=260, anchor='w', font=("Helvetica", 25), fg_color='#57CC99', hover_color='#3F8F6C',
                            command=showFoodMenu)
food_button.grid(row=0, column=0, padx=20, pady=30, sticky=W)

shopping_button = ctk.CTkButton(master=category_frame, image=shopping, text="Shopping", text_color=("white", "black"),
                                height=60, width=260, anchor='w', font=("Helvetica", 25), fg_color='#57CC99',
                                hover_color='#3F8F6C', command=showShoppingMenu)
shopping_button.grid(row=1, column=0, padx=20, pady=30, sticky=W)
transportation_button = ctk.CTkButton(master=category_frame, image=transportation, text_color=("white", "black"),
                                      text="Transportation", height=60, width=260, anchor='w', font=("Helvetica", 25),
                                      fg_color='#57CC99', hover_color='#3F8F6C', command=showTransportationMenu)
transportation_button.grid(row=2, column=0, padx=20, pady=30, sticky=W)
recreation_button = ctk.CTkButton(master=category_frame, image=recreation, text="Recreation",
                                  text_color=("white", "black"), height=60, width=260, anchor='w',
                                  font=("Helvetica", 25), fg_color='#57CC99', hover_color='#3F8F6C',
                                  command=showNatureMenu)
recreation_button.grid(row=3, column=0, padx=20, pady=30, sticky=W)


def optionmenu_callback(choice):
    if choice == 'Light Mode':
        ctk.set_appearance_mode('light')
    elif choice == 'Dark Mode':
        ctk.set_appearance_mode('dark')


space_label = ctk.CTkLabel(master=category_frame, height=200, text="")
space_label.grid(row=4, column=0)
darkmode_label = ctk.CTkLabel(master=category_frame, text_color=("black", "white"), font=("Helvetica", 14),
                              text="Appearance")
darkmode_label.grid(row=5, column=0, pady=15)
mode_dropdown = customtkinter.CTkOptionMenu(master=category_frame,
                                            values=["Light Mode", "Dark Mode"],
                                            dropdown_fg_color=('light grey', '#2B2B2B'), fg_color='#57CC99',
                                            button_color='#3F8F6C', button_hover_color='#2D664D',
                                            font=("Helvetica", 14),
                                            command=optionmenu_callback)
mode_dropdown.grid(row=6, column=0)

root.mainloop()
