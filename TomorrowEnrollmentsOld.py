from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import getpass

Uname = input("What is your LMS login username:  ") #ask for the username
Pword = getpass.getpass("What is your LMS login password:  ")  #ask for the password (getpass hides the keystrokes)

driver = webdriver.Chrome()
driver.get("""LoginPage""")#Launches Chrome to the login page

inputUserName = driver.find_element_by_name("UserName")  #This may need to be changed for different websites
inputUserName.send_keys(Uname)  #enter the username to the field on the webpage
inputPassword = driver.find_element_by_name("Password")  #This may need to be changed for different websites
inputPassword.send_keys(Pword)  #enter the password to the field on the webpage
signin = driver.find_element_by_id("login-submit")  #Find the Sign-In button.  This may need to be changed for different websites
signin.click()  #"Click" the "Sign In" button

driver.get("""Page with the dropdowns""")  #Go to the page that will be worked on

time.sleep(1)  #Pause for a second, the page is loading

x = 0
while x < 12:  #Infinite loop to ensure all of the dropdowns get changed
    if x < 10:
        x += 1
        drop = driver.find_element(By.XPATH, "//*[text()='Unknown']")  #find the element to change
        drop.click()  #Click on the dropdown

        attend = driver.find_element(By.XPATH, '//*[@id="changeCompletionStatus"]/div[2]')  #1=Unknown, 2=Attending, 3=No Show, 4=Complete; this marks everyone attending
        attend.click()
    else:
        driver.refresh()  #Refresh the page to solve a website glitch
        x = 1  #reset the counter to continue the loop
        time.sleep(1)  #pause for page load