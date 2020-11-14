import csv
import time
from selenium import webdriver
from credentials import *


# functions
def parsename(x):
    name = driver.find_element_by_xpath(
        "//div[contains(@id, 'ember"+str(x)+"')]/span"
    ).text
    return name


def parsebio(x):
    bio = driver.find_element_by_xpath(
        "//div[contains(@id, 'ember"+str(x+2)+"')]/span"
    ).text
    return bio

# selenium webdriver, change it here if you use another browser
driver = webdriver.Chrome()

# connection
print('Logging in...')
driver.get('https://linkedin.com')
time.sleep(2)
sign_in_button = driver.find_element_by_class_name('nav__button-secondary')
sign_in_button.click()
time.sleep(2)
id_box = driver.find_element_by_id('username')
id_box.send_keys(user)
pass_box = driver.find_element_by_id('password')
pass_box.send_keys(pwd)
sign_in_button_2 = driver.find_element_by_class_name('btn__primary--large')
sign_in_button_2.click()
time.sleep(2)

# load group
print('Finding group...')
page = 1
driver.get('https://www.linkedin.com/groups/'+group+'/manage/membership/members/?page='+str(page))
time.sleep(5)

# page 1
for page in range(first, last):
    print('Parsing page '+str(page)+'...')
    driver.get('https://www.linkedin.com/groups/'+str(group)'/manage/membership/members/?page='+str(page))
    time.sleep(5)
    x = 131
    for y in range(1, 51):
        try:
            with open('output.csv', 'a') as output:
                csv_writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([parsename(x), parsebio(x)])
        except:
            result = None
            while result == None and x <=1300 :
                try:
                    x = x + 1
                    result = parsename(x)
                    with open('output.csv', 'a') as output:
                        csv_writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        csv_writer.writerow([parsename(x), parsebio(x)])
                except:
                    pass
                print('Error, for x='+str(x)+'at page '+str(page))
        x = x + 22
    time.sleep(60)

# rest of the pages
#for page in range(first, last):
#    print('Parsing page '+str(page)+'...')
#    driver.get('https://www.linkedin.com/groups/'+str(group)'/manage/membership/members/?page='+str(page))
#    time.sleep(60)
#    x = 40
#    for y in range(0, 50):
#        x = x+27
#        try:
#            with open('output.csv', 'a') as output:
#                csv_writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                csv_writer.writerow([parsename(x), parsebio(x)])
#        except:
#            try:
#                x = x + 1
#                with open('output.csv', 'a') as output:
#                    csv_writer = csv.writer(output, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#                    csv_writer.writerow([parsename(x), parsebio(x)])
#            except:
#                print('Error, for x='+str(x)+'at page '+str(page))
