from flask import Flask, render_template, url_for, request, redirect, flash, get_flashed_messages
from datetime import datetime

from logging import DEBUG
from forms import BookmarkForm

app = Flask(__name__)
app.logger.setLevel(DEBUG)


def getsecretkey():
    import os
    return os.urandom(24)


app.config["SECRET_KEY"] = getsecretkey()
from thermos.users import Users

bookmarks = dict()


def store_bookmarks(url, user="Deb", description=""):
    bookmarks[url] = [user, datetime.utcnow()]


def new_bookmarks(num):
    print sorted(bookmarks.items(), key=lambda bkm: bkm[1][1], reverse=True)[:num]
    return sorted(bookmarks.items(), key=lambda bkm: bkm[1][1], reverse=True)[:num]


@app.route('/')
@app.route("/index")
def index():
    # return 'Hello World!'
    # return render_template("index.html",
    #                        title = "Thermos Title passed from View",
    #                        text = ["Text1","Text2","Text3"])
    return render_template("index.html",
                           title="Thermos Title passed from View",
                           user=Users("Debabrata", "Patnaik"),
                           new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=["GET", "POST"])
def add():
    user = Users("Debabrata", "Patnaik")
    form = BookmarkForm()
    form.userform.data = user.getfullname()[:3]
    # if request.method == "POST":
    #     url = request.form["url"]
    #     user = request.form.get("user","Deb")
    #     store_bookmarks(url, user)
    #     app.logger.debug("Stored URL: " + url)
    #     flash("Stored URL: " + url)
    #     return redirect(url_for('index'))
    # return render_template("add.html")
    if form.validate_on_submit():
        print form.url.data, form.description.data
        try:
            print form.userform
        except Exception, exc:
            print exc
        url = form.url.data
        description = form.description.data
        user = form.userform.data

        store_bookmarks(url, user, description)
        app.logger.debug("Stored URL: " + url)
        flash("Stored URL: {}".format(url))
        return redirect(url_for("index"))
    return render_template("add.html", form=form, user=Users("Debabrata", "Patnaik"))


@app.errorhandler(404)
def pagenotfound(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def servererror(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
