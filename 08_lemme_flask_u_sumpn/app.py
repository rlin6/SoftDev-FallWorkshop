#Ricky Lin
#SoftDev pd6
#K08: Fill Yer Flask
#2018-09-20

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_World():
    print(__name__) #terminal output
    return "<a href='/foo'> No hablo queso! </a>"

@app.route("/foo")
def cheez_it():
    return "<a href='/boo'> Cheese is Supreme </a>"

@app.route("/boo")
def lactose():
    return "<a href='/yoo'> Cheese & Crackers </a>"

@app.route("/yoo")
def cheesy():
    return "<a href='/'> Chuck E Cheese </a>"

if __name__ == '__main__':
    app.run(debug=True)
