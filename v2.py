import csv
import time
from credentials import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


def load_wait_by_xpath(element_xpath):
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
    except TimeoutException:
        print("Loading took too much time!")


if user != '' and pwd != '':

    #connection
    driver = webdriver.Chrome()
    driver.get('https://linkedin.com')
    load_wait_by_xpath("//input[@id='session_key']")
    driver.find_element_by_xpath("//input[@id='session_key']").send_keys(user)
    driver.find_element_by_xpath("//input[@id='session_password']").send_keys(pwd)
    driver.find_element_by_xpath("//button[@class='sign-in-form__submit-button']").click()

    #groupe
    driver.get('https://www.linkedin.com/groups/'+str(group)+'/manage/membership/members/?page=15')
    time.sleep(5)

    for k in range(50):
        try:
            with open('output.csv', 'a') as output:
                csv_writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(
                    [driver.find_element_by_xpath("//div[@id='ember"+str(131 + 22 * k)+"']/span").text,
                     driver.find_element_by_xpath("//div[@id='ember"+str(133 + 22 * k)+"']/span").text])
        except NoSuchElementException:
            result = None
            x = 1
            while result is None and k <=48:
                try:
                    with open('output.csv', 'a') as output:
                        csv_writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csv_writer.writerow(
                            [driver.find_element_by_xpath("//div[@id='ember" + str(131 + x + 22 * k) + "']/span").text,
                             driver.find_element_by_xpath("//div[@id='ember" + str(133 + x + 22 * k) + "']/span").text])
                except:
                    pass
                x = x + 1
