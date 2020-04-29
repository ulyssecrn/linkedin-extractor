import csv
import time
from selenium import webdriver
from credentials import *

# functions
def parsename(x):
    name = driver.find_element_by_xpath(
        "/html[@class='artdeco osx']/body[@class='render-mode-BIGPIPE nav-v2 ember-application boot-complete icons-loaded']/div[@id='ember6']/div[@class='application-outlet ']/div[@class='authentication-outlet']/div[@id='groups']/div[@class='groups-manage']/div[@class='groups-manage__grid']/main[@class='groups-manage__core-rail container ph0 pb0 Elevation-2dp']/div[@id='ember62']/artdeco-typeahead[@id='ember63']/artdeco-typeahead-results-list[@id='ember63-a11y']/artdeco-typeahead-result[@id='ember" + str(
        x) + "']/div[@id='ember" + str(x + 1) + "']/artdeco-entity-lockup[@id='ember" + str(
        x + 2) + "']/artdeco-entity-lockup-content[@id='ember" + str(x + 8) + "']/a[@id='ember" + str(x + 9) + "']/artdeco-entity-lockup-title[@id='ember" + str(x + 10) + "']/span").text
    return name

def parsebio(x):
    bio = driver.find_element_by_xpath("/html[@class='artdeco osx']/body[@class='render-mode-BIGPIPE nav-v2 ember-application boot-complete icons-loaded']/div[@id='ember6']/div[@class='application-outlet ']/div[@class='authentication-outlet']/div[@id='groups']/div[@class='groups-manage']/div[@class='groups-manage__grid']/main[@class='groups-manage__core-rail container ph0 pb0 Elevation-2dp']/div[@id='ember62']/artdeco-typeahead[@id='ember63']/artdeco-typeahead-results-list[@id='ember63-a11y']/artdeco-typeahead-result[@id='ember" + str(
        x) + "']/div[@id='ember" + str(x + 1) + "']/artdeco-entity-lockup[@id='ember" + str(
        x + 2) + "']/artdeco-entity-lockup-content[@id='ember" + str(x + 8) + "']/artdeco-entity-lockup-subtitle[@id='ember" + str(x + 12) + "']").text
    return bio

# selenium webdriver, change it here if you use another browser
driver = webdriver.Safari()

# connection
print('Logging in...')
driver.get('https://linkedin.com')
sign_in_button = driver.find_element_by_class_name('nav__button-secondary')
sign_in_button.click()
id_box = driver.find_element_by_id('username')
id_box.send_keys('user')
pass_box = driver.find_element_by_id('password')
pass_box.send_keys('pwd')
sign_in_button_2 = driver.find_element_by_class_name('btn__primary--large')
sign_in_button_2.click()
time.sleep(2)

# accept warning
if "number" in driver.current_url:
    skip_button = driver.find_element_by_class_name('secondary-action')
    skip_button.click()
    time.sleep(2)

# load group
print('Finding group...')
page = 1
driver.get('https://www.linkedin.com/groups/'+group'/manage/membership/members/?page='+str(page))
time.sleep(5)
dismiss_button = driver.find_element_by_class_name("artdeco-dismiss")
dismiss_button.click()
driver.get('https://www.linkedin.com/groups/'+group'/manage/membership/members/?page='+str(page))
time.sleep(5)

# page 1
if first == 1:
    print('Parsing page 1...')
    x = 67
    with open('output.csv', 'a') as output:
        csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([parsename(x), parsebio(x)])

    x = 59
    for y in range(1, 50):
        x = x + 27
        try:
            vide = parsename(x)
        except:
            x = x + 1
        with open('output.csv', 'a') as output:
            csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([parsename(x), parsebio(x)])
    first = 2

# rest of the pages
a = 0
for page in range(first, last):
    print('Parsing page '+str(page)+'...')
    driver.get('https://www.linkedin.com/groups/4366029/manage/membership/members/?page='+str(page))
    time.sleep(5)
    x = 40
    for y in range(0, 50):
        x = x+27
        try:
            with open('output.csv', 'a') as output:
                csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow([parsename(x), parsebio(x)])
        except:
            try:
                x = x + 1
                with open('output.csv', 'a') as output:
                    csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow([parsename(x), parsebio(x)])
            except:
                print('Error, for x='+str(x)+'at page '+str(page))
