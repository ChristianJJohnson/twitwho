from flask import Flask

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes


DATABASE_URI = "sqlite:///web_app_99.db" # using relative filepath

def create_app():
    # initializes the app
    app = Flask(__name__)

    
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    # A blueprint in Flask is a template
    # for generating a "section" of a web application.
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app() # invokes the create_app function
    my_app.run(debug=True) # then runs the app