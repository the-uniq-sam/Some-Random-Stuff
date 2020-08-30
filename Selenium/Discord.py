from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
time.sleep(15)
driver.get("http://www.discord.com/login")
time.sleep(30)
driver.find_element_by_name("email").send_keys("Enter your EMAIL here")
driver.find_element_by_name("password").send_keys("Enter your PASSWORD here")
driver.find_element_by_xpath("//button[@type='submit']").click()

#Now goto desired channel manually
a = 'n'
print("Now goto desired channel manually making sure typebox says Message #general and press y when done")
while(a!='y')
  a = input()
  print("Now goto desired channel manually making sure typebox says Message #general and press y when done")
time.sleep(3)

msg = driver.find_element_by_xpath("//div[@aria-label='Message #general']")
b = 1
while b==1:
  msg.send_keys("Pls beg")
  msg.send_keys(Keys.ENTER)
  time.sleep(30)
  msg.send_keys("Pls dep max")
  msg.send_keys(Keys.ENTER)
  time.sleep(11)

print("Script is now working, no need to print you noob")
