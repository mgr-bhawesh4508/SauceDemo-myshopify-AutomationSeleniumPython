from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
import time


#Code To maximize screen
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

#location to chromedriver
service = Service(r"C:\Users\97155\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Initialize the driver
driver= webdriver.Chrome(service=service, options=chrome_options)

# open Saucelabs
driver.get("https://sauce-demo.myshopify.com/account/login")

# wait for page to load
time.sleep(15)
# implicit wait

# close browser
driver.quit()