import selenium.webdriver as webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
sneaker_name = []
website = "https://www.myntra.com/"
path = '/Users/shrishgupta/Downloads/chromedriver_mac64'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(website)
search_button = driver.find_element(
    "xpath", '//input[@placeholder="Search for products, brands and more"]')
search_button.send_keys("shoes")
enter_button = driver.find_element("xpath", '//a[@class="desktop-submit"]')
enter_button.click()
list1 = driver.find_elements(By.CLASS_NAME, "product-base")
for match in list1:
    text = match.find_element(By.CLASS_NAME, "product-product")
    word = driver.find_element("xpath", '//h4[@class="product-product"]').text
    if "Sneakers" in text.text:
        sneaker_name.append(text.text)


print("page1ends")
page_button2 = driver.find_element(
    "xpath", '//a[@href="https://www.myntra.com/shoes?p=2"]')
page_button2.click()
list2 = driver.find_elements(By.CLASS_NAME, "product-base")
for match2 in list2:
    text = match2.find_element(By.CLASS_NAME, "product-product")
    word = driver.find_element("xpath", '//h4[@class="product-product"]').text
    if "Sneakers" in text.text:
        sneaker_name.append(text.text)
        # sneaker_name.append(driver.find_element(
        # "xpath", '//h4[@class="product-product"]').text)
print("page2ends")
page_button3 = driver.find_element(
    "xpath", '//a[@href="https://www.myntra.com/shoes?p=3"]')
page_button3.click()
list3 = driver.find_elements(By.CLASS_NAME, "product-base")
for match3 in list3:
    text = match3.find_element(By.CLASS_NAME, "product-product")
    word = driver.find_element("xpath", '//h4[@class="product-product"]').text
    if "Sneakers" in text.text:
        sneaker_name.append(text.text)
print("page3ends")
page_button4 = driver.find_element(
    "xpath", '//a[@href="https://www.myntra.com/shoes?p=4"]')
page_button4.click()
list4 = driver.find_elements(By.CLASS_NAME, "product-base")
for match4 in list4:
    text = match4.find_element(By.CLASS_NAME, "product-product")
    word = driver.find_element("xpath", '//h4[@class="product-product"]').text
    if "Sneakers" in text.text:
        sneaker_name.append(text.text)
print("page4ends")
print(sneaker_name)
