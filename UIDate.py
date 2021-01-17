from selenium import webdriver 
from time import sleep
driver = webdriver.Firefox(executable_path = 'C:\\Users\\Ali Hanafiah\\Downloads\\geckodriver-v0.29.0-win64\\geckodriver.exe') 

url = "https://www.kompas.id/baca/opini/2021/01/14/krisis-lingkungan-dan-bencana-pandemi/"

def TestDate(driver, url):
    element = driver.find_elements_by_xpath("//*[@id='__layout']/div/div[2]/div/div[1]/div/article/div[3]/div[4]/div[1]/div[2]/time[1]")
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    try:            
        if match_iso8601( str_val ) is not None:
            statusTest='Pass'
    except:
        statusTest='Failed'
    
    return statusTest

statusDate = TestDate(driver, url)