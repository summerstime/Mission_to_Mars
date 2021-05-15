from flask import Flask, render_template, redirect, url_for
from flask_pymongo import flask_pymongo
import scraping    # this imports the file that I made called scraping.py

# set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection to db named mars_app
app.config["MONGO_URI"]="mongodb://localhost:27017/mars_app"     # URI is Uniform Resource Indentifier
mongo = PyMongo(app)

# set up the routes
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)   # .update(query_parameter, data, options) format. {} empty JSON
    return redirect('/', code=302)            # redirect back to the home screen

if __name__ == "__main__":
    app.run()