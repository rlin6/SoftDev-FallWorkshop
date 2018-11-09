from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print(app)
    return render_template("index.html")

@app.route("/auth")
def auth():
    print(app)
    print(request)
    print(request.args)
    return render_template

if __name__ == '__main__':
    app.run(debug=True)

