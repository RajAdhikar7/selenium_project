

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WebDriver path .
driver = webdriver.Chrome(executable_path='C:/Users/icon/Desktop/selenium_django_assigment/env/Lib/site-packages/selenium/webdriver')

# open the form 
driver.get('https://forms.gle/WT68aV5UnPajeoSc8')

# filling out the form fields
name_field_xpath = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/input'
contact_number_field_xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
email_field_xpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
address_field_xpath ='/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea'
pin_code_field_xpath ='/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]'
date_field_xpath = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div'
gender_field_xpath = '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]'
captcha_field_xpath ='/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input'


# Fill out the form
driver.find_element(By.XPATH, name_field_xpath).send_keys('Rameshwar Adhikar')
driver.find_element(By.XPATH, contact_number_field_xpath).send_keys('9322404847')
driver.find_element(By.XPATH, email_field_xpath).send_keys('adhikarraj77@gmail.com')
driver.find_element(By.XPATH, address_field_xpath).send_keys('k9 building cidco n5 , aurangabad')
driver.find_element(By.XPATH, pin_code_field_xpath).send_keys('431003')
driver.find_element(By.XPATH, date_field_xpath).send_keys('15/07/2024')
driver.find_element(By.XPATH, gender_field_xpath).send_keys('Male')
driver.find_element(By.XPATH, captcha_field_xpath).send_keys('GNFPYC')

# Submit the form
submit_button_xpath = '/html/body/div[1]/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div'
driver.find_element(By.XPATH, submit_button_xpath).click() 

# Wait for the confirmation page to load
time.sleep(2)  # 

# Capture a screenshot of the confirmation page
driver.save_screenshot('confirmation.png')

# Close the browser
driver.quit()
