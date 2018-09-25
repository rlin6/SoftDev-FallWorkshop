#Living Tribunal: Dennis Chen, Ricky Lin
#SoftDev pd6
#K10: Jinja Tuning ...
#2018-09-24

import random
from flask import Flask, render_template
from RHCP import occCreate, randomOcc, OCCLIST

app = Flask(__name__)

@app.route("/")
def hello_World():
    return "<a href='/occupations'> No hablo queso! Click for greatness </a>"

@app.route("/occupations")
def occupations():
    occDict = occCreate("data/occupations.csv", OCCLIST, 0, 2)
    occChosen = randomOcc(occDict) 
    return render_template('LivingTribunal_chenD-linR.html',random = occChosen, link = occDict[occChosen][1], _dict = occDict)

if __name__ == '__main__':
    app.run(debug=True)
