from selenium import webdriver

browser = webdriver.Chrome()
# print (browser)
browser.get('https://techstepacademy.com/trial-of-the-stones')

riddleOfStone = browser.find_element_by_css_selector('input[id="r1Input"]')
riddleOfStone.send_keys('rock')

riddleOfStoneButton = browser.find_element_by_css_selector('button[id="r1Btn"]')
riddleOfStoneButton.click()

riddleOfStoneAnswer = browser.find_element_by_css_selector('div#passwordBanner > h4')
riddleOfStoneText = riddleOfStoneAnswer.text
# print ("RiddleOfStoneAnswer: ", riddleOfStoneText)

riddleOfSecretsInput = browser.find_element_by_css_selector('input[id="r2Input"]')
riddleOfSecretsInput.send_keys(riddleOfStoneText)

riddleOfSecretsButton = browser.find_element_by_css_selector('button[id="r2Butn"]')
riddleOfSecretsButton.click()

# Two Merchants

# twoMerchantsFirst = browser.find_element_by_xpath("//div/span/b[text()][1]");
# print (twoMerchantsFirst)



browser.quit()



