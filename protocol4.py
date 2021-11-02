import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.set_headless(headless=False)
driver = webdriver.Chrome(options=options, executable_path=os.path.join("..", "/Users/lorenz/PycharmProjects/FlexikonProject/chromedriver_for_mac"))

driver.get('https://www.immobilienscout24.de/')
driver.find_element_by_partial_link_text('München').click()

output = open("linklist_inserate.txt", "a+")
try:
    while driver.find_element_by_partial_link_text('Nächste Seite') is not None:
        adlinks = driver.find_elements_by_css_selector(".resultlist-title")
        print(adlinks)
        for e in adlinks:
            ref = e.get_attribute("href")
            print(ref)
            output.write(ref + "\n")
        driver.find_element_by_partial_link_text('Nächste Seite').click()
except:
    print("No next page clickable, session terminated.")

output.close()
driver.close()
