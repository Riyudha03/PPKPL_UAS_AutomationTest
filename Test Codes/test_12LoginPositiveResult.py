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

class Test12LoginPositiveResult():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_12LoginPositiveResult(self):
    self.driver.get("https://x.com/")
    self.driver.set_window_size(652, 726)
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(2) > .css-146c3p1 > .css-1jxf684:nth-child(1) > .css-1jxf684").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.NAME, "text").click()
    self.driver.find_element(By.NAME, "text").send_keys("veejadm")
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(6) .css-1jxf684 > .css-1jxf684").click()
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(" v33sh@nj")
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(2) > .css-175oi2r:nth-child(2) > .css-175oi2r:nth-child(2) .css-146c3p1:nth-child(1) > .css-1jxf684:nth-child(1) > .css-1jxf684:nth-child(1)").click()
  
