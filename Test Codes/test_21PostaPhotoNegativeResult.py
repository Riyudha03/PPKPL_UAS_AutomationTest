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

class Test21PostaPhotoNegativeResult():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_21PostaPhotoNegativeResult(self):
    self.driver.get("https://x.com/home")
    self.driver.set_window_size(652, 726)
    self.driver.find_element(By.CSS_SELECTOR, ".r-5vhgbc > .css-146c3p1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".public-DraftStyleDefault-block").send_keys("Sample")
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(1) > .css-175oi2r > .css-175oi2r:nth-child(2) > .css-175oi2r:nth-child(1) > .css-146c3p1 > .r-4qtqp9").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(1) > .css-175oi2r > .css-175oi2r:nth-child(1) > .css-175oi2r > .css-175oi2r > .css-146c3p1 > .r-4qtqp9").click()
    self.driver.execute_script("window.scrollTo(0,368)")
    self.driver.execute_script("window.scrollTo(0,108)")
    self.driver.find_element(By.CSS_SELECTOR, ".r-1hjwoze path").click()
  
