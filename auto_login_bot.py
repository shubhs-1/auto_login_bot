from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
import random
import tkinter as tk
import credentials as cd
kybrd_list_left = ['Gmail','Facebook']
kybrd_list_right = ['LinkedIn','GitHub']
browser = None

def main():
    password="ABCD"
    tries = 0
    x = 3
    while tries < x:
        user_input = input("Please Enter Master Password: ")
        if user_input != password:
            tries +=1
            print('Incorrect Password, ' + str(x-tries) + '  more attempts left\n')
        else:
            tries = x+1
    if tries == x and user_input != password:
        sys.exit('Incorrect Password, terminating... \n')
    print("User successfully logged in!")
if __name__ == "__main__":
    main()

def onclick(k):
    global browser
    if browser is None:
        browser = webdriver.Chrome()
        browser.get('http://google.com')
    def click():
        if k == 'Gmail':
            gmaillogin()
        elif k == 'LinkedIn':
            linkedinlogin()
        elif k == 'Facebook':
            facebooklogin()
        elif k == 'GitHub':
            githublogin()

    return click

def gmaillogin():
    newclick()
    usernameStr = cd.gmail_user
    passwordStr = cd.gmail_pass
    browser.get('https://accounts.google.com/ServiceLogin?'
             'service=mail&continue=https://mail.google'
             '.com/mail/#identifier')
    emailElem = browser.find_element_by_id('identifierId')
    emailElem.send_keys(usernameStr)
    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click()
    time.sleep(3)
    passwordElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
    passwordElem.send_keys(passwordStr)
    signinButton = browser.find_element_by_id('passwordNext')
    signinButton.click()

def linkedinlogin():
    newclick()
    usernameStr = cd.link_user
    passwordStr = cd.link_pass
    browser.get('https://www.linkedin.com/uas/login')
    emailElem = browser.find_element_by_id('session_key-login')
    emailElem.send_keys(usernameStr)
    passwordElem = browser.find_element_by_id('session_password-login')
    passwordElem.send_keys(passwordStr)
    signinButton = browser.find_element_by_name('signin')
    signinButton.click()

def githublogin():
    newclick()
    usernameStr = cd.git_user
    passwordStr = cd.git_pass
    browser.get('https://github.com/login')
    emailElem = browser.find_element_by_id('login_field')
    emailElem.send_keys(usernameStr)
    passwordElem = browser.find_element_by_id('password')
    passwordElem.send_keys(passwordStr)
    signinButton = browser.find_element_by_name('commit')
    signinButton.click()

def facebooklogin():
    newclick()
    usernameStr = cd.face_user
    passwordStr = cd.face_pass
    browser.get(('https://www.facebook.com'))
    username = browser.find_element_by_id('email')
    username.send_keys(usernameStr)
    passwordElem = browser.find_element_by_id('pass')
    passwordElem.send_keys(passwordStr)
    nextButton = browser.find_element_by_id('loginbutton')
    nextButton.click()

def newclick():
    count=random.randint(1, 100)
    name = "tab"+str(count);
    tabname = "window.open('about:blank','tab"+str(count)+"');";
    browser.execute_script(tabname)
    browser.switch_to.window(name)

class SimpleGridApp(object):
    def __init__(self, master, **kwargs):
        self.keyboardButtons = []
        for i, k in enumerate(kybrd_list_left):
            button = tk.Button(root, text=k, width=10, relief='raised',
                               command=onclick(k),)
            button.grid(row=i, column=0)
            self.keyboardButtons.append(button)
        for i, k in enumerate(kybrd_list_right):
            button = tk.Button(root, text=k, width=10, relief='raised',
                               command=onclick(k),)
            button.grid(row=i, column=1)
            self.keyboardButtons.append(button)

root = tk.Tk()
root.wm_title("Vidushak")
app = SimpleGridApp(root, title="Vidushak")
root.mainloop()