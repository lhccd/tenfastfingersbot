import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.set_headless(headless=False)
driver = webdriver.Chrome(options=options, executable_path=os.path.join("..", "/Users/lorenz/PycharmProjects/FlexikonProject/chromedriver_for_mac"))

def print_start():
    print("***********************************")
    print("***********************************")
    print("Reaching out for immobilienscout24.com \n")
    print("BOT is started")
    print("***********************************")
    print("***********************************")

print_start()

driver.get('https://www.immobilienscout24.de/')

element = driver.find_element_by_partial_link_text('München')
print(element.get_attribute("href"))
element.click()

#lastpagenumber = driver.find_element_by_css_selector("#is24-qa-pager-numbers > li:nth-child(6) > a").text
#lastpagenumber
#searchsites = []
adlinklist = []
#i = 0
#print(lastpagenumber)
#while (i is not int(lastpagenumber)):
#    searchsites.append("https://www.immobilienscout24.de/wohnen/bayern,muenchen/mietwohnungen,seite-" + str(i) + ".html")
#    i = i+1
#    print(i)

#for i in searchsites:
#    driver.get(i)
adlinks = driver.find_elements_by_css_selector(".resultlist-title")
for e in adlinks:
    print(e.get_attribute("response.css('#is24-content div.criteriagroup.flex.flex--wrap.main-criteria-container > div:nth-child(2) > div:nth-child(1)::text').extract_first()href"))
    adlinklist.append(e.get_attribute("href"))



#nextpage.get_attribute("href").click()

driver.close()


#driver.execute_script("arguments[0].scrollIntoView();", element)