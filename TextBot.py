import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.set_headless(headless=False)
driver = webdriver.Chrome(options=options, executable_path=os.path.join("..", "/Users/lorenz/PycharmProjects/TenFastfingersBot/chromedriver_for_mac"))

def print_start():
    print("***********************************")
    print("***********************************")
    print("Reaching out for 10fastfingers.com \n")
    print("BOT is started")
    print("***********************************")
    print("***********************************")

print_start()
#driver.get('https://10fastfingers.com/typing-test/german')
driver.get('https://10fastfingers.com/typing-test/german')
driver.implicitly_wait(30)

categorylist = driver.find_elements_by_css_selector('#row1 > span')

input = driver.find_element_by_css_selector('#inputfield')

for i,e in enumerate(categorylist) :
    print(str(i) + ": "+str(e.text))
    input.send_keys(str(e.text)+" ")