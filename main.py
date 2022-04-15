import csv
import sys

with open('Data (CS257)/netflix_titles.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    #print(type(data))
    dataArray = []
    for row in data:
        dataArray.append(row)
    print(dataArray[2][2])

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




def main():
    print(f"Arguments count: {len(sys.argv)}")
    functionName = sys.argv[1]
    print("function name: ", functionName)
    if functionName == "getMovie":
        getMovie()

main()