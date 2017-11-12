


import json
import requests
from bs4 import BeautifulSoup
import re
import polyline
import cam_coors
#https://maps.googleapis.com/maps/api/directions/json?origin=Brooklyn&destination=Queens&mode=walking&alternatives=&key=AIzaSyCrIErnSCAoA07R_m9NqNIQNcuD0Cf3Vn4

def get_routes(origin,destination):
    ret_dic = {}
    origin_dat = cam_coors.getcoors(origin)
    desti_dat = cam_coors.getcoors(destination)
    base = 'https://maps.googleapis.com/maps/api/directions/json?'
    origin = 'origin=' + origin
    destination = '&destination=' + destination
    base += origin + destination + '&mode=walking&alternatives=true&key=AIzaSyCrIErnSCAoA07R_m9NqNIQNcuD0Cf3Vn4'
    data = requests.get(base).text
    dic = json.loads(data)
    poly_line = (dic['routes'])
    polyline_list = []
    poly_line_array = []
    rets=[]
    for i in range(2):
        polyline_list.append(poly_line[i]['overview_polyline']['points'])
    for i in polyline_list:
        pol_val = polyline.decode(i)
        poly_line_array.append(pol_val)
    for i in poly_line_array:
        ret_val = ''
        for vals in i:
            ret_val += '{lat: ' + str(vals[0]) + ',' + 'lng: ' + str(vals[1])+'}, '
        ret_val = ret_val[:-2]
        rets.append(ret_val)
    #print(poly_line_array)
    ret_dic['origin'] = origin_dat
    ret_dic['destination'] = desti_dat
    ret_dic['way1'] = rets[0]
    ret_dic['way2'] = rets[1]
    return ret_dic
#print (get_routes("858 Jamaica Ave, Brooklyn, NY 11208", "C-Town Supermarkets, 241 Taaffe Pl, Brooklyn, NY 11205"))
#print(polyline.decode('''mpjwFn`zaM`AzKvB`Nj@vCPp@dFxOvAhEcGxF}CxCUTY`@Yh@Qb@OdAEtALjADzAAn@Ed@Mr@Sr@o@`Bo@tAk@rA_@j@SX?JDRDNL\\bEl[t@bGAVmAjGcBxIyCpOqBpEaChFu@rAiCjD}GpIgB~BgDxGwAjCqApCgD|GaCvEc@~@N|Cd@rIf@xIFbAJ|@VrFXdHRxDlAzUjCri@Bf@dKxJjEhEUh@rGzF\\fHnChf@x@lNjIryApB|]gBT'''))
