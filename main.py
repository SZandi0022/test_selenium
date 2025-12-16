from re import search

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

import time


# تنظیمات chrom
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=Options()
)
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("detach", True)
driver.get("http://uitestingplayground.com/")

#کد
driver.get("https://www.google.com")
search_fild=driver.find_element("name","q")
search_fild.send_keys("selenium Automation testing")
search_fild.send_keys(Keys.RETURN)
search_fild.click()
time.sleep(30)