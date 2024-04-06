from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Wait for element visibility
def wait_for_element(driver, by, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((by, locator))
    )

# Utilize function with error handling and element visibility check
def flipkart(driver):
    url = "https://www.flipkart.com/"
    driver.get(url)
    driver.maximize_window()

    try:
        # Search for the product
        search = wait_for_element(driver, By.XPATH, "(//input[@placeholder='Search for Products, Brands and More'])[1]")
        search_item = "Samsung Galaxy S10"
        search.send_keys(search_item + Keys.ENTER)
        
        # Apply filters
        time.sleep(2)  # Add explicit wait if needed
        samsung_btn = wait_for_element(driver, By.XPATH, "(//div[@class='_24_Dny'])[1]")
        assured_btn = wait_for_element(driver, By.XPATH, "(//div[@class='_24_Dny _3tCU7L'])[1]")
        price_filter_btn = wait_for_element(driver, By.XPATH, "(//div[normalize-space()='Price -- High to Low'])[1]")
        
        samsung_btn.click()
        time.sleep(2)
        assured_btn.click()
        time.sleep(2)
        price_filter_btn.click()
        time.sleep(10)
        
        # Scraping product details
        names = driver.find_elements(By.CLASS_NAME, "_4rR01T")
        prices = driver.find_elements(By.CLASS_NAME, "_25b18c")
        link_elements = driver.find_elements(By.CLASS_NAME, "_1fQZEK")
        
        links = [item.get_attribute("href") for item in link_elements]
        
        # Print details
        for i in range(len(names)):
            count = i + 1
            print(f"Product_no. {count}")
            print(f"Product_Name: {names[i].text}")
            price = prices[i].text.split('\n')[0]
            print(f"Display_Price: {price}")
            print(f"Link_To_Page: {links[i]}")
            print('\n')
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Initialize WebDriver
try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    flipkart(driver)
    
finally:
    # Close the WebDriver session
    if 'driver' in locals():
        driver.quit()