#switch this to 1 or a fancy background pic
showBackgroundPic=1

#show overlap indicators (0=off, 1=on, default=0).
#combine with showCars=0 for best results
showIndicators=1

#show cars at all (0=off, 1=on, default=1)
showCars=1

#This is the zoom factor for the whole app.
#1.0-1.2 is normal on a 24" with full hd. Increase to have it bigger (e.g. 1.5), decrease to minimize (e.g. 0.7)
guiZoomFactor=1.2

#We can make the whole app semi-transparent, so it's even less disturbing. 1.0 = full opacity, 0.0 = invisible
maxiumAlpha=0.9

#Show title and background for x seconds
showTitle=5

#Update threshold: Do calculations every X seconds. 0 would be as often as possible, higher values won't
#let the map be smooth (but faster). Default is 0.03 ~= 30 fps
updateThreshold=0.03

#app name with version
helicorsaTitle = "helicorsa v4"

#world coordinates zoom or how big the bars are
worldzoom = 5.0

#painting offset, should match the window. better don't touch
xOff = 100.0
yOff = 100.0

#Distance threshold: How far away are the cars we paint?
distanceThreshold = 30.0
#Opacity threshold: At wich distance (in meters) should the cars start to fade?
#8 would be around 2 car lenghts
opacityThreshold = 8.0

#fade out cars in front of the player in an arc of X degrees (0 to disable)
frontFadeOutArc=90
#if a car in front is faded out, how soft should it fade? (again in degrees, 0 to disable = on/off, 10° is default and quite nice)
frontFadeAngle=10

#how big are the cars (in meters). Sorry, no data from ac available
carLength=4.3
carWidth=1.8

#draw with borders? set the border size in total pixel after zoom
carBorderThickness=1.0