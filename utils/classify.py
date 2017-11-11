import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='5f595de4e2614d19ccf7612b3fab7a77bba99ae1')

#print(json.dumps(visual_recognition.classify(images_url="https://i.gyazo.com/613a0e1e6215f83c20cab7b17d08aca6.png"), indent=2))
#print(json.dumps(visual_recognition.detect_faces(images_url="https://i.gyazo.com/0554982403e371aa04107b844fa5321f.png"), indent=2))

def get_ped_percentage(imageurl):
    global visual_recognition
    img_data = json.dumps(visual_recognition.classify(images_url=imageurl), indent=2)
    classifications = json.loads(img_data)["images"][0]["classifiers"][0]['classes']
    ret_val = 0
    for classes in classifications:
        if ('pedestrian' in classes['class']):
            ret_val = float(classes['score'])
    return ret_val


#get_ped_percentage("https://i.gyazo.com/613a0e1e6215f83c20cab7b17d08aca6.png")
