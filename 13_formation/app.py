#Ricky Lin
#SoftDev1 pd6
#K13: Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print(app)
    return render_template("index.html")

@app.route("/auth", methods=["GET", "POST"])
def auth():
    print(app)
    print(request)
    print(request.args)
    user = request.form['first'] + ' ' + request.form['last'] 
    return "Welcome " + user + " to my den. <br> You have reached here through a POST method" + '''<br><a href="/">If you want to leave</a>'''

if __name__ == '__main__':
    app.run(debug=True)

