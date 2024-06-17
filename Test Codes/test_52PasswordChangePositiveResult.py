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

class Test52PasswordChangePositiveResult():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_52PasswordChangePositiveResult(self):
    self.driver.get("https://x.com/home")
    self.driver.set_window_size(652, 726)
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(8) path").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(1) > .css-175oi2r > .css-175oi2r:nth-child(8) path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(8) .css-1jxf684").click()
    self.driver.find_element(By.LINK_TEXT, "Your account").click()
    self.driver.find_element(By.CSS_SELECTOR, ".css-175oi2r:nth-child(3) > .css-175oi2r > .css-175oi2r > .css-175oi2r > .css-146c3p1:nth-child(1) > .css-1jxf684").click()
    self.driver.find_element(By.NAME, "current_password").click()
    self.driver.find_element(By.NAME, "current_password").send_keys("veeshanji")
    self.driver.find_element(By.NAME, "new_password").click()
    self.driver.find_element(By.NAME, "new_password").send_keys("v33sh@nj")
    self.driver.find_element(By.NAME, "password_confirmation").click()
    self.driver.find_element(By.NAME, "password_confirmation").send_keys("v33sh@nj")
    self.driver.find_element(By.CSS_SELECTOR, ".r-q4m81j > .css-1jxf684:nth-child(1)").click()
  