from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # retrieve records from the mongo database mission_to_mars collection mars_HW12
    mars_data = mongo.db.mars_HW12.find_one()

    # Return template and data
    return render_template("index.html", mars_data = mars_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function - scrape_mars is the py file that is called 
    # the .scrape_info() is the return identified as mars_HW12_info in scrape_mars.py
    # this gets passed back up to the home route    
    mars_info = scrape_mars.scrape_info()

    #remove previous data from collection named mars_HW12
    mongo.db.mars_HW12.delete_many({})

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_HW12.insert_one(mars_info)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
