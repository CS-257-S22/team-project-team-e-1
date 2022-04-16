import csv
import sys
import random

datasetsLoc = ['Data (CS257)/netflix_titles.csv','Data (CS257)/hulu_titles.csv','Data (CS257)/disney_plus_titles.csv','Data (CS257)/amazon_prime_titles.csv']
for i,file in enumerate(datasetsLoc):
    fullData = []
    with open(file, newline='') as csvfile:
        streamingData = csv.reader(csvfile)
        #print(type(data))
        for j,row in enumerate(streamingData):
            if i==0 and j==0:
                row.append("Streaming Service")
            elif i==0 and j!=0:
                row.append("Netflix")
            elif i==1 and j==0:
                row.append("Netflix")
            fullData.append(row)


def getRandomMovie(*kwargs):
    randInt
    if len(kwargs)==0:
        randInt = random.randint(0,len(fullData))
        print(fullData[randInt])
    for key, value in kwargs.items():
        if 


def main():
    print(f"Arguments count: {len(sys.argv)}")
    functionName = sys.argv[1]
    print("function name: ", functionName)
    if functionName=="getRandomMovie":
        if len(sys.argv) > 1
            getRandomMovie()

main()