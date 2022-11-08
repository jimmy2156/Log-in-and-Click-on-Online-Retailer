from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  driver = webdriver.Chrome(options = options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver


def main():
  driver = get_driver()
  driver.find_element(by="id", value="CustomerEmail").send_keys("gaganjot50266@gmail.com")
  driver.find_element(by="id", value="CustomerPassword").send_keys("21562156" + Keys.RETURN)
  time.sleep(3)




print(main())