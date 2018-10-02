'''
Duckies - Daniel Gelfand and Ricky Lin
SoftDev1 pd6
K<14> -- Do I Know You?
2018-10-02
'''
from flask import Flask, render_template, session, request, url_for, redirect
import os

app = Flask(__name__)
#generate random string
app.secret_key = os.urandom(32)

error = ''

@app.route("/")
def home():
    #if user is in a session go to welcome page
    if request.cookies.get('session'):
        return render_template('log.html')
    #otherwise be at login page
    else:
        return render_template("index.html")

@app.route("/auth", methods=['GET'])
def login():
    #obtain inputted user and password
    user = request.args['user']
    pw = request.args['pw']
    #check if username and password match up
    if (user == 'Bob'):
        if (pw == 'Duck'):
            #adding data to session
            session['Bob'] = 'Duck'
            return render_template("log.html")
        else:
            error = 'Password not found'
    else:
            error = 'Username not found'

    return render_template('index.html', error = error)


@app.route("/logout")
def logout():
    #remove data from session
    session.pop('Bob')
    #redirect to root
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
