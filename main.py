from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://www.trendyol.com/")

wait = WebDriverWait(driver, 5)

search_box = driver.find_element(By.CLASS_NAME, "V8wbcUhU")
search_box.send_keys("Casper Excalibur Laptop")
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "cyrzo7gC")))

search_button = driver.find_element(By.CLASS_NAME, "cyrzo7gC")
search_button.click()


item_price = driver.find_elements(By.CLASS_NAME, "prc-box-dscntd")
item_name = driver.find_elements(By.CLASS_NAME, "prdct-desc-cntnr-name")

wait.until(expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "prc-box-dscntd")))
item_prices = []
item_names = []

for value in range(len(item_price)):
    item_prices.append(item_price[value].text)
    item_names.append(item_name[value].text)

data = {'Name': item_names, 'Price': item_prices}
new_data_frame = pd.DataFrame(data)

print(new_data_frame)