import csv
import sys

with open('Data (CS257)/netflix_titles.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    #print(type(data))
    dataArray = []
    for row in data:
        dataArray.append(row)
    #print(dataArray[0][2])



def main():
    print(f"Arguments count: {len(sys.argv)}")
    functionName = sys.argv[0]
    print("function name: ", functionName)

main()