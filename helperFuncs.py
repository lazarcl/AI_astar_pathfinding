from graphics import drawRectangle, fillRectangle

def mapreader(world):
    '''
    this reads the map file and creates a dict of cords=key terrain type=val.
    '''
    world.mapdict = {}   #key = cords   ,   value = blocktype
    worlddoc = open('map.txt', 'r')
    lineCount = 0
    world.tileWidth = 0
    for line in worlddoc:  #line is row
        line.strip()
        if len(line) > world.tileWidth:
            world.tileWidth = len(line)
        charCount = 0
        for char in line:  #char is col
            if char == '-':
                world.mapdict[(charCount, lineCount)] = 1 #walkable
            elif char == '#':
                world.mapdict[(charCount, lineCount)] = 0 #unwalkable
            elif char == 'T':
                world.mapdict[(charCount, lineCount)] = 2 #trail tile
            charCount += 1
        lineCount += 1
    world.tileHeight = lineCount

def mapSize():
    '''
    helper func that returns largest dimensions of map to use for calculating window size 
    '''
    worlddoc = open('map.txt', 'r')
    lineCount = 0
    width = 0
    for line in worlddoc:  #line is row
        line.strip()
        if len(line) > width:
            width = len(line)
        lineCount += 1
    return (width-1, lineCount)


def findTileFromCords(cords, tileSize):
    '''
    takes tuple of pixel cords in program window, and outputs tuple of cords of the tile that contains given cords. tile cords are
    the cords that are used to reference a tile in mapdict
    '''
    (x, y) = cords
    col = x/tileSize 
    row = y/tileSize 
    return (col, row)


def drawTileHelper(cords, tileSize, tileType):
    (x, y) = cords
    if tileType == 0: # walkable tile
        fillRectangle(x*tileSize, y*tileSize, tileSize, tileSize, 'red')
        drawRectangle(x*tileSize, y*tileSize, tileSize, tileSize)
    elif tileType == 1: # unwalkable tile
        fillRectangle(x*tileSize, y*tileSize, tileSize, tileSize, 'green')
        drawRectangle(x*tileSize, y*tileSize, tileSize, tileSize)
    elif tileType == 2: # trail tile
        fillRectangle(x*tileSize, y*tileSize, tileSize, tileSize, 'brown')
        drawRectangle(x*tileSize, y*tileSize, tileSize, tileSize)
    elif tileType == -1: #start tile
        fillRectangle(x*tileSize, y*tileSize, tileSize, tileSize, 'yellow')
        drawRectangle(x*tileSize, y*tileSize, tileSize, tileSize)
    elif tileType == -2: #dest tile
        fillRectangle(x*tileSize, y*tileSize, tileSize, tileSize, 'orange')
        drawRectangle(x*tileSize, y*tileSize, tileSize, tileSize)

















