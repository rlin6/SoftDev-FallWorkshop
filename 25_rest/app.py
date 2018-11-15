# Ricky Lin
# SoftDev1 pd06
# K #24: A RESTful Journey Skyward
# 2018-11-13

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/")
def home():

    #url requested using my key with the parameter of the date of 06/23 and hd quality
    mykey = 'https://opentdb.com/api.php?amount=10' 

    #get the http response
    response = urllib.request.urlopen(mykey)

    #reads the info received
    d = response.read()

    #turns the json into a dictionary
    data = json.loads(d)

    #test print
    print(data)

    #returns the template with the jinja placeholder as the url of the dictionary
    return render_template("index.html", question=data['results'][1]['question'], answer=data['results'][1]['correct_answer'])

if __name__ == '__main__':
    app.run(debug=True)

