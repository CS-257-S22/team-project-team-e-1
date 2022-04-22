import csv
from flask import Flask
import main
 


app = Flask(__name__)
""" @description: Takes in the title inputted by the user, then modifies the underscores to spaces so it can be
taken by the get movie function
    @params: The title entered in the browser
    @returns: The same title with underscores instead of spaces"""
def helperParser(title):
    parsedTitle = ""
    for i in range(0, len(title)):
        if title[i] == '_':
            parsedTitle = parsedTitle + ' '
        else:
            parsedTitle = parsedTitle + title[i]
    return parsedTitle

""" @description: Standard/default route: prints a welcome message on the homepage. 
    @params: None
    @returns: home message"""
homepage_message = "Welcome to the homepage. Please type in /getMovie/<some_title> to view the data for that title-- If the movie title has multiple words,please separate them using underscores. For example, to search the movie Bird Box, you would type the url followed by /getMovie/Bird_Box."
@app.route('/')
def homepage():
    return homepage_message


""" @description: Starts up the getMovie function-- uses parameters in the browser to specify the title of the movie
    @params: /getMovie/<title>, with <title> replaced with user input
    @returns: Movie info for the selected title"""
@app.route('/getMovie/<title>', strict_slashes=False)
def getFilm(title):
    parsedTitle = helperParser(title)
    print(parsedTitle)
    return str(main.getMovie(parsedTitle))

"""
    @description: assigns the getRandomMovie function from main.py to a url.
    @params: args - a user input for what to randomized 
    @return: the string to be displayed on the webpage for random movie/show
"""
@app.route('/getRandomMovie/<category>/<args>/', strict_slashes=False)
def getRandomMovie(category,args) -> str:
    fullArgs = [category] + args.split("_")
    parsedArgs = main.Parser(fullArgs)
    return str(main.getRandomMovie(parsedArgs))

"""
    @description: displays the usage text as given by the usage_message.txt file
    @params: None - the file is predetermined
    @return: the string to be displayed on the webpage for usage
"""
@app.route('/usage/', strict_slashes=False)
def usage() -> str:
    with open("usage_message.txt") as f: # The with keyword automatically closes the file when you are done
        return f.read()

@app.errorhandler(404)
def page_not_found(e):
     return "sorry, wrong format. To get info from the dataset, enter URL/row/column, where URL is the URL provided by the program, row is the desired row, and column is the desired column"

@app.errorhandler(500)
def python_bug(e):
    return "Something went wrong with the program-- hopefully this bug will be fixed shortly."

if __name__ == '__main__':
    app.run()