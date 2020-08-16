#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#storig 

firstname = ['Tevfik']
surname= ['Pehlivan']
email = [' email@gmail.com']
cell = ['5311112233']
birthdate = [4,4,2020]
password = ['1111xxxx****']
passwordrepeat = ['1111xxxx****']


#XpathUrl

inputFirstname = '//*[@id="account-firstName"]'		
inputSurname = '//*[@id="account-lastName"]'
inputEmail = '//*[@id="account-email"]'					
inputCell = '//*[@id="account-phone"]'
inputBirthdate = '//*[@id="account-birthDate"]'
inputPassword = '//*[@id="password-newPassword"]'
inputPasswordrepeat = '//*[@id="password-confirmPassword"]'			

#Check

gender = '//*[@id="account-genderMale"]'
emailnoticethick = '//*[@id="account-receiveEmail"]'
smsnoticethick = '//*[@id="account-receiveSms"]'
capthca = '/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]'		



#Submit
submit = '/html/body/div[3]/main/div[1]/div[2]/div/div/div/section/div/div/div/div/form/button'



def sleep():
	time.sleep(5)

browser = webdriver.Firefox()
browser.get('https://www.gratis.com/sign-up')


i = 0
while i < len(firstname):
	browser.find_element_by_xpath(inputFirstname).send_keys(firstname[i])
	browser.find_element_by_xpath(inputSurname).send_keys(surname[i])
	browser.find_element_by_xpath(inputEmail).send_keys(email[i])
	browser.find_element_by_xpath(inputCell).send_keys(cell[i])
	browser.find_element_by_xpath(inputBirthdate).send_keys(birthdate[i])
	browser.find_element_by_xpath(inputPassword).send_keys(password[i])
	browser.find_element_by_xpath(inputPasswordrepeat).send_keys(passwordrepeat[i])
	browser.find_element_by_xpath(gender).click()
	browser.find_element_by_xpath(emailnoticethick).click()
	browser.find_element_by_xpath(smsnoticethick).click()
	browser.find_element_by_xpath(capthca).click()	

	i += 1

	sleep()
	browser.back()
	sleep()

browser.quit()



	