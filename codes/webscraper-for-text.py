##########################
## Description: Use selenium to scrape text from the body of a website
## Python 3 environment
## Install selenium with webdriver [https://selenium-python.readthedocs.io/installation.html] 
# ######################## 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

## Configure the web driver instance
options = Options()
options.add_argument('--headless') # headless browser so GUI is not shown
options.add_argument('--incognito')
driver = webdriver.Chrome(options=options)

url = 'https://www.google.com/'
driver.get(url)

try:
    elem = driver.find_element_by_tag_name('body') # locate the desired element
except:
    elem ='Error! No elements found'
finally:
    print(elem.text)

driver.close()
