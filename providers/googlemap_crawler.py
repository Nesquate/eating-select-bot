import random
from time import sleep
from  selenium import webdriver    
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

class GoogleMapCrawler:
    def  __init__(self):
        chrome_options = Options() 
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--disable-gpu") 
        chrome_options.add_argument("--incognito")
        self.webdriver = webdriver.Chrome(options=chrome_options)
        

    def search(self, keyword):
        self.webdriver.get(f"https://www.google.com/maps/search/{keyword}/@24.1788232,120.6423018,16z/data=!3m1!4b1")
        html = self.webdriver.page_source
        soup = BeautifulSoup(html, "html.parser")

        self.result_all = soup.find_all("div", class_="bfdHYd") # Magic
        selected = self.result_all[round(random.randint(0, len(self.result_all)-1))]

        title = selected["aria-label"]
        rate = selected.find("span", class_="ZkP5Je")["aria-label"]
        address = selected.find("jsl").find_next("jsl").get_text()

        return (title, rate, address)


    def close(self):
        self.webdriver.close()