from tkinter import *
import customtkinter as ctk
import tkintermapview

#google maps starter code from https://github.com/TomSchimansky/TkinterMapView

#create tkinter window
root = ctk.CTk()
root.title("EnvironMap")
root.geometry(f"{800}x{600}")

#create a map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=CENTER)

#set map to google maps
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

#set current widget position by address (change to current)
map_widget.set_position(38.033554, -78.507980)


root.mainloop()

