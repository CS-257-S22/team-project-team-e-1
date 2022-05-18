import csv
import sys
import random
import psycopg2
import psqlConfig as config

class DataSource:
        
    def __init__(self):
         self.connection = self.connect()

    def connect(self):
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def searchByTitle(self, title):
        """
            @description: Uses database query to return database row matching inputted title
            @params: A user inputted title
            @returns: None
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM movies WHERE title = %s"
            cursor.execute(query, (title,))
            movieDetails = list(cursor.fetchall()[0])
            return movieDetails
        except Exception as e:
            print("ERROR:Title not found.", file = sys.stderr)
            sys.exit(title)
            return None
        
    def getTopTenMovies(self):
        """
            @description: Uses database query to find ten movies with highest popularity 
            @params: None
            @returns: topTenMovies - list of tuples containing the ten most popular movies
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT title FROM populartitles ORDER BY popularity DESC LIMIT 10")
        topTenMovies = cursor.fetchall()
        return topTenMovies

    def incrementMoviePopularity(title):
        """
            @description: Uses database query to increment popularity of 
            @params: title - the movie that was just searched for in getMovie()
            @returns: None
        """
        cursor = self.connection.cursor()
        cursor.execute("UPDATE populartitles SET popularity = popularity+1 WHERE title = %s")
        
    def findMatchingMoviesHelper(self, parsedArgs):
        """
            @description: Uses database query to find movies matching the given filters
            @params: parsedArgs - the filters we are searching for
            @returns: cursor.fetchall() - the tupled list of matching movies
        """
        query = "SELECT * FROM movies WHERE"
        
        matchingMovies = []
        criteria = [[], [], [], [], [], [], [], [], [], [], [], []]
        categories = ["showtype", "title", "director", "actors", "country", "dateadded", "releaseyear", "rating", "duration", "genre", "synopsis", "platform"]
        criteria[0] = parsedArgs.getType()
        criteria[1] = parsedArgs.getTitle()
        criteria[2] = parsedArgs.getDirector()
        criteria[3] = parsedArgs.getCast()
        criteria[4] = parsedArgs.getCountry()
        criteria[5] = parsedArgs.getDateAdded()
        criteria[6] = parsedArgs.getYear()
        criteria[7] = parsedArgs.getRating()
        criteria[8] = parsedArgs.getDuration()
        criteria[9] = parsedArgs.getListedIn()
        criteria[10] = parsedArgs.getDescription()
        criteria[11] = parsedArgs.getService()
 
        firstCategory = True
        for i in range(11):
            if criteria[i] != []:
                if firstCategory:
                    query = query + " {} ILIKE '%{}%'"
                    query = query.format(categories[i], criteria[i][0])
                    firstCategory = False    
                else:        
                    query = query + " AND {} ILIKE '%{}%'"
                    query = query.format(categories[i], criteria[i][0])
        try:
            cursor = self.connection.cursor()
            cursor.execute(query,)
            return(cursor.fetchall())
        except Exception as e:
            print("ERROR: Parsed Args.", file = sys.stderr)
            sys.exit()
            return None
    
    def getAllMovies(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM movies")
        allMovies = cursor.fetchall()
        return allMovies


class Parser:
    '''@description: a class that takes command-line arguments from the user, tests them for correct format, and stores them to use in functions
       @args: command line filters inputted by the user at runtime
       @returns: None: creates object containing the inputted category and criterion'''
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
        self.service = []

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
                    elif category in ["-ser","-service"]:
                        self.service.append(args[i])    
                    else:
                        print("ERROR:Invalid command line arguments.")
                        printUsage("filters")
                    i += 1
            else:
                print("ERROR:Invalid command line arguments.")
                printUsage("filters")
            
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
    def getService(self):
        return self.service
    def isEmpty(self):
        return self.noArgs


def getMovie(parsedArgs):
    """
        @description: takes in a movie title, initializes the data, and searches for and returns a list containing all the info 
        pertaining to that movie
        @params: title - a str that provides the title of the movie
        @returns: movieInformation - a list that has the information of a movie
    """
    if (len(parsedArgs.title) < 1):
        printUsage("getMovie")
    title = parsedArgs.getTitle()[0] 
    title = title.strip()
    if len(title)==0:
        print("ERROR: Function getMovie needs a title argument (-ti \"title\"). ")
    database = DataSource()
    movieInformation = database.searchByTitle(title) #need to call dataSearch before increaseMoviePopularity
    return movieInformation #Definitely clearer, not sure if it's actually less code




def getRandomMovie(parsedArgs):
    """
        @description: gives a random movie suggestion based off given criteria (uses getMovie and findMatchingMovies)
        @params: parsedArgs - a Parser object containing the search criteria as specified in the command line
        @returns:  getMovie - a list of the movie info using the function getMovie() as a helper
    """
    
    if parsedArgs.isEmpty():
        database = DataSource()
        movieArray = database.getAllMovies()
        randInt = random.randint(0,len(movieArray)-1)
        return self.getMovie(movieArray[randInt].getTitle())
    
    else:
        filteredMovies = findMatchingMovies(parsedArgs)
        print(filteredMovies[0])
        if len(filteredMovies) == 0:
            return []
        randInt = random.randint(0,len(filteredMovies) - 1)
        
        parsedArgs = Parser(["-ti", filteredMovies[randInt]])
        return getMovie(parsedArgs)


def getPopularMovies():
    """
        @description: gives the most popular movie suggestions based off how often they have been searched for using getMovie and getRandomMovie
        @params: None
        @returns: popularMovieList - a list of the top 10 most popular movies as recorded in the populartitles database
    """
    database = DataSource()
    popularMovieList = list(database.getTopTenMovies())
    return popularMovieList


def increaseMoviePopularity(movieTitle):
    """
        @description: Helper function for getMovie() - Updates populartitles database when a movie is viewed (increases movie's popularity by 1)
        @params: movieTitle - the movie that was just searched for in getMovie()
        @returns: None
    """
    database = DataSource()
    database.incrementMoviePopularity(movieTitle)


def isCategory(category):
    """
        @description: Helper function for Parser class - helps determine if a category is one of the listed headings in the dataset
        @params: category - given category shorthand we are testing
        @returns: Boolean representing if the category was valid or not
    """
    if category in ["-ty","-type", "-ti",
        "-title", "-di", "-director", "-ca","-a", 
        "-cast","-co","-country","-da","-date_added", "-y", "-year", "-r", "-rating","-du","-duration","-g","-genre","-de","-description","-ser","-service"]:
        return True
    return False



def findMatchingMovies(parsedArgs):
    """
        @description: gives a list of titles of movies matching the given filters; does an AND search, so any title returned
        must match all of the criteria
        @params: parsedArgs - the filters we are searching for
        @returns: matchingMovies - a list of movies matching the criteria
    """
    dataSource = DataSource()
    movies =  dataSource.findMatchingMoviesHelper(parsedArgs)
    titles = []
    i = 0
    #helper fcn lists of tuples containing all the info for each movie, and we just want the title
    while i < len(movies):
        movie = list(movies[i])
        title = movie[1]
        titles.append(title)
        i = i + 1
    return titles


def Usage():
    """
        @description: Loads the usage statement as an array so that we may index the txt file
        @params: None
        @return: array containing each line of the usage statement as an element
    """
    with open("usage_message.txt") as f: # The with keyword automatically closes the file when you are done
        usageArray = []
        line = f.readline()
        while line:
         usageArray.append(line.strip())
         line = f.readline()
        
        return usageArray


def printUsage(functionName):
    """
        @descrption: prints either the general usage statement, or the statement
        for the desired function
        @params: function name
        @returns: None
    """
    usage = Usage()
    for i in range(0, 3):
        print(usage[i])
    if functionName == "general":
        for i in range(3, 24):
            print(usage[i])
    if functionName == "getMovie":
        for i in range(24, 30):
            print(usage[i])
    
    if functionName == "getRandomMovie":
        for i in range(30, 42):
            print(usage[i])
    
    if functionName == "findMatchingMovies":
        for i in range(42, 54):
            print(usage[i])
    
    if functionName == "getPopularMovie":
        for i in range(54, 61):
            print(usage[i])
    
    if functionName == "filters":
        for i in range(61, 83):
            print(usage[i])
    sys.exit(sys.argv)


def main():
    """
        @description: our main method that runs when main.py is called; checks if user input is incomplete and calls an error, 
        if not puts arguments into the Parser class and calls the correct function
        @params: None
        @returns: None
    """
    potentialFunctions = ["getMovie", "findMatchingMovies", "getRandomMovie", "getPopularMovies"]
    #print usage statements
    if(len(sys.argv) < 2):
        printUsage("general")
    if (sys.argv[1] not in potentialFunctions):
        if sys.argv[1] in ["help", "-help", "usage", "-usage"]:
            if(len(sys.argv) < 3):
                printUsage("general")
            functionName = sys.argv[2]
            if functionName in potentialFunctions:
                printUsage(functionName)
            if functionName == "filters":
                printUsage(functionName)
            else:
                printUsage("general")
        else:
            printUsage("general")

        

    #pull function and args
    functionName = sys.argv[1]
    parsedArgs = Parser(sys.argv[2:])
    if functionName == "getMovie":
        if (len(sys.argv) < 3):
            printUsage("getMovie")
        if (len(sys.argv) < 3):
            printUsage("getMovie")
        print(getMovie(parsedArgs))
    elif functionName == "findMatchingMovies":
        print(findMatchingMovies(parsedArgs))
    elif functionName=="getRandomMovie":
        print(getRandomMovie(parsedArgs))
    elif functionName == "getPopularMovies":
        print(getPopularMovies())   
    else:
        print("You should not be here... it is not possible. You have broken logic.", file = sys.stderr)
        sys.exit(functionName)


if __name__ == '__main__':
    main()
