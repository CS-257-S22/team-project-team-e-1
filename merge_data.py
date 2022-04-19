import sys
import csv

datasetsLoc = ['Data (CS257)/netflix_titles.csv','Data (CS257)/hulu_titles.csv','Data (CS257)/disney_plus_titles.csv','Data (CS257)/amazon_prime_titles.csv']
for i,file in enumerate(datasetsLoc):
    fullData = []
    with open(file, newline='') as csvfile:
        streamingData = csv.reader(csvfile)
        #print(type(data))
        for j,row in enumerate(streamingData):
            if i==0 and j==0:
                row.append("Streaming Service")
            elif i==0 and j>0:
                row.append("Netflix")
            elif i==1 and j>0:
                row.append("Hulu")
            elif i==2 and j>0:
                row.append("Disney Plus")
            elif i==3 and j>0:
                row.append("Amazon Prime")
            fullData.append(row)
