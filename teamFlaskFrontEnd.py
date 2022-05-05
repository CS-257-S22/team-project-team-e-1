import csv
from flask import Flask, render_template, request
import main
 


app = Flask(__name__)
logosImg = ["https://cdn.vox-cdn.com/thumbor/Yq1Vd39jCBGpTUKHUhEx5FfxvmM=/39x0:3111x2048/1200x800/filters:focal(39x0:3111x2048)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png","https://upload.wikimedia.org/wikipedia/commons/e/e4/Hulu_Logo.svg,https://cdn.pastemagazine.com/www/articles/2019/10/18/disney-plus.jpg","https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Amazon_Prime_Video_logo.svg/2560px-Amazon_Prime_Video_logo.svg.png"]
logosLinks = ["https://www.netflix.com/browse","https://www.hulu.com","https://www.disneyplus.com/","https://www.amazon.com/Amazon-Video/b/?ie=UTF8&node=2858778011&ref_=nav_cs_prime_video"]

def getHomepage():
    """
        @description: displays the homepage text as given by the usage_message.txt file
        @params: None - the file is predetermined
        @return: the string to be displayed on the webpage for usage
    """
    with open("homepage.txt") as f: # The with keyword automatically closes the file when you are done
        return f.read()

homepage_message = str(getHomepage())
@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/search', methods =['GET', 'POST']) 
def functionSwitchboard():  
    if request.args['titleChoice']:
        title = request.args['titleChoice']
        parsedArgs = main.Parser(["-ti", title])
        result = main.getMovie(parsedArgs)
        return render_template('movieInfo.html', type = result[1], title = title, director = result[3], cast = result[4], locations = result[5], dateAdded = result[6], releaseYear = result[7], rating = result[8], runtime = result[9], genres = result[10], description = result[11], streamingService = result[12],logos = logosImg,links=logosLinks)
    else:
        return "other functionality not yet implemented"


@app.route('/popularmovies', strict_slashes=False)
def get_popular_movies():
    """
        @description: Returns a list of the most viewed movies as determined by popularMovies.txt 
        by running getPopularMovies() from main.py. 
        @return: getPopularMovies() - the list of popular movies, which here is casted to a string type. 
    """
    return render_template('matchingMovie.html', movies = main.getPopularMovies(), keyword="popular movies")



def getUsage():
    """
        @description: displays the usage text as given by the usage_message.txt file
        @params: None - the file is predetermined
        @return: the string to be displayed on the webpage for usage
    """
    with open("usage_message.txt") as f: # The with keyword automatically closes the file when you are done
        return f.read()


@app.route('/FAQs', strict_slashes=False) 
def FAQpage():
    return render_template('help.html')


@app.route('/usage/', strict_slashes=False)
def usage() -> str:
    return getUsage()


@app.errorhandler(404)
def page_not_found(e):
     return "Error: The URL you inputted did not map to a page. " + getHomepage()


@app.errorhandler(500)
def python_bug(e):
    return "Something went wrong with the program-- hopefully this bug will be fixed shortly."


if __name__ == '__main__':
    app.run()