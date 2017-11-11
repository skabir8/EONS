from math import sqrt


def in_radius(pair1,pair2):
    #pair1 0 == latitude
    #pair1 1 == longitutde
    #pair2 0 == latitude
    #pair2 1 == longitutde
    p1 = pair1[0] - pair2[0]
    p2 = pair[1] - pair2[1]
    area = ((p1*p1) + (p2*p2))
    radius = 0.5
    if (area < radius):
        return True
    else:
        return False
