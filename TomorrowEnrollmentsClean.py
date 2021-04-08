from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import getpass

Uname = input("What is your LMS login username:  ") #ask for the username
Pword = getpass.getpass("What is your LMS login password:  ")  #ask for the password (getpass hides the keystrokes)

driver = webdriver.Chrome()
driver.get("<Login Page>")  #Launches Chrome to the login page

inputUserName = driver.find_element_by_name("UserName")  #This may need to be changed
inputUserName.send_keys(Uname)  #enter the username to the field on the webpage
inputPassword = driver.find_element_by_name("Password")  #This may need to be changed
inputPassword.send_keys(Pword)  #enter the password to the field on the webpage
signin = driver.find_element_by_id("login-submit")  #find the "Sign In" button
signin.click()  #"Click" the "Sign In" button

driver.get("<Page that will be worked on>")  #Go to the page that will be worked on

time.sleep(1)  #Pause for a second

x = 0
while x < 12:  #Infinite loop to ensure all of the dropdowns get changed
    if x < 10:
        x += 1
        try:
            drop = driver.find_element(By.XPATH, "//*[text()='Unknown']")  #find the element to change
            drop.click()  #Click on it
            attend = driver.find_element(By.XPATH, '//*[@id="changeCompletionStatus"]/div[2]')  #1=Unknown, 2=Attending, 3=No Show, 4=Complete; this marks everyone attending
            attend.click()
        except:
            x = 13  #exit the loop
    else:
        driver.refresh()  #Refresh the page to solve a website glitch
        x = 1  #reset the counter
        time.sleep(1)  #pause for page load

driver.quit()  #Close the browswer
time.sleep(1)
exit()  #End the program