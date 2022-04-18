import csv
import sys
import random
import argparse


def initializeData():
    with open('Data (CS257)/netflix_titles.csv', newline='') as csvfile:
        data = csv.reader(csvfile)
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



def getRandomMovie(**kwargs):
    curData = dataArray
    if len(kwargs)==0:
        randInt = random.randint(0,len(dataArray)-1)
        print(dataArray[randInt])
        #also return it for testing
        return dataArray[randInt]
    else:
        #loop over all the possible options
        #pull the cases that match those options
        for key, value in kwargs.items():
            if key in ["-t","-type"]:
                curData = [row for row in curData if value in row[1]]
            elif key in ["-g","-genre"]:
                curData = [row for row in curData if value in row[10]]  
            elif key in ["-d","-director"]:
                curData = [row for row in curData if value in row[3]]
            elif key in ["-c","-cast"]:
                curData = [row for row in curData if value in row[4]]
            elif key in ["-y","-year"]:
                curData = [row for row in curData if value in row[7]]
            elif key in ["-r","-rating"]:
                curData = [row for row in curData if value in row[8]]
            else:
                print("Invalid command line arguments.")
                sys.exit(kwargs)
        
        randInt = random.randint(0,len(curData)-1)
        print(curData[randInt])
        return curData[randInt]

class Parser:
    def __init__(self, args):
        
        self.type = []
        self.title = []
        self.director = []
        self.cast = []
        self.country = []
        self.date_added = []
        self.release_year = []
        self.rating = []
        self.duration = []
        self.listed_in = []
        self.description = []

        for i in range(2, len(args), 2):
            curCategory = sys.argv[i]
            criterion = sys.argv[i+1]
            if curCategory in ["-t","-type"]:
                self.type.append(criterion)
            elif curCategory in ["-t","-type"]:
                self.type.append(criterion)
            elif curCategory in ["-g","-genre"]:
                curData = [row for row in curData if value in row[10]]  
            elif curCategory in ["-d","-director"]:
                curData = [row for row in curData if value in row[3]]
            elif curCategory in ["-c","-cast"]:
                curData = [row for row in curData if value in row[4]]
            elif curCategory in ["-y","-year"]:
                curData = [row for row in curData if value in row[7]]
            elif curCategory in ["-r","-rating"]:
                self.rating.append(criterion)
            else:
                print("Invalid command line arguments.")
                sys.exit(kwargs)
            myKwargs[curCategory] = specifiedCategory



def main():
    global dataArray 
    dataArray = initializeData()
    print(f"Arguments count: {len(sys.argv)}")
    print(sys.argv)
    functionName = sys.argv[1]
    numArgs = len(sys.argv)
    print("function name: ", functionName)
   
    if functionName=="getRandomMovie":
        myKwargs = {}
        for i in range(2, numArgs, 2):
            curCategory = sys.argv[i]
            specifiedCategory = sys.argv[i+1]
            myKwargs[curCategory] = specifiedCategory
        getRandomMovie(**myKwargs)
    elif functionName == "getMovie":
        getMovie()

#usage should be for without function (specifies functions) and for certain function (gives criterion)

#if we want to implement argparse to make things cleaner
#  # Create the parser
#     parser = argparse.ArgumentParser()
#     # Add an argument
#     parser.add_argument('-g', '--genre', type=str, action='store_true', 
#     help="takes in a str formatted genre")
#     parser.add_argument('-g', '--genre', type=str, action='store_true', 
#     help="takes in a str formatted genre")
#     parser.add_argument('-r', '--rating', type=str, action='store_true', 
#     help="shows output")
#     # Parse the argument
#     args = parser.parse_args()
#     # Print "Hello" + the user input argument
#     print('Hello,', args.name)
main()