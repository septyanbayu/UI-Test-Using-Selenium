from selenium import webdriver 
from time import sleep
driver = webdriver.Firefox(executable_path = 'C:\\Users\\Ali Hanafiah\\Downloads\\geckodriver-v0.29.0-win64\\geckodriver.exe') 

url = "https://www.kompas.id/baca/opini/2021/01/14/krisis-lingkungan-dan-bencana-pandemi/"

def TestFont(driver, url):
    driver.get(url) 
    driver.set_page_load_timeout(90)
    id = driver.find_elements_by_xpath("//div[@class='content']/p")
    statusTest='Pass'
    for i in id:
        font = i.value_of_css_property("font-family")
        if font !='Georgia, Times New Roman, Times, serif':
            statusTest='Failed'
            break
    return statusTest

StatusFont = TestFont(driver, url)