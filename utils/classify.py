import json
import requests
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3
from bs4 import BeautifulSoup
import re
visual_recognition = VisualRecognitionV3('2016-05-20', api_key='5f595de4e2614d19ccf7612b3fab7a77bba99ae1')

def get_ped_percentage(imageurl):
    global visual_recognition
    img_data = json.dumps(visual_recognition.classify(images_url=imageurl), indent=2)
    classifications = json.loads(img_data)["images"][0]["classifiers"][0]['classes']
    ret_val = 0
    #print (classifications)
    for classes in classifications:
        if ('pedestrian' in classes['class']):
            ret_val = float(classes['score'])
    return ret_val

def get_cam_image(url):
    url = url.strip()
    if ('multiview' in url):
        url = mutate_url(url)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    scripts = soup.find_all('script')[4]
    for x in scripts:
        ret = x
    start_point = ret.find(''''http://''')
    end_point = ret.find(".jpg'+'?math=';")
    url = (ret[start_point:end_point])[1:]+'.jpg'
    return (url)

def mutate_url(url):
    url = url.strip()
    start_point = url.find('=')
    return 'http://dotsignals.org/google_popup.php?cid=' + (url[start_point+1:])


def get_all_cams(camlist):
    ret_sum = 0
    for x in camlist:
        ret_sum += get_ped_percentage(get_cam_image(x))
    return ret_sum
#print (mutate_url('http://dotsignals.org/multiview2.php?listcam=983'))
#get_cam_image('http://dotsignals.org/google_popup.php?cid=503')
#http://dotsignals.org/multiview2.php?listcam=983

#get_ped_percentage("https://i.gyazo.com/613a0e1e6215f83c20cab7b17d08aca6.png")
#print (get_ped_percentage("http://207.251.86.238/cctv443.jpg"))
