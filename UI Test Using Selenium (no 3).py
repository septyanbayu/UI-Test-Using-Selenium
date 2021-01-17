# import org.openqa.selenium.By;
# import org.openqa.selenium.Dimension;
# import org.openqa.selenium.WebDriver;
# import org.openqa.selenium.chrome.ChromeDriver;

# public class GetElementSize {
# 	public static void main(String[] args) {
# 		// set chrome driver exe path
# 		System.setProperty("webdriver.firefox.driver", "'C:\\Users\\Ali Hanafiah\\Downloads\\geckodriver-v0.29.0-win64\\geckodriver.exe");
# 		WebDriver driver = new FirefoxDriver();
# 		driver.get("https://chercher.tech/selenium-webdriver-sample");
# 		// fetches text from the element and stores it in text
# 		Dimension size = driver.findElement(By.xpath("//button[contains(@class,'btn-primary')]")).getSize();
# 		System.out.println("Size of the button : "+ size);
# 	}
# }

from selenium import webdriver 
from time import sleep
driver = webdriver.Firefox(executable_path = 'C:\\Users\\Ali Hanafiah\\Downloads\\geckodriver-v0.29.0-win64\\geckodriver.exe') 

url = "https://www.kompas.id/baca/opini/2021/01/14/krisis-lingkungan-dan-bencana-pandemi/"

#opening link in the browser 
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

def TestFontSize(driver, url):
    array = 'Kecil Sedang Besar'
    driver.get(url) 
    driver.set_page_load_timeout(90)
    element = driver.find_elements_by_xpath("//*[@id='__layout']/div/div[2]/div/div[1]/div/article/div[3]/div[4]/div[2]/div[1]/div/button")
    element[0].click()
    print(element[0].text)
    element1 = driver.find_elements_by_xpath("//*[@id='__layout']/div/div[2]/div/div[1]/div/article/div[3]/div[4]/div[2]/div[1]/div/nav/ul/li[1]/button/div/p")
    print('-----------')
    print(element1[0])
    print(element1[0].text)
    print('-----------')
    # if array==element[0].text:
    #     print('sama')
    statusTest='Pass'
    return statusTest

def TestDate(driver, url):
    element = driver.find_elements_by_xpath("//*[@id='__layout']/div/div[2]/div/div[1]/div/article/div[3]/div[4]/div[1]/div[2]/time[1]")
    regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$'
    try:            
        if match_iso8601( str_val ) is not None:
            statusTest='Pass'
    except:
        statusTest='Failed'
    
    return statusTest

StatusFont = TestFont(driver, url)
statusDate = TestDate(driver, url)
statusFacebook = TestSocialMedia(driver, url, 'www.facebook.com', "//*[@id='__layout']/div/div[2]/div/div[1]/div/article/div[3]/div[4]/div[2]/div[2]/div/a[1]")
statusTwitter = TestSocialMedia(driver, url, 'https://twitter.com', "//*[@id='__layout']/div/div[2]/div/div[1]/div/article/div[3]/div[4]/div[2]/div[2]/div/a[2]")
statusWhatsApp = TestSocialMedia(driver, url, 'https://api.whatsapp.com', "//*[@id='__layout']/div/div[2]/div/div[1]/div/article/div[3]/div[4]/div[2]/div[2]/div/a[3]")
statusFontSize = TestFontSize(driver, url)
statusurlBerlangganan = TestBerlangganan(driver, url)
print('Status URL Berlangganan : ' +statusurlBerlangganan)
print('Status Date : ' +statusDate)
print('Status Facebok: ' +statusFacebook)
# print('Status Twitter: ' +statusTwitter)
print('Status WhatsApp: ' +statusWhatsApp)
print('Status Test Font : '+StatusFont)


