import folium
import pandas as pd


# function to assign marker colors for each volcano based on elevation
def elevation_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# function to convert meters to feet
def meter_feet(hight):
    return round(hight / 3.28084)


# html link to seach for volcano on google
html = """
Volcano Name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s ft <br>
Status: %s <br>
Type: %s
"""


# Read the volcations.txt data and store them in lists
volcanoes = pd.read_csv("Interactive Map of Volcanoes/Volcanoes.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])
name = list(volcanoes["NAME"])
status = list(volcanoes["STATUS"])
types = list(volcanoes["TYPE"])


# Use folium to set the start map and zoom level
map = folium.Map(location=[37.0, -100.0], zoom_start=5, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

# loop through the volcanoes lists and apply to map
for lt, ln, el, name, status, types in zip(lat, lon, elev, name, status, types):

    # popup window with info about a the volcano
    iframe = folium.IFrame(html=html % (
        name, name, meter_feet(el), status, types), width=200, height=125)
    # set the marker and call the color function
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(
        iframe), icon=folium.Icon(color=elevation_color(el))))

map.add_child(fg)

# save to html
map.save("Map1.html")
