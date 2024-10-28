
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get('https://www.cdkeys.com/xbox-live/xbox-game-pass-core-12-month-membership-ww')

title=driver.title

driver.implicitly_wait(0.5)
print(title)


price=driver.find_element(By.ID, "product-price-19417")
driver.implicitly_wait(0.5)
price=driver.find_element(By.CLASS_NAME, "price")
driver.implicitly_wait(5)
print(f"The price is ${price}")

driver.quit()