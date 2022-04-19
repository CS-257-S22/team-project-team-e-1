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

def processGetMovie():
    title = sys.argv[2]
    filmInfo = getMovie(title)
    printList(filmInfo)

def getMovie(title):
    filmRow = dataSearch(title)
    if filmRow == None:
       print("Title not found", file = sys.stderr)
       return
    selectedMovieInfo = dataArray[filmRow]
    increaseMoviePopularity(title)
    return selectedMovieInfo#Definitely clearer, not sure if it's actually less code

def dataSearch(keyword):
    keyword = keyword.strip()
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
        return filteredData[randInt]


def getPopularMovies():
    finalList = []
    popularTitlesList = open("popularTitles.txt", 'r')
    for line in popularTitlesList:
        currline = line.split('|')
        if currline[0] == "Movie":
            finalList = updatePopularMoviesList(finalList, currline)
    popularTitlesList.close()

    return finishedPopularMoviesList(finalList)


#Helper function for getPopularMovies()
def updatePopularMoviesList(movieList, currentMovie):
    #ensures that the popular list has only 10 movies 
    if len(movieList) != 10:
        movieList.append([currentMovie[1], currentMovie[2]])
        movieList = bubble_sort(movieList)            
            
    #checks popularity of current movie with that of the least popular movie currently in the final list
    #always sorts after a change so the movies are always listed in ascending popularity order
    else:
        if movieList[0][1] < currentMovie[2]:
            movieList[0] = [currentMovie[1], currentMovie[2]]
            movieList = bubble_sort(movieList)

    return movieList


#Helper function for getPopularMovies()
#reorganizes final list so only titles are printed (ie respective popularity ranks aren't shown)
def finishedPopularMoviesList(popularMovieList):    
    count = 0
    for title in popularMovieList:
        popularMovieList[count] = title[0]
        count += 1
    return popularMovieList


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

'''
This sorting algorithm was made by Santiago Valdarrama 
and taken from https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python.
Only the indices in the if statement were changed from the original function.
'''
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


def isCategory(category):
    if category in ["-ty","-type", "-ti",
        "-title", "-d", "-director", "-c", 
        "-cast", "-y", "-year", "-r", "-rating"]:
        return True
    return False

class Parser:
    #takes command line arguments and parses them, sorts into categories
    #of search criteria. will have expanded utility in later iterations of the program
    def __init__(self, args):
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

        if len(args)>0:
            self.noArgs = False
        i = 0
        while i < len(args):
            if isCategory(args[i]):
                category = args[i]
                i += 1
                while (i < len(args)) and not isCategory(args[i]):
                    if category in ["-ty","-type"]:
                        self.type.append(args[i])
                    elif category in ["-ti","-title"]:
                        self.title.append(args[i])  
                    elif category in ["-d","-director"]:
                        self.director.append(args[i])
                    elif category in ["-c", "-a", "-cast"]:
                        self.cast.append(args[i])
                    elif category in ["-y","-year"]:
                        self.release_year.append(args[i])
                    elif category in ["-r","-rating"]:
                        self.rating.append(args[i])
                    else:
                        print("Invalid command line arguments.")
                        sys.exit()
                    i += 1
            

    def getType(self):
        return self.type
    def getTitle(self):
        return self.title
    def getDirector(self):
        return self.director
    def getCast(self):
        return self.cast
    def getCountry(self):
        return self.country
    def getDateAdded(self):
        return self.date_added
    def getYear(self):
        return self.release_year
    def getRating(self):
        return self.rating
    def getDuration(self):
        return self.duration
    def getListedIn(self):
        return self.listed_in
    def getDescription(self):
        return self.description
    def isEmpty(self):
        return self.noArgs



def findMatchingMovies(parsedArgs):
    matchingMovies = []
    criteria = [[], [], [], [], [], [], [], [], [], [], [], []]
    criteria[1] = parsedArgs.getType()
    criteria[2] = parsedArgs.getTitle()
    criteria[3] = parsedArgs.getDirector()
    criteria[4] = parsedArgs.getCast()
    criteria[5] = parsedArgs.getCountry()
    criteria[6] = parsedArgs.getDateAdded()
    criteria[7] = parsedArgs.getYear()
    criteria[8] = parsedArgs.getRating()
    criteria[9] = parsedArgs.getDuration()
    criteria[10] = parsedArgs.getListedIn()
    criteria[11] = parsedArgs.getDescription()
 
    #for each row in the csv, check the content in each column
    #and see if it matches at least one of the search criteria.
    row = 0 
    while row < len(dataArray):
        isMatch = True
        for column in range(12):
            item = dataArray[row][column]
            itemWords = item.split()
            for word in itemWords:
                if word.lower() in (criterion.lower() 
                for criterion in criteria[column]):
                    title = dataArray[row][2]
                    matchingMovies.append(title)
        row += 1

    return matchingMovies


def main():
    global dataArray 
    dataArray = initializeData()
    
    #pull function and args
    numArgs = len(sys.argv)
    functionName = sys.argv[1]
    parsedArgs = Parser(sys.argv[2:])

    if functionName == "findMatchingMovies":
        print(findMatchingMovies(parsedArgs))
    elif functionName=="getRandomMovie":
<<<<<<< HEAD
        myKwargs = {}
        numArgs = len(sys.argv)
        for i in range(2, numArgs, 2):
            curCategory = sys.argv[i]
            specifiedCategory = sys.argv[i+1]
            myKwargs[curCategory] = specifiedCategory
        getRandomMovie(**myKwargs)
    elif featureName == "getMovie":
        processGetMovie()
    else:
        printUsage()

def main():
    global dataArray 
    dataArray = initializeData()
    print(f"Arguments count: {len(sys.argv)}")
    print(sys.argv)
    if(len(sys.argv) < 2):
        printUsage()
    else:
        functionName = sys.argv[1]
        initialDirectoryPath(functionName)
    
    
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
=======
        print(getRandomMovie(parsedArgs))
    elif functionName == "getMovie":
        title = sys.argv[2]
        filmInfo = getMovie(title)
    elif functionName == "getPopularMovies":
        print(getPopularMovies())
    else:
        print("Function name not recognized-- please choose either getMovie, getRandomMovie, getPopularMovies, or search", file = sys.stderr)

>>>>>>> origin/main

if __name__ == '__main__':
    main()
