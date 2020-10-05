from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https:\\automatetheboringstuff.com')
elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
print(elem)
elem.click()
#Simulates clicking the element
elem = browser.find_elements_by_css_selector('p')
#elementS, finds paragraph elements

browser.back()
#Goes back
browser.forward()
#Goes forward
browser.refresh()
#Refreshes page
browser.back()

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(9)')
print(elem.text())
 #Prints all the text within the element
elem = browser.find_element_by_css_selector('html')
#grabs the whole web page
print(elem.text())



searchElem = browser.find_element_by_css_selctor('.search-field')
searchElem.send_keys('zophie')
#types in the search bar
searchElem.submit()
#Finds html associated with submitting search

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(9)')
print(elem.text())

browser.quit()
#Exits out of the browser
