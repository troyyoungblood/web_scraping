20210217_Homework_TY
## Web-scraping for information about Mars

This activity is the introduction to scraping information from the web and creating a visualization presenting various facts about Mars.

The following sites were visited for information:
<br>
The latest news  - (https://mars.nasa.gov/news/)
<br>
Facts about Mars - (https://space-facts.com/mars/)
<br>
Images of the Mars hemispheres - (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

Pandas was used to develop and test the code for scraping and saving the information to a MongoDB.  Once the code was varified in Pandas, a MongoDB with Flask templating was used to create a HTML page which renders the information that was scraped from the source locations referenced above.

Images of the rendered browser.
<br>
<br>
<img src="/Images/top_part.PNG">
<br>
<br>
<img src="/Images/middle.PNG">
<br>
<br>
<img src="/Images/bottom.PNG">

The following information is submitted for the activity
<br>
<br>
code folder
<br>
mission_to_mars_TY.ipynb - jupyter notebook used with Pandas to develop and test code to scrape the source locations
<br>
app.py - executed first, calls the scrap_mars.py and index.html files
<br>
scrape_mars.py - scrapes the infromation
<br>
<br>
templates folder
<br>
index.html - renders the information in a browser
<br>
<br>
Images folder
<br>
top_part.png - top of rendered page for placement in README file
<br>
middle.png - middle of rendered page for placement in README file
<br>
bottom.png - bottom of rendered page for placement in README file


