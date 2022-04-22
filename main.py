import csv
import sys
import random


# a class to store movie information in a neat organized fashion
class Movie:

    def __init__(self, movieInfo):
        self.movieInfo = movieInfo
        self.type = movieInfo[1]
        self.title = movieInfo[2]
        self.director = movieInfo[3]
        self.cast = movieInfo[4]
        self.country = movieInfo[5]
        self.date_added = movieInfo[6]
        self.release_year = movieInfo[7]
        self.rating = movieInfo[8]
        self.duration = movieInfo[9]
        self.listed_in = movieInfo[10]
        self.description = movieInfo[11]

    def getMovieInfo(self):
        return self.movieInfo
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

    
"""
                getMovie

    @description: initializes the dataset by pulling from csv, making movie objects, and putting them into an array.
    **THIS DOES NOT INCLUDE HEADER**
    @params: None
    @returns: None
"""
def initializeData():
    with open('Data/netflix_titles.csv', newline='') as csvfile:
        data = csv.reader(csvfile)
        movieArray = []
        next(data)
        for movie in data:
            movieObject = Movie(movie)
            movieArray.append(movieObject)

    return movieArray

"""
    @description: initializes the dataset by pulling from csv, making movie objects, and putting them into an array 
    @params: title - a str that provides the title of the movie
    @returns: movieInfo - a list that has the information of a movie
"""
def getMovie(title):
    title = title.strip()
    if len(title)==0:
        print("ERROR: Function getMovie needs a title argument (-ti \"title\"). ")
        printUsage()
        sys.exit(title)

    movieInfo = dataSearch(title) #need to call dataSearch before increaseMoviePopularity
    increaseMoviePopularity(title)
    return movieInfo #Definitely clearer, not sure if it's actually less code


"""
    @description: helper function for the method getMovie: actually finds the movie
    @params: keyword - a str giving the title of the film we are interested in finding
    @returns: MovieArray[index].getMovieInfo() - a list that has the information of a movie
"""

def dataSearch(keyword):
    movieArray = initializeData()
    keyword = keyword.strip()
    index = 0
    curMovie = movieArray[index].getTitle()
    while curMovie != keyword:
        if index+1 == len(movieArray):
            print("ERROR:Title not found.", file = sys.stderr)
            printUsage()
            sys.exit(keyword)
        index += 1
        curMovie = movieArray[index].getTitle()
    return movieArray[index].getMovieInfo()

"""
                    getRandomMovie

    @description: gives a random movie suggestion based off given criteria using getMovie and findMatchingMovies
    @params: parsedArgs - a Parser object containing the search criteria
    @returns:  getMovie (eventually a list) - the movie info coming from getMovie
"""

def getRandomMovie(parsedArgs):
    movieArray = initializeData()
    #first check if there are no args
    if parsedArgs.isEmpty():
        randInt = random.randint(0,len(movieArray)-1)
        #also return it for testing
        return getMovie(movieArray[randInt].getTitle())
    
    else:
        #filter data using criteria in arguments (if no args, full data is used)
        filteredMovies = findMatchingMovies(parsedArgs)
        #generate random number for this filter data
        randInt = random.randint(0,len(filteredMovies)-1)
        #return/print the random movie from the subsetted data
        return getMovie(filteredMovies[randInt])

"""

                    getPopularMovie

    @description: gives the most popular movies suggestion based off how often they have been searched for using getMovie and getRandomMovie
    @params: None
    @returns: finishedPopularMoviesList (eventually a list) - helper function
"""

def getPopularMovies():
    finalList = []
    popularTitlesList = open("popularTitles.txt", 'r')
    for line in popularTitlesList:
        currline = line.split('|')
        if currline[0] == "Movie":
            finalList = updatePopularMoviesList(finalList, currline)
    popularTitlesList.close()

    return finishedPopularMoviesList(finalList)

"""
    @description: helper method for popular movies
    @params: movieList - the list of popular movies we are editing , currentMovie - the movie that was just searched for
    @returns: movieList (list) - updated movieList
"""

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

"""
    @description: Helper function for getPopularMovies() - reorganizes final list so only titles are printed (ie respective popularity ranks aren't shown)
    @params: popularMovieList - the list of popular movies we are editing , currentMovie - the movie that was just searched for
    @returns: popularMovieList (list) - the final list to be displayed
"""

def finishedPopularMoviesList(popularMovieList):    
    count = 0
    for title in popularMovieList:
        popularMovieList[count] = title[0]
        count += 1
    return popularMovieList

"""
    @description: Helper function for getMovie() - Updates popularTitles.txt when a movie is viewed (increases movie's popularity)
    @params: movieTitle - the movie that was just searched for
    @returns: None
"""

def increaseMoviePopularity(movieTitle):
    file = open('popularTitles.txt', 'r')
    allMoviesList = file.readlines()
    
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
    file = open('popularTitles.txt', 'w')
    file.writelines(allMoviesList)  
    file.close()        

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

"""
                Parser

    @description: Helper function for Parser object - helps determine if a category is valid
    @params: category - given category shorthand we are testing
    @returns: Boolean
"""

def isCategory(category):
    if category in ["-ty","-type", "-ti",
        "-title", "-di", "-director", "-ca","-a", 
        "-cast","-co","-country","-da","-date_added", "-y", "-year", "-r", "-rating","-du","-duration","-g","-genre","-de","-description"]:
        return True
    return False

#a class that takes command-line arguments, tests them for correct format, and stores them to use in functions

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
                    elif category in ["-di","-director"]:
                        self.director.append(args[i])
                    elif category in ["-ca", "-a", "-cast"]:
                        self.cast.append(args[i])
                    elif category in ["-co", "-country"]:
                        self.country.append(args[i])
                    elif category in ["-da","-date_added"]:
                        self.date_added.append(args[i])
                    elif category in ["-y","-year"]:
                        self.release_year.append(args[i])
                    elif category in ["-r","-rating"]:
                        self.rating.append(args[i])
                    elif category in ["-du","-duration"]:
                        self.duration.append(args[i])
                    elif category in ["-g","-genre"]:
                        self.listed_in.append(args[i])
                    elif category in ["-de","-description"]:
                        self.duration.append(args[i])  
                    else:
                        print("ERROR:Invalid command line arguments.")
                        printUsage()
                        sys.exit(args[i])
                    i += 1
            else:
                print("ERROR:Incorrect definition of a category.")
                printUsage()
                sys.exit(args[i])
            
    #to access all the instance variables
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

"""

                findMatchingMovies

    @description: gives a list of all movies matching the given criteria (uses OR for multiple crtieria)
    @params: parsedArgs - the criteria we are searching for
    @returns: matchingMovies - a list of movies
"""

def findMatchingMovies(parsedArgs):
    movieArray = initializeData()

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
 
    #for each movie in the csv, check the content in each column
    #and see if it matches at least one of the search criteria.
    index = 0 
    while index < len(movieArray):
        for column in range(12):
            item = movieArray[index].getMovieInfo()[column]
            itemWords = item.split(",")
            for word in itemWords:
                for criterion in criteria[column]:
                    if criterion.lower() in word.lower(): 
                        title = movieArray[index].getTitle()
                        matchingMovies.append(title)
        index += 1

    return matchingMovies

"""
    @description: provides the usage statement
    @params: None
    @returns: None
"""

def printUsage():
    with open("usage_message.txt") as f: # The with keyword automatically closes the file when you are done
        print(f.read())

"""
    @description: our main method that runs when main.py is called and sorts the args
    @params: None
    @returns: None
"""

def main():
    potentialFunctions = ["getMovie", "findMatchingMovies", "getRandomMovie", "getPopularMovies"]
    if(len(sys.argv) < 2 or sys.argv[1] not in potentialFunctions):
        print("ERROR:No function in command line.")
        printUsage()
        sys.exit(sys.argv)
    #pull function and args
    functionName = sys.argv[1]
    parsedArgs = Parser(sys.argv[2:])
    if functionName == "getMovie":
        print(getMovie(parsedArgs.getTitle()[0]))
    elif functionName == "findMatchingMovies":
        print(findMatchingMovies(parsedArgs))
    elif functionName=="getRandomMovie":
        print(getRandomMovie(parsedArgs))
    elif functionName == "getPopularMovies":
        print(getPopularMovies())
    else:
        print("You should not be here... it is not possible. You have broken logic.", file = sys.stderr)
        printUsage()
        sys.exit(functionName)


if __name__ == '__main__':
    main()
