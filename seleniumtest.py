"""
before running this make sure to add chromedriver.exe to your PATH variable or you will run into error"
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_google(query):
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(query)
    search.send_keys(Keys.RETURN)
    while True:
        pass
    
search_google('how to build a voice assistant in python')