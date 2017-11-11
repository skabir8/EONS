from bs4 import BeautifulSoup
fp = open("test.html")
soup = BeautifulSoup(fp, "lxml")

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

for link in soup.find_all('input'):
    if link.get('type') == "checkbox":

        #output as string-- easier to read
        #print("Name: " + l3[j] + " Link: ""dotsignals.org/multiview2.php?listcam=" + link.get('value'))

        #output as a single dictionary (unordered)
        #d[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')

        #build dictionaries based on borough
        if j < 215:
            dmanhattan[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        elif j < 312:
            dbrooklyn[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        elif j < 349:
            dbronx[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        elif j < 516:
            dqueens[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        else:
            dstatenisland[l3[j]] = "dotsignals.org/multiview2.php?listcam=" + link.get('value')
        j = j + 1
        
#print(dmanhattan)
#print(dbrooklyn)
#print(dbronx)
#print(dqueens)
#print(dstatenisland)
#print(d)
