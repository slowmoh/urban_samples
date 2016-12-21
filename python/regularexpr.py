print("hallo")

htmlFile = readFile("test.html")
#print(htmlFile)

imagelist = re.findall(r"<img.*?>", str(htmlFile))
#print(imagelist)  
#for eachimage in imagelist:
    #print(eachimage)
    
srclist = re.findall(r'src="([^"]+)"', str(imagelist))
for eachsrc in srclist:
    print(eachsrc)
print(len(srclist))


withouthttp = [] 
imagelist2 = re.findall(r'<img.*? src="([^"]+)".*?>', str(htmlFile))
for eachsrc2 in imagelist2:
    print(eachsrc2)
    match = re.match(r'http://.*?.de', str(eachsrc2))
    if match:
        print("was gefunden")
    else:
        print("nichts gefunden")
print(len(imagelist2))
    




exampleString = '''Jessica is 15 years old, and Daniel is 27 years old. Edward 
is 97, and this grandfather, Oscar, is 102. '''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

#print(ages)
#print(names)

ageDict = {}
x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1
    
#print(ageDict)