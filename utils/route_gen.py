


import json
import requests
from bs4 import BeautifulSoup
import re
import polyline

#https://maps.googleapis.com/maps/api/directions/json?origin=Brooklyn&destination=Queens&mode=walking&alternatives=&key=AIzaSyCrIErnSCAoA07R_m9NqNIQNcuD0Cf3Vn4

def get_routes(origin,destination):
    base = 'https://maps.googleapis.com/maps/api/directions/json?'
    origin = 'origin=' + origin
    destination = '&destination=' + destination
    base += origin + destination + '&mode=walking&alternatives=on&key=AIzaSyCrIErnSCAoA07R_m9NqNIQNcuD0Cf3Vn4'
    data = requests.get(base).text
    dic = json.loads(data)
    print(base)
    return dic

#print (get_routes("74-39 Jamaica Ave, Woodhaven, NY 11421", "C-Town Supermarkets, 241 Taaffe Pl, Brooklyn, NY 11205"))
print(polyline.decode('''mpjwFn`zaM`AzKvB`Nj@vCPp@dFxOvAhEcGxF}CxCUTY`@Yh@Qb@OdAEtALjADzAAn@Ed@Mr@Sr@o@`Bo@tAk@rA_@j@SX?JDRDNL\\bEl[t@bGAVmAjGcBxIyCpOqBpEaChFu@rAiCjD}GpIgB~BgDxGwAjCqApCgD|GaCvEc@~@N|Cd@rIf@xIFbAJ|@VrFXdHRxDlAzUjCri@Bf@dKxJjEhEUh@rGzF\\fHnChf@x@lNjIryApB|]gBT'''))
