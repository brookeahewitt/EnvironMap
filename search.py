from tkinter import *
import customtkinter as ctk
import tkintermapview
import requests
import json

key = 'AIzaSyCRkh-Rq03zC0Leg6McXYuqsEYRM4f6Tok' #REMOVE KEY

url = 'https://maps.googleapis.com/maps/api/place/search/json'

radius = '20000'


def restaurant(curr_location):
    param_type = 'restaurant|cafe'
    keyword = 'vegetarian|vegan|plant based'
    return do_search(param_type, keyword, curr_location)


def shopping(curr_location):
    param_type = 'store'
    keyword = 'second hand|used|thrift|vintage'
    return do_search(param_type, keyword, curr_location)


def transportation(curr_location):
    param_type = 'bicycle_store|bus_station'
    keyword = ''
    return do_search(param_type, keyword, curr_location)

def parks(curr_location):
    param_type = 'park'
    keyword = ''
    return do_search(param_type, keyword, curr_location)


def do_search(param_type, keyword, curr_location):
    global radius, key
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
