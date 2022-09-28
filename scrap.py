import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path

main_url = "https://library.bdrc.io/search?q={querry}~1&lg=bo&t=Etext&uilang=en"
DRIVER_PATH = "/Users/jungtop/Downloads/chromedriver.exe"
timeout = 10

def get_page(querry):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(main_url.format(querry=querry)) 
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'result-content'))
    WebDriverWait(driver, timeout).until(element_present)
    Path("./source_code.html").write_text(driver.page_source)
    soup = BeautifulSoup(driver.page_source,'html.parser')
    body = soup.find('body')
    divs = body.select("div.result-content.etext")
    print(len(divs))

def extract_page(page):
    soup = BeautifulSoup(page,'html.parser')
    works = soup.find_all("div",{"class":"result-content  etext"})

if __name__ == "__main__":
    querry = "།སྤོས་དང་དཔག་བསམ་ཤིང་དང་རིན་ཆེན་ཤིང་།"
    page = get_page(querry)
    #print(page)
    #extract_page(page)
    a = 0
