from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/training-ground')
input_element = browser.find_element_by_css_selector('input[id="ipt1"]')
input_element.send_keys('My second automation')

button_element = browser.find_element_by_css_selector('button[name="butn1"]')
button_element.click()