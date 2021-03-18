
from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    title = "Home Page"
    pageHeader = "This is the home page it is cool!"
    return render_template("home.html", title=title, pageHeader=pageHeader)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
