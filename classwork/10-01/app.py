from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/auth", methods=['GET'])
def login():
    user = request.args['user']
    pw = request.args['pw']
    if (user == 'Bob'):
        if (pw == 'Duck'):
            return render_template("log.html")
        else:
            return 'Password is incorrect'
    else:
        return 'Username not found'
        
@app.route("/logout")
def logout():
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

