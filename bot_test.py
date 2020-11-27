from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument("--headless")
option.add_argument("disable-gpu")

print('Enter the gmailid and password') 
gmailId, passWord = map(str, input().split()) 

driver = webdriver.Chrome(options=option)
driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry = ServiceLogin') 

driver.implicitly_wait(15) 
  
loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]') 
loginBox.send_keys(gmailId) 
  
nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]') 
nextButton[0].click() 
  
passWordBox = driver.find_element_by_xpath( '//*[@id ="password"]/div[1]/div / div[1]/input') 
passWordBox.send_keys(passWord) 
  
nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]') 
nextButton[0].click()


# browser = webdriver.Chrome(options=option)

# browser.get("https://docs.google.com/forms/u/3/")

# textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
# radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
# checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
# submitbutton = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")

# textboxes[0].send_keys("Hello World")

# radiobuttons[2].click()

# checkboxes[1].click()
# checkboxes[3].click()

# submitbutton[0].click()