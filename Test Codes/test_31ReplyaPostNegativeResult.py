# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test31ReplyaPostNegativeResult():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_31ReplyaPostNegativeResult(self):
    self.driver.get("https://x.com/home")
    self.driver.set_window_size(652, 726)
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(7) > .css-175oi2r > .css-175oi2r > .r-4qtqp9 path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(7) path").click()
    self.driver.find_element(By.XPATH, "//*[contains(@id, \'id__\')]//*[contains(@class, \'r-4qtqp9\')]").click()
    self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(2) > .css-175oi2r > .css-175oi2r:nth-child(1) > .css-175oi2r > .css-175oi2r > .css-146c3p1 path").click()
    self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block").send_keys("Sample")
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(2) > .css-175oi2r:nth-child(1) > .css-175oi2r:nth-child(1) > .css-175oi2r:nth-child(1) > .css-175oi2r:nth-child(1) > .css-175oi2r:nth-child(1) path:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(3) > .css-175oi2r:nth-child(2) .css-1jxf684 > .css-1jxf684").click()
    self.driver.execute_script("window.scrollTo(0,748.6666870117188)")
  
