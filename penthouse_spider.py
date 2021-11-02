import scrapy
from scrapy.crawler import CrawlerProcess
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.set_headless(headless=False)
driver = webdriver.Chrome(options=options, executable_path=os.path.join("..",
                                                                        "/Users/lorenz/PycharmProjects/FlexikonProject/chromedriver_for_mac"))


def print_start():
    print("***********************************")
    print("***********************************")
    print("Reaching out for immobilienscout24.com \n")
    print("BOT is started")
    print("***********************************")
    print("***********************************")


print_start()

driver.get('https://www.immobilienscout24.de/')
driver.find_element_by_partial_link_text('München').click()

adlinklist = []
output = open("linklist_inserate2.txt", "a+")
try:
    while driver.find_element_by_partial_link_text('Nächste Seite') is not None:
        adlinks = driver.find_elements_by_css_selector(".resultlist-title")
        print(adlinks)
        for e in adlinks:
            ref = e.get_attribute("href")
            print(ref)
            adlinklist.append(ref)
            output.write(ref + "\n")
        driver.find_element_by_partial_link_text('Nächste Seite').click()
except:
    print("No next page clickable, session terminated.")

output.close()
driver.close()


class PenthouseSpider(scrapy.Spider):
    name = "penthouse"

    start_urls = adlinklist

    # start_urls = [
    #     'https://www.immobilienscout24.de/expose/108023046',
    #     'https://www.immobilienscout24.de/expose/107605401',
    #     'https://www.immobilienscout24.de/expose/108023046',
    #     'https://www.immobilienscout24.de/expose/107844457',
    #     'https://www.immobilienscout24.de/expose/102199351',
    #     'https://www.immobilienscout24.de/expose/106830508',
    #     'https://www.immobilienscout24.de/expose/107082498',
    #     'https://www.immobilienscout24.de/expose/103541616',
    #     'https://www.immobilienscout24.de/expose/107234570',
    #     'https://www.immobilienscout24.de/expose/104969656',
    #     'https://www.immobilienscout24.de/expose/107064641'
    # ]

    def parse(self, response):
        yield {
            'Titel': response.css('#expose-title::text').extract_first(),
            'Kaltmiete': response.css(
                '#is24-content div.criteriagroup.flex.flex--wrap.main-criteria-container > div:nth-child(1) > div:nth-child(1)::text').extract_first(),
            'Anzahl Zimmer': response.css(
                '#is24-content div.criteriagroup.flex.flex--wrap.main-criteria-container > div:nth-child(2) > div:nth-child(1)::text').extract_first(),
            'Fläche in qm': response.css(
                '#is24-content div.criteriagroup.flex.flex--wrap.main-criteria-container > div:nth-child(3) > div:nth-child(1)::text').extract_first(),
        }


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'csv',
    'FEED_URI': "immoscout_muenchen_mietwohnungen.csv"
})

#process.crawl(PenthouseSpider)
#process.start()
