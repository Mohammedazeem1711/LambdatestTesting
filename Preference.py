from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Preference:
    Username = "jumphubbell@gmail.com"
    Password = "Hubbell@123"
    ser_obj = Service("E:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.get("https://jumpcharge-env.ap-south-1.elasticbeanstalk.com/portal")
    driver.implicitly_wait(5000)
    driver.find_element(By.ID, "EmailId").send_keys(Username)
    driver.find_element(By.ID, "Password").send_keys(Password)
    driver.find_element(By.ID, "lnkLogin").click()
    driver.maximize_window()
    # To overcome overlapped element below lines of link argument
    link = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div")
    driver.execute_script("arguments[0].click();", link)
    std = driver.find_element(By.XPATH,
                              "/html/body/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/input")
    std.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    driver.implicitly_wait(3000)
    driver.find_element(By.XPATH,
                        "/html/body/div[3]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div/div[1]/div/div[1]/div[1]/div/input").send_keys(
        5)
    std_hrs = driver.find_element(By.XPATH, "//*[@id='txtStandardPerHour']")
    std_hrs.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    driver.implicitly_wait(3000)
    driver.find_element(By.XPATH, "//*[@id='txtStandardPerHour']").send_keys(24)
    driver.find_element(By.XPATH, "//*[@id='ulpaymentdashboard']/li[2]").click()
    driver.find_element(By.XPATH, "//*[@id='listAdd']").click()
    dom = driver.find_element(By.XPATH, "//*[@id='input0']")
    dom.send_keys("@hotmail.com")
    chkdisc = driver.find_element(By.XPATH, "//*[@id='chkDiscount']").is_selected()
    if chkdisc:
        print("Element checked - Seleceted Already")
    else:
        driver.find_element(By.XPATH, "//*[@id='chkDiscount']").click()
        print("Discount selected")
    disc = driver.find_element(By.XPATH, "//*[@id='txtDiscountUsd']")
    disc.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
    driver.find_element(By.XPATH, "//*[@id='txtDiscountUsd']").send_keys(6)
    driver.implicitly_wait(3000)
    sav = driver.find_element(By.XPATH, "//*[@id='btnSavePaymentConfiguration']")
    driver.execute_script("arguments[0].click();", sav)
    if sav:
        driver.find_element(By.XPATH, "/html/body/div[5]").is_displayed()
        print("Saved successfully")
    else:
        driver.find_element(By.XPATH, "//*[@id='btnpaymentsettingexceptcheckedout']").click()
        driver.find_element(By.XPATH, "//*[@id='btnAcceptImageProcessNotice']")
        print("Saved successfully after dialog box clicked")
