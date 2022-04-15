import csv
import sys

with open('Data (CS257)/netflix_titles.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    #print(type(data))
    dataArray = []
    for row in data:
        dataArray.append(row)
    #print(dataArray[0][3])

def getMovie(title):
    curRow = 1
    curMovie = dataArray[curRow][2]
    if curMovie == title:
        return 



def main():
    print(f"Arguments count: {len(sys.argv)}")
    functionName = sys.argv[0]
    print("function name: ", functionName)

main()