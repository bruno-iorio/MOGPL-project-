class Parser:
    def __init__(self,file):
        pass

    def parseFile(filename):
        dim = None
        listBlocked = []
        initX = None
        initY = None
        endX = None
        endY = None
        initOrientation = None
        with open(filename, "r") as f:
            ln = 0
            for line in file:
                if ln == 0:
                    dim = line.split()
                    dim[0] = int(dim[0])
                    dim[1] = int(dim[1])
                    dim[0] += 1
                    dim[1] += 1
                    
                elif ln <= dim[0]:
                    row = line.split()
                    for i in range(len(row)):
                        row[i] = int(row[i])
                    for x in range(len(row)):
                        if row[x] == 1:
                            listBlocked.extend([(x, y),(x+1,y),(x,y+1),(x+1,y+1)])
                elif ln == dim[0] + 1:
                    row = line.split()
                    initX, initY, endX, endY = int(row[0]), int(row[1]), int(row[2]), int(row[3])
                    initOrientation = row[4]
                else:
                    row = line.split()
                    if len(row) == 2 and row[0] == '0' and row[1] == '0':
                        break
                ln+=1 
        width = dim[0]
        length = dim[1]
        return width, length, initX, initY, endX, endY, initOrientation, listBlocked
    


