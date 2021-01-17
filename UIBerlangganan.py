from selenium import webdriver 
from time import sleep
driver = webdriver.Firefox(executable_path = 'C:\\Users\\Ali Hanafiah\\Downloads\\geckodriver-v0.29.0-win64\\geckodriver.exe') 

url = "https://www.kompas.id/baca/opini/2021/01/14/krisis-lingkungan-dan-bencana-pandemi/"

def TestBerlangganan(driver, url):
    driver.get(url) 
    driver.set_page_load_timeout(90)
    element = driver.find_elements_by_xpath("//*[@id='__layout']/div/div[1]/header/div/div[3]/div/div/a[2]/span")
    element[0].click()
    curr_url = driver.current_url
    if curr_url == 'https://gerai.kompas.id/belanja/harian-kompas/kompas-digital-premium':
        statusTest='Pass'
    else:
        statusTest='Failed'
    return statusTest


statusurlBerlangganan = TestBerlangganan(driver, url)