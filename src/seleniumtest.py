
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getPriceAndStockStatus(url):
    driver=webdriver.Chrome()

    try:
        

        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        title=driver.title
        print(title)


        # price=driver.find_element(by=By.CLASS_NAME, value="price")
        # driver.implicitly_wait(1)
        # print(f"The price is ${price.text}")

        stock_status=''
        possible_stock_selectors = [
            (By.CLASS_NAME, "stock"),
            (By.CLASS_NAME, "proinfo"),
            (By.CLASS_NAME, "availability"),
            (By.XPATH, "//*[contains(@class, 'stock')]"),
            (By.XPATH, "//*[contains(@class, 'availability')]"),
            (By.XPATH, "//*[contains(text(), 'IN STOCK') or contains(text(), 'Out of stock')  or contains(text(), 'available') or contains(normalize-space(text()), 'In Stock'  or contains(text(), 'Available')]"),
            (By.XPATH, "//td[contains(text(), 'available')]") ,
            (By.XPATH, "//td[contains(text(), 'Stock')]/following-sibling::td") ,
            (By.XPATH, "//li[contains(text(), 'Availability')]"),
            (By.XPATH, "//*[@id='content']/div[2]/div/div/div[2]/ul/li[3]"),
            (By.XPATH, "//li[span[contains(text(), 'Availability')]]/text() | //li[span[contains(text(), 'Availability')]]/span/following-sibling::text()")
        ]
        # inStock=driver.find_elements(by=By.CLASS_NAME, value="product-usps-item")
        # driver.implicitly_wait(1)
        # for item in inStock:
        #     print(f"The price is ${item.text}")

        for by,value in possible_stock_selectors:
            try:
                stock_status=driver.find_elements(by, value)
                # for element in stock_status:
                if len(stock_status)>0 :
                  print(f"Stock status: ${stock_status[0].text} and value is ${value}")
                break

            except Exception as E:
                # print(f"Exception: ${E}")
                continue


    except Exception as e:
        print(e)


    driver.quit()

# getPriceAndStockStatus('https://www.cdkeys.com/xbox-live/xbox-game-pass-core-12-month-membership-ww')
# getPriceAndStockStatus('https://www.kinguin.net/category/12710/xbox-live-12-months-gold-eu-subscription-card#')
getPriceAndStockStatus('https://www.gamers-outlet.net/en/xbox/buy-xbox-game-pass-ultimate-3-month-cd-key-xbox-live-global-stackable')

# getPriceAndStockStatus('https://www.mmoga.com/Epic-Store-Games/Red-Dead-Redemption-Epic-Games-Store-EU-Greencode-Key.html')
# getPriceAndStockStatus('https://www.instant-gaming.com/en/3169-buy-xbox-game-pass-core-12-month-12-months-xbox-one-xbox-series-x-s-game-microsoft-store/?_gl=1*1hwn1hj*_up*MQ..&gclid=CjwKCAjw-JG5BhBZEiwAt7JR67MaNmlZ9usCj5265MM7blguvye4MPtL1IgL2CubQUf8fphp10y0wRoCB4AQAvD_BwE')
# getPriceAndStockStatus('https://www.hrkgame.com/en/games/product/call-of-duty-black-ops-6-cross-gen-edition-xbox-one-xbox-series-x?fss=search_list')


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import re

# # Function to get price and stock status
# def get_price_and_stock(url):
#     driver = webdriver.Chrome()
    
#     try:
#         driver.get(url)
#         WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

#         # Get the title of the page
#         title = driver.title
#         print(f"Title: {title}")

#         # Attempt to find price using common selectors
#         price = None
#         possible_price_selectors = [
#             (By.CLASS_NAME, "price"),
#             (By.XPATH, "//*[contains(@class, 'price')]"),
#             (By.XPATH, "//*[contains(@id, 'price')]"),
#             (By.XPATH, "//*[contains(text(), '$') or contains(text(), '£') or contains(text(), '€')]")
#         ]
        
#         for by, value in possible_price_selectors:
#             try:
#                 price = WebDriverWait(driver, 3).until(EC.presence_of_element_located((by, value)))
#                 if price and re.search(r"[\d.,]+", price.text):
#                     print(f"The price is: {price.text}")
#                     break
#             except:
#                 continue

#         # Attempt to find stock status using common selectors
#         stock_status = None
#         possible_stock_selectors = [
#             (By.CLASS_NAME, "stock"),
#             (By.CLASS_NAME, "availability"),
#             (By.XPATH, "//*[contains(@class, 'stock')]"),
#             (By.XPATH, "//*[contains(@class, 'availability')]"),
#             (By.XPATH, "//*[contains(text(), 'In stock') or contains(text(), 'Out of stock') or contains(text(), 'Available')]")
#         ]

#         for by, value in possible_stock_selectors:
#             try:
#                 stock_status = driver.find_element(by, value).text
#                 print(f"Stock status: {stock_status}")
#                 break
#             except:
#                 continue

#         if not price:
#             print("Price not found.")
#         if not stock_status:
#             print("Stock status not found.")

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     finally:
#         driver.quit()

# # Test with a sample URL
# get_price_and_stock("https://www.cdkeys.com/xbox-live/xbox-game-pass-core-12-month-membership-ww")

                                            # In Stock
                                    
