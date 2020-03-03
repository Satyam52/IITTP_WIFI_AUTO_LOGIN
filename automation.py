from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')

chrome_browser = webdriver.Chrome(options=options)


chrome_browser.get('https://1.1.1.1/login.html')

user_Name = chrome_browser.find_element_by_name('username')
user_Name.clear()
user_Name.send_keys("CH18B004")
user_Pass = chrome_browser.find_element_by_name('password')
user_Pass.clear()
user_Pass.send_keys("CH18B004")
submit_Button = chrome_browser.find_element_by_name('Submit')
submit_Button.click()

chrome_browser.quit()
