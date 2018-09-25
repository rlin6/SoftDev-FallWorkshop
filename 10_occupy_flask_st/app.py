#Living Tribunal: Dennis Chen, Ricky Lin
#SoftDev pd6
#K10: Jinja Tuning ...
#2018-09-24

#import flask methods
from flask import Flask, render_template 
from util import RHCP #import util as package

app = Flask(__name__)

@app.route("/")
def hello_World():
    return "<a href='/occupations'> No hablo queso! Click for greatness </a>"

@app.route("/occupations")
def occupations():
    #create a new empty dict
    occDict = {}
    #create the dictionary reading 3 columns of the csv 
    occDict = RHCP.occCreate("data/occupations.csv", occDict, 0, 2) 
    #pick a random occupation
    occChosen = RHCP.randomOcc(occDict) 
    return render_template('LivingTribunal_chenD-linR.html',
                            random = occChosen, #random job that appears
                            link = occDict[occChosen][1], #link of the random
                            _dict = occDict) #use dictionary in Jinja

if __name__ == '__main__':
    app.run(debug=True)
