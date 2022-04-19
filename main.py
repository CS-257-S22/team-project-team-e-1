import csv
import sys
import random
#from turtle import tiltangle


def initializeData():
    with open('Data (CS257)/netflix_titles.csv', newline='') as csvfile:
        data = csv.reader(csvfile)
        dataArray = []
        for row in data:
            dataArray.append(row)
    return dataArray

def getMovie(title):
    increaseMoviePopularity(title)
    print(title)
    title = title.strip()
    filmRow = dataSearch(title)
    if filmRow == None:
       print("Title not found", file = sys.stderr)
       return
    selectedMovieInfo = dataArray[filmRow]
    printList(selectedMovieInfo)
    return selectedMovieInfo#Definitely clearer, not sure if it's actually less code

def dataSearch(keyword):
    curRow = 1
    curMovie = dataArray[curRow][2]
    while curMovie != keyword:
        if curRow+1 == len(dataArray):
            return None
        curRow += 1
        curMovie = dataArray[curRow][2]
    return curRow

def printList(data):
    for datapoint in data:
        print(datapoint)


def getRandomMovie(parsedArgs):

    #first check if there are no args
    if parsedArgs.isEmpty():
        randInt = random.randint(0,len(dataArray)-1)
        print(dataArray[randInt])
        #also return it for testing
        return dataArray[randInt]
    
    else:
        #filter data using criteria in arguments (if no args, full data is used)
        filteredData = search(parsedArgs)
        #generate random number for this filter data
        randInt = random.randint(0,len(filteredData)-1)
        #return/print the random row from the subsetted data
        print(filteredData[randInt])
        return filteredData[randInt]


def getPopularMovies():
    finalList = []
    popularTitlesList = open("popularTitles.txt", 'r')
    for line in popularTitlesList:
        currline = line.split('|')
        if currline[0] == "Movie":
            #ensures that the popular list has only 10 movies 
            if len(finalList) != 10:
                finalList.append([currline[1], currline[2]])
                finalList = bubble_sort(finalList)
            #checks popularity of current movie with that of the least popular movie currently in the final list
            #always sorts after a change so the movies are always listed in ascending popularity order
            else:
                if finalList[0][1] < currline[2]:
                    finalList[0] = [currline[1], currline[2]]
                    finalList = bubble_sort(finalList)
    popularTitlesList.close()

    printTenMostPopularMovies(finalList)


#Helper function for getPopularMovies()
#reorganizes final list so only titles are printed (ie respective popularity ranks aren't shown)
def printTenMostPopularMovies(popularMovieList):    
    count = 0
    for title in popularMovieList:
        popularMovieList[count] = title[0]
        count += 1
    print(popularMovieList)


#Helper function for getMovie()
#Updates popularTitles.txt when a movie is viewed (increases movie's popularity)
def increaseMoviePopularity(movieTitle):
    allMoviesList = open('popularTitles.txt', 'r').readlines()
    
    movieNewPopularity = ""
    counter = 0

    #finds the movie that was viewed and adds 1 to its popularity tracker
    for movieInfo in allMoviesList:
        if movieTitle in movieInfo:
            tempMovieInfo = movieInfo.split('|')
            tempMovieInfo[2] = int(tempMovieInfo[2]) + 1
            tempMovieInfo[2] = str(tempMovieInfo[2])
            movieNewPopularity = '|'.join(tempMovieInfo)
            break
        counter += 1 
          
    #rewrites the popularTitles file to reflect the viewed movie's new popularity tracker
    allMoviesList[counter] = movieNewPopularity
    transferNewMoviesList = open('popularTitles.txt', 'w').writelines(allMoviesList)          


#This sorting algorithm was made by Santiago Valdarrama 
#and taken from https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python.
#Only the indices in the if statement were changed from the original function.
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j][1] > array[j + 1][1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

# a parser object to keep track of all the options used when searching the datset
class Parser:
    #initialize the parser by taking in args and assigning them by 
    def __init__(self):
        self.noArgs = True
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

        #error checking for length of args
        if len(sys.argv) < 2:
            print("Invalid command line arguments: need a command line function.")
            sys.exit(sys.argv)
        elif len(sys.argv) == 2:
            pass
        else:
            #signal that we have args
            self.noArgs = False
            #pull the arguments in a specified order

            for i in range(2, len(sys.argv), 2):
                curCategory = sys.argv[i]
                criterion = sys.argv[i]

                #error checking
                if criterion in ["-ty","-type", "-ti",
                "-title", "-d", "-director", "-c", 
                "-cast", "-y", "-year", "-r", "-rating"]:
                    print("Please provide an argument following " + criterion)
                    sys.exit(sys.argv)
                elif curCategory in ["-ty","-type"]:
                    self.type.append(criterion)
                elif curCategory in ["-ti","-title"]:
                    self.title.append(criterion)  
                elif curCategory in ["-d","-director"]:
                    self.director.append(criterion)
                elif curCategory in ["-c", "-a", "-cast"]:
                    self.cast.append(criterion)
                elif curCategory in ["-y","-year"]:
                    self.release_year.append(criterion)
                elif curCategory in ["-r","-rating"]:
                    self.rating.append(criterion)
                else:
                    print("Invalid command line arguments.")
                    sys.exit(sys.argv)

    def getType(self):
        return self.type
    def getTitle(self):
        return self.title
    def getDirector(self):
        return self.director
    def getCast(self):
        return self.cast
    def getYear(self):
        return self.release_year
    def getRating(self):
        return self.rating
    def isEmpty(self):
        return self.noArgs



def main():
    global dataArray 
    dataArray = initializeData()
    
    #pull function and args
    parsedArgs = Parser()
    functionName = sys.argv[1]
   
    if functionName=="getRandomMovie":
        getRandomMovie(parsedArgs)
    elif functionName == "getMovie":
        title = sys.argv[2]
        filmInfo = getMovie(title)
    elif functionName == "getPopularMovies":
        getPopularMovies()
    else:
        print("Function name not recognized-- please choose either getMovie, getRandomMovie, getPopularMovies, or search", file = sys.stderr)


main()