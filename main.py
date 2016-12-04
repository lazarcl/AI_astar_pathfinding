from graphics import *
from helperFuncs import *
import random
import math

global tileSize 
tileSize = 22
(w,h) = mapSize()
makeGraphicsWindow(w*tileSize, h*tileSize)

#########split state polygon##########
#splits the states' lines up so the polygons can be graphed

#had to make new fips code to match both county and census data.

###dictionaries are used to store each counties ratio for that year/dataset
#for following dicts: key = FIPS code       value = ratio of native american/alaskan to total pop

#global cordlist = []
def start(world):
#for splashscreen...
    world.splashscreen = True
    mapreader(world)
    world.startCords = (1, 1)
    world.destCords = (1, 1)
 

        
    
def draw(world):
###splashscreen to tell user what this map is about
    if world.splashscreen == True:
        setBackground((240, 255, 255))
        drawString('A* pathfinding', 90, 57, size =32)
        drawString('by Cooper Lazar', 90, 95, size=17)
        drawString('leftclick to select start, rightclick to select destination', 90, 250, size = 26)
        drawString('press q to quit', 547, 510, size=24)
###fills counties with their colors using a separate func and then lays outlines on top. Also displays which years data is being projected
    else:
        #draw tiles
        for cord in world.mapdict:
            drawTileHelper(cord, tileSize, tileType=world.mapdict[cord])

        #draw start and dest tiles on top
        (startX,startY) = world.startCords
        drawTileHelper(world.startCords, tileSize, -1)

        tmpCords = findTileFromCords(getMousePosition(), tileSize)
        if world.mapdict[tmpCords] != 0:
            world.destCords = findTileFromCords(getMousePosition(), tileSize)
        drawTileHelper(world.destCords, tileSize, -2) 


        




###just listeners in here       
def updateWorld(world):
    onKeyPress(spacelistener, 'space')
    onKeyPress(quitlistener, 'q')
    onMousePress(recordmousecords)

    if world.splashscreen == False:
        print(world.startCords, world.destCords)


############################################Supporting Functions Below######################################

####listener for space which causes map data year to be cycled and splashscreen ended
def spacelistener(world, key):
    if world.splashscreen == True:
        world.splashscreen = False


###listener to quit graphics window
def quitlistener(world, key):
    endGraphics()

###This listenerfunction prints the mouse cords when clicked so that i could determine where to place text
def recordmousecords(world, x, y, button):
    cords = findTileFromCords((x,y), tileSize)
    if world.mapdict[cords] !=0:
        world.startCords = findTileFromCords((x,y), tileSize)






runGraphics(start, updateWorld, draw)