from tkinter import *
import customtkinter as ctk
import tkintermapview
import requests
import json



url = 'https://maps.googleapis.com/maps/api/place/search/json'

radius = '392186.9'
curr_location = '38.03215, -78.48906'


def restaurant():
    param_type = 'restaurant|cafe'
    keyword = 'vegetarian|vegan|plant based'
    return do_search(param_type, keyword)


def shopping():
    param_type = 'store'
    keyword = 'second hand|used|thrift|vintage'
    return do_search(param_type, keyword)


def transportation():
    param_type = 'bicycle_store|bus_station'
    keyword = ''
    return do_search(param_type, keyword)


def do_search(param_type, keyword):
    global radius, curr_location, key
    params = {
        'location': curr_location,
        'radius': radius,
        'type': param_type,
        'keyword': keyword,
        'key': key
    }
    response = requests.get(url, params=params)
    data = json.loads(response.text)
    locations = []

    for result in data['results']:
        name = result['name']
        address = result['vicinity']
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        locations.append([name, address, lat, lng])

    return locations
