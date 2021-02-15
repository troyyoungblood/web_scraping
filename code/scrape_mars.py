from splinter import Browser
from bs4 import BeautifulSoup
import requests
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/troyy/.wdm/drivers/chromedriver/win32/88.0.4324.96/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    ##  - - MARS NEWS  START - - --  

    # NASA Mars News url
    url_nmn = 'https://mars.nasa.gov/news/'

    # browser.visit seems to work better on this site
    # response = requests.get(url_nmn)
    browser.visit(url_nmn) 

    # time.sleep(5)

    # Creating an instance
    html = browser.html 
    soup2 = BeautifulSoup(html, 'html.parser')

    # just scraping the latest(top) article
    title_nmn = soup2.find_all('div', class_ = 'content_title')[1].text
    para_nmn = soup2.find('div', class_ = 'article_teaser_body').text

    # mars_news = {"title" : title_nmn, "para": para_nmn}

    browser.quit()

    ##  - - MARS NEWS  END - - --

    ##  - - MARS FACTS  START - - -- 

    # NASA Facts url
    url_mf = 'https://space-facts.com/mars/'

    # response seems to work better on this web page
    # browser.visit(url_mf)
    response = requests.get(url_mf)

    # time.sleep(5)

    # Creating an instance
    soup4 = BeautifulSoup(response.text, 'html.parser')

    # scraping fact table
    table_mf = soup4.find('tbody')

    mf_table_html_content = str(table_mf)
    # mars_facts = {"facts_table" : mf_table_html_content}

    browser.quit()

    ##  - - MARS FACTS  END - - --

    ##  - - MARS HEMISPHERE  START - - --

    #Mars Hemispheres - Cerberus
    url1_mh = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'

    #response works better with this site
    response = requests.get(url1_mh)

    soup5 = BeautifulSoup(response.text, 'html.parser')

    rel_path5 = soup5.find('div', class_='downloads')
    cerb_img = rel_path5.find('li').a['href']
    cerb_img

    #Mars Hemispheres - Schiaparelli
    url2_mh = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'

    #response works better with this site
    response = requests.get(url2_mh)

    soup6 = BeautifulSoup(response.text, 'html.parser')

    rel_path6 = soup6.find('div', class_='downloads')
    schi_img = rel_path6.find('li').a['href']
    schi_img

    #Mars Hemispheres - Syrtis Major
    url3_mh = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'

    #response works better with this site
    response = requests.get(url3_mh)

    soup7 = BeautifulSoup(response.text, 'html.parser')

    rel_path7 = soup7.find('div', class_='downloads')
    syrt_img = rel_path7.find('li').a['href']
    syrt_img

    #Mars Hemispheres - Valles Marineris
    url4_mh = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'

    #response works better with this site
    response = requests.get(url4_mh)

    soup8 = BeautifulSoup(response.text, 'html.parser')

    rel_path8 = soup8.find('div', class_='downloads')
    valle_img = rel_path8.find('li').a['href']
    valle_img

    hemisphere_info = [
        {"title" : "Cerberus Hemisphere", "img_url" : cerb_img},
        {"title" : "Schiaparelli Hemisphere", "img_url" : schi_img},
        {"title" : "Syrtis Major Hemisphere", "img_url" : syrt_img},
        {"title" : "Valles Marineris Hemisphere", "img_url" : valle_img}
        ]

    browser.quit()

    mars_HW12_info = {
    "title" : title_nmn,
    "para" : para_nmn,
    "table" : mf_table_html_content,
    "images" : hemisphere_info
    }

    # Return results
    return mars_HW12_info