
from selenium import webdriver 
from time import sleep
driver = webdriver.Firefox(executable_path = 'C:\\Users\\Ali Hanafiah\\Downloads\\geckodriver-v0.29.0-win64\\geckodriver.exe') 

url = "https://www.kompas.id/baca/opini/2021/01/14/krisis-lingkungan-dan-bencana-pandemi/"
def TestSocialMedia(driver, url, name, path):
    driver.get(url) 
    driver.set_page_load_timeout(90)
    element = driver.find_elements_by_xpath(path)
    print(len(element))
    print(element[0])
    main_page = driver.current_window_handle
    element[0].click()
    sleep(5)
    for handle in driver.window_handles:
        if handle != main_page:
            switch_page = handle
    driver.switch_to.window(switch_page)
        
    curr_url = driver.current_url
    print(curr_url)
    if name in curr_url.lower():
        statusTest = 'Pass'
    else:
        statusTest = 'Failed'
    driver.close()
    return statusTest

statusFacebook = TestSocialMedia(driver, url, 'www.facebook.com', "//*[@id='__layout']/div/div[2]/div/div[1]/div/article/div[3]/div[4]/div[2]/div[2]/div/a[1]")