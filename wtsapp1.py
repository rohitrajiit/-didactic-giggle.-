from selenium import webdriver
b = webdriver.Firefox()
b.get('http://web.whatsapp.com')
input()
elem = b.find_element_by_xpath('//span[contains(text(),"Rahul Delhi")]')
elem.click()
elem1 = b.find_elements_by_class_name('input')
#while True:
elem1[1].send_keys('Hi')
b.find_element_by_class_name('send-container').click()
