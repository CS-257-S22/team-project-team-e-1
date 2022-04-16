import csv
import sys
import random

def initializeData():
    with open('Data (CS257)/netflix_titles.csv', newline='') as csvfile:
        data = csv.reader(csvfile)
        #print(type(data))
        dataArray = []
        for row in data:
            dataArray.append(row)
    return dataArray

def getMovie():
    title = sys.argv[2]
    print(title)
    curRow = 1
    curMovie = dataArray[curRow][2]
    while curMovie != title:
        if curRow+1 == len(dataArray):
            print("Title not found", file = sys.stderr)
            exit()
        curRow += 1
        curMovie = dataArray[curRow][2]
    for item in dataArray[curRow]:
        print(item)



def getRandomMovie(*kwargs):
    randInt
    curData = dataArray[1]
    if len(kwargs)==0:
        randInt = random.randint(0,len(dataArray))
        print(dataArray[randInt])
        #also return it for testing
        return dataArray[randInt]
    else:
        #loop over all the possible options
        #pull the cases that match those options
        for key, value in kwargs.items():
            if key in ["-t","-type"]:
                for i in len(dataArray):
                    curValue = dataArray[i][1]
                    if value in curValue and dataArray[i] not in curData:
                        curData.append(dataArray[i])
            elif key in ["-g","-genre"]:
                for i in len(dataArray):
                    curValue = dataArray[i][10]
                    if value in curValue and dataArray[i] not in curData:
                        curData.append(dataArray[i])
            elif key in ["-d","-director"]:
                for i in len(dataArray):
                    curValue = dataArray[i][3]
                    if value in curValue and dataArray[i] not in curData:
                        curData.append(dataArray[i])
            elif key in ["-c","-cast"]:
                for i in len(dataArray):
                    curValue = dataArray[i][4]
                    if value in curValue and dataArray[i] not in curData:
                        curData.append(dataArray[i])
            elif key in ["-y","-year"]:
                for i in len(dataArray):
                    curValue = dataArray[i][7]
                    if value in curValue and dataArray[i] not in curData:
                        curData.append(dataArray[i])
            elif key in ["-r","-rating"]:
                for i in len(dataArray):
                    curValue = dataArray[i][8]
                    if value in curValue and dataArray[i] not in curData:
                        curData.append(dataArray[i])
            else:
                print("Invalid command line arguments.")
                sys.exit(kwargs)

        randInt = random.randint(0,len(curData))
        print(curData[randInt])
        return curData[randInt]


def main():
    global dataArray = initializeData()
    print(f"Arguments count: {len(sys.argv)}")
    functionName = sys.argv[1]
    numArgs = len(sys.argv)
    print("function name: ", functionName)
    if functionName=="getRandomMovie":
        myKwargs = {}
        for i in range(2, numArgs, 2):
            curCategory = sys.argv[i]
            specifiedCategory = sys.argv[i+1]
            myKwargs[curCategory] = specifiedCategory
        getRandomMovie(myKwargs)
    elif functionName == "getMovie":
        getMovie()

main()