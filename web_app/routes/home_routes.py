from flask import Flask, Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def home():
    return render_template("index.html")

@home_routes.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)