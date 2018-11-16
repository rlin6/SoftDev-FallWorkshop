# Ricky Lin
# SoftDev1 pd06
# K #26: Getting More REST
# 2018-11-16

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/")
def home():

    #url requested
    movie_stub = 'http://www.omdbapi.com/?apikey='

    #my key
    moviekey = '42b42999&'

    #the selection category
    movieselection = 't='

    #the query entry
    moviequery = 'naruto'

    movieurl = movie_stub + moviekey + movieselection + moviequery 
    bored_url = 'https://www.boredapi.com/api/activity'
    chuck_url = 'http://api.icndb.com/jokes/random/'

    #get the http response
    movieresponse = urllib.request.urlopen(movieurl)
    boredresponse = urllib.request.urlopen(bored_url)
    chuckresponse = urllib.request.urlopen(chuck_url)

    #reads the info received
    movie = movieresponse.read()
    bored = boredresponse.read()
    chuck = chuckresponse.read()


    #turns the json into a dictionary
    moviedata = json.loads(movie)
    boreddata = json.loads(bored)
    chuckdata = json.loads(chuck)

    #test print
    print(moviedata)
    print(boreddata)
    print(chuckdata)

    #returns the template with the jinja placeholder as the url of the dictionary
    return render_template("index.html", 
    title=moviedata['Title'], 
    pic=moviedata['Poster'], 
    activity=boreddata['activity'], 
    participants=boreddata['participants'], 
    joke=chuckdata['value']['joke'] )

if __name__ == '__main__':
    app.run(debug=True)

