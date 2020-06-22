from selenium import webdriver
import time
import pyautogui

chrome_path = r" " #add your chrome webdriver path
driver = webdriver.Chrome(chrome_path)

driver.get("https://www.facebook.com/messages/t/")
time.sleep(3)

email_input = driver.find_element_by_id("email")
password_input = driver.find_element_by_id("pass")
login_button = driver.find_element_by_id("loginbutton")

email = " " #email
password = " " #pass
email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()


time.sleep(15)
contact = [" "] #name of people
search_input = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/label/input')
search_input.send_keys(contact[0])

time.sleep(3)
account = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a/div/div[2]/div/div')
account.click()

time.sleep(3)
text = "Hello"
text_box = driver.find_element_by_css_selector('.notranslate')
text_box.send_keys(text)

for i in range(50):
    pyautogui.typewrite("\n")
    pyautogui.typewrite(text)
    pyautogui.typewrite("\n")
    time.sleep(.5)
