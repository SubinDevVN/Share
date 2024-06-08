#Tạo file account.txt, form username:pass mỗi tài khoản một dòng
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def status(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1;34m" + "[ Trạng thái ]:" + text + "\033[0m")
  
def load_accounts(file_path):
    accounts = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if ':' in line:
                accounts.append(line.strip().split(':'))
    return accounts

def login_roblox(username, password):
    try:
        status(f"Đăng nhập vào tài khoản {username}")
        driver = webdriver.Edge()
        driver.set_window_size(500, 500)
        driver.set_window_position(0, 0)
        driver.get("https://roblox.com/login")

        status("Đang nhập tài khoản")
        username_input = driver.find_element("id", "login-username")
        username_input.send_keys(username)
        time.sleep(1)

        status("Đang nhập mật khẩu")
        password_input = driver.find_element("id", "login-password")
        password_input.clear()
        for char in password:
            password_input.send_keys(char)
            time.sleep(0.2)  

        status("Đang đăng nhập")
        login_button = driver.find_element("id", "login-button")
        login_button.click()  
        time.sleep(10) 

        status("Đang tìm người dùng") 
        driver.get('https://www.roblox.com/users/{ id tài khoản cần follow }/profile?friendshipSourceType=PlayerSearch')
        time.sleep(5) 

        status("Tiến hành theo dõi") 
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "popover-link"))).click()
        time.sleep(5) 
        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Follow']"))).click()
        status("Theo dõi thành công")
        time.sleep(5)  
        driver.quit()

    except Exception as e:
        status(f"Lỗi: {str(e)}")

accounts = load_accounts('account.txt')

for username, password in accounts:
    login_roblox(username, password)
