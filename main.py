import webapp2
import random
class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movieList = ["Scarface", "LOTR(Any)", "Easy A", "Frozen", "The Big Lebowski"]
        # TODO: randomly choose one of the movies, and return it
        lotNum = random.randint(0,(len(movieList)-1))
        moviePic = movieList[lotNum]

        return moviePic

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        movieTomorrow = self.getRandomMovie()
        tomorrowCOntent = "<h1>Tomorrow's Movie</h1>"
        tomorrowCOntent += "<p>" + movieTomorrow + "</p>"

        self.response.write(content)
        self.response.write(tomorrowCOntent)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
