from selenium import webdriver
import time

# Open chrome browser
browser = webdriver.Chrome()
# Get Request from url
browser.get('https://techstepacademy.com/trial-of-the-stones')
# Access input element
riddleStone = browser.find_element_by_css_selector('input[id="r1Input"]')
riddleStone.send_keys('rock')
# Access button of Riddle of Stone
riddleStoneBtn = browser.find_element_by_css_selector('button[id="r1Btn"]')
# print ('btn:', riddleStoneBtn)
# Click on Riddle of Stone button 
riddleStoneBtn.click()
# Access element of Riddle Stone answer
riddleStoneAnswer = browser.find_element_by_css_selector('div#passwordBanner > h4')
# Access text of element of Riddle Stone answer
riddleStoneText = riddleStoneAnswer.text

# Access Riddle of Secrets input 
riddleSecrets = browser.find_element_by_css_selector('input[id="r2Input"]')
# print(riddleSecrets)
riddleSecrets.send_keys(riddleStoneText)
# Access Riddle of Secrets button
riddleSecretsBtn = browser.find_element_by_css_selector('button#r2Butn')
# Click Riddle of Secrets button
riddleSecretsBtn.click()

# Two Merchants-Simple approach

# Access element with name of merchant with highest amount
richest_merchant_name = browser.find_element_by_xpath("//p[text()='3000'] /.. /span")
# Call text of element with merchant name
richest_merchant_name_txt = richest_merchant_name.text
# Access input of Two Merchants
merchant_input = browser.find_element_by_id('r3Input')
# Pass text of richest merchant to input
merchant_input.send_keys(richest_merchant_name_txt)
# Access button of Two merchants
merchant_answer_btn = browser.find_element_by_css_selector("button#r3Butn")
# Click on button of Two merchants
merchant_answer_btn.click()
# Access 'Check Answer' btn
check_btn = browser.find_element_by_css_selector('button[name="checkButn"]')
# Click on 'Check Answer' btn
check_btn.click()
# Access element that says 'Trial Complete'
complete_msg = browser.find_element_by_css_selector("div#trialCompleteBanner > h4")
# Assert 'Check Answer' text
assert complete_msg.text == 'Trial Complete'

print ('Final: ', complete_msg.text)

# Wait 4 seconds before closing
# time.sleep(4)
# Close browser
# browser.quit()
