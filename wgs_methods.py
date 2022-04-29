import sys
from selenium import webdriver  # import selenium to the file
import wgs_locators as locators  # all variable take from wgs_locators file
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from radar import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # => add this for dropdown list


# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')

s = Service(executable_path='C://Users//GAURAV//PycharmProjects//pythonProject//chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setup():
    print("launch We GO study Application")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.wegosty_url)
    sleep(0.25)
    if driver.current_url == 'http://34.233.225.85/':
        print("Launched Successfully")
        sleep(0.25)
    else:
        print("Please check the code")
        teardown()


def teardown():
    if driver is not None:
        print('-----------------------------------****-----------------------')
        print('The test Completed at:', datetime.datetime.now())
        sleep(2)
        driver.close()
        driver.quit()

def login():
    driver.find_element(By.XPATH, "//button[@class='toast-close-button']").click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'LOGIN').click()
    sleep(1)
    driver.find_element(By.ID, 'user_email').send_keys(locators.consultant_email)
    sleep(1)
    driver.find_element(By.ID, 'user_password').send_keys('123cctb')
    sleep(1)
    driver.find_element(By.XPATH, "//input[@value='SIGN IN']").click()
    sleep(3)


def create_new_student():
    driver.find_element(By.LINK_TEXT, "My WeGoStudy").click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Students').click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Create New Student').click()
    sleep(0.25)
    driver.find_element(By.ID, 'user_student_detail_attributes_first_name').send_keys(locators.first_name)
    sleep(1)
    driver.find_element(By.ID, 'user_student_detail_attributes_last_name').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys('2022 04 26')
    sleep(0.25)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').clear()
    sleep(1)
    date = datetime.date(randint(1956, 2014), randint(1, 12), randint(1, 28))
    date_of_birth = str(date)
    driver.find_element(By.ID, 'user_student_detail_attributes_birth_date').send_keys(date_of_birth)
    sleep(0.25)
    # while(driver.find_element(By.XPATH, '//div[@class="datepicker-days"]//th//td[@class="datepicker-switch"]')).text:
    #     driver.find_element(By.XPATH, '//th[@class= "prev"]')


    # for dateelement in alldates:
    #     date = dateelement.text
    #     if date == '6':
    #         dateelement.click()
    #     break
    sleep(0.25)
    driver.find_element(By.ID, 'user_student_detail_attributes_passport_number').send_keys(locators.pass_number)
    sleep(0.25)
    driver.find_element(By.ID, 'select2-user_student_detail_attributes_country_of_citizenship-container').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@type="search"]').send_keys('Algeria')
    sleep(1)
    driver.find_element(By.XPATH, '//option[@value="DZ"]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'phone_number').send_keys(locators.phone_number)
    sleep(0.25)
    driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_apartment_number').send_keys(locators.apt_num)
    sleep(0.25)
    driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_mailing_address').send_keys(locators.mailing_address)
    sleep(0.25)
    #driver.find_element(By.XPATH, '//*[@class="chosen-container chosen-container-single chosen-with-drop chosen-container-active"]').click()
    # driver.find_element(By.XPATH, '//*[@class="chosen-container chosen-container-single"]').click()
    # sleep(0.25)
    # driver.find_element(By.XPATH, '//*[@class="chosen-search-input"]').send_keys('Canada')
    driver.find_element(By.LINK_TEXT, 'Country').click()
    sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/div/input').send_keys(f'Canada{Keys.ENTER}')
    sleep(0.6)
    print('searchbox')
    # driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_country_chosen"]/div/ul/li[39]').click()
    # sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Province/State').click()
    sleep(0.6)
    driver.find_element(By.XPATH, '//*[@id="user_student_detail_attributes_address_attributes_state_chosen"]/div/ul/li[3]').click()
    sleep(0.6)
    driver.find_element(By.LINK_TEXT, 'City').click()
    sleep(0.6)
    driver.find_element(By.XPATH,'//*[@id="user_student_detail_attributes_address_attributes_city_chosen"]/div/ul/li[30]').click()
    sleep(0.6)
    driver.find_element(By.ID, 'user_student_detail_attributes_address_attributes_zip_code').send_keys(locators.postal_code)
    sleep(0.6)
    driver.find_element(By.ID, 'user_email').send_keys(locators.user_email)
    sleep(0.6)



# def logout():
#     driver.find_element(By.XPATH, "//span[@class='my-auto mr-2 pf-name']").click()
#     sleep(1)
#     driver.find_element(By.LINK_TEXT, 'Log out').click()
#     sleep(1)
#     print("User can Successfully logout")


setup()
login()
create_new_student()
# logout()
