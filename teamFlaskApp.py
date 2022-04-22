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

""" @description: Loads movie data for processing
    @params: None
    @returns: None"""
def load_data():
    data = main.initializeData()
    rawData = [movie.getMovieInfo() for movie in data]

""" @description: Starts up the getMovie function-- uses parameters in the browser to specify the title of the movie
    @params: /getMovie/<title>, with <title> replaced with user input
    @returns: Movie info for the selected title"""
@app.route('/getMovie/<title>', strict_slashes=False)
def getFilm(title):
    parsedTitle = helperParser(title)
    print(parsedTitle)
    return str(main.getMovie(parsedTitle))

@app.errorhandler(404)
def page_not_found(e):
     return "sorry, wrong format. To get info from the dataset, enter URL/row/column, where URL is the URL provided by the program, row is the desired row, and column is the desired column"

@app.errorhandler(500)
def python_bug(e):
    return "Something went wrong with the program-- hopefully this bug will be fixed shortly."

if __name__ == '__main__':
    load_data()
    app.run()