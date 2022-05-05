from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")
driver.delete_all_cookies()
driver.maximize_window()
driver.get("https://www.google.com/")

searchFieldElement = driver.find_element(By.NAME, "q")
searchFieldElement.clear()
searchFieldElement.send_keys("agv helmet")
searchFieldElement.send_keys(Keys.ENTER)

driver.close()
