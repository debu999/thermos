from flask import Flask, render_template, url_for

app = Flask(__name__)

from thermos.users import Users


@app.route('/')
@app.route("/index")
def index():
    # return 'Hello World!'
    # return render_template("index.html",
    #                        title = "Thermos Title passed from View",
    #                        text = ["Text1","Text2","Text3"])
    return render_template("index.html",
                           title="Thermos Title passed from View",
                           user=Users("Debabrata", "Patnaik"))


@app.route('/add')
def add():
    return render_template("add.html")


@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def servererror(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=False)
