from bs4 import BeautifulSoup
import cam_coors
fp = open("test.html")
soup = BeautifulSoup(fp, "html.parser")

l = []
l2 = []
l3 = []
l4 = []

for y in soup.find_all('td'):#list showing inactive or active cameras
    if y.get('id') == "repCam__ctl0_lbNum": #check if its a camera
        l2.append(y.text.encode('utf-8'))


for x in soup.find_all('span'):
    l.append(x.text)
    #l.append(x.text.encode('utf-8'))

#this removes special characters from the names
for entry in l:
    entry = entry.encode('ascii',errors='ignore')
    l4.append(entry)


#delete entries that aren't names
del l4[0]
del l4[len(l4) - 1]
del l4 [len(l4) - 1]

for k in range(len(l2)):
    if not "Inactive" in l2[k]: #get rid of inactive cameras
        l3.append(l4[k])


j = 0
d = {}

dmanhattan = {}
dbrooklyn = {}
dstatenisland = {}
dqueens = {}
dbronx = {}


lmanhattan = []
lbrooklyn = []
lstatenisland = []
lqueens = []
lbronx = []

for link in soup.find_all('input'):
    if link.get('type') == "checkbox":

        #output as string-- easier to read
        #print("Name: " + l3[j] + " Link: ""dotsignals.org/multiview2.php?listcam=" + link.get('value'))

        #output as a single dictionary (unordered)
        #d[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')

        #build dictionaries based on borough
        if j < 215:
            lmanhattan.append(l3[j])
            dmanhattan[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        elif j < 312:
            lbrooklyn.append(l3[j])
            dbrooklyn[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        elif j < 349:
            lbronx.append(l3[j])
            dbronx[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        elif j < 516:
            lqueens.append(l3[j])
            dqueens[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        else:
            lstatenisland.append(l3[j])
            dstatenisland[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        j = j + 1


def pair_addr_w_coors(list):
    d = []
    i=0
    for address in list:
        coors = cam_coors.getcoors(address)
        d.append(coors)
        print (i, d)
        i+= 1
    return d

print(pair_addr_w_coors(lmanhattan))
'''
print(pair_addr_w_coors(lbrooklyn))
print(pair_addr_w_coors(lqueens))
print(pair_addr_w_coors(lbronx))
print(pair_addr_w_coors(lstatenisland))
'''
#print(lmanhattan)       
#print(dmanhattan)
#print(dbrooklyn)
#print(dbronx)
#print(dqueens)
#print(dstatenisland)
#print(d)

