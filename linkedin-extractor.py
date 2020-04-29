import csv
import time
from selenium import webdriver

user = ''
pwd = ''
group = ''

driver = webdriver.Chrome()
driver.get('https://linkedin.com')

sign_in_button = driver.find_element_by_class_name('nav__button-secondary')
sign_in_button.click()


############# connection & ouverture de la page #############
print('Logging in...')
id_box = driver.find_element_by_id('username')
id_box.send_keys('user')
pass_box = driver.find_element_by_id('password')
pass_box.send_keys('pwd')
sign_in_button_2 = driver.find_element_by_class_name('btn__primary--large')
sign_in_button_2.click()
time.sleep(2)

if "number" in driver.current_url:
    skip_button = driver.find_element_by_class_name('secondary-action')
    skip_button.click()
    time.sleep(2)

page = 1

print('Finding group...')
driver.get('https://www.linkedin.com/groups/'+group'/manage/membership/members/?page='+str(page))
time.sleep(5)
dismiss_button = driver.find_element_by_class_name("artdeco-dismiss")
dismiss_button.click()
driver.get('https://www.linkedin.com/groups/'+group'/manage/membership/members/?page='+str(page))
time.sleep(5)

############# définition des fonctions #############
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


############## par lettre de l'alphabet ################
search = driver.find_element_by_xpath("/html[@class='artdeco osx']/body[@class='render-mode-BIGPIPE nav-v2 ember-application boot-complete icons-loaded']/div[@id='ember6']/div[@class='application-outlet ']/div[@class='authentication-outlet']/div[@id='groups']/div[@class='groups-manage']/div[@class='groups-manage__grid']/main[@class='groups-manage__core-rail container ph0 pb0 Elevation-2dp']/div[@id='ember62']/artdeco-typeahead[@id='ember63']/section[@class='groups-manage-group-list__tab-header ph4 display-flex align-items-flex-end']/div[@class='groups-manage-group-list__search relative']/div[@id='groups-manage-group-list__search-input']/div/input")
search.send_keys('a')
last_page = int(driver.find_element_by_xpath("/html[@class='artdeco osx']/body[@class='render-mode-BIGPIPE nav-v2 ember-application boot-complete icons-loaded']/div[@id='ember6']/div[@class='application-outlet ']/div[@class='authentication-outlet']/div[@id='groups']/div[@class='groups-manage']/div[@class='groups-manage__grid']/main[@class='groups-manage__core-rail container ph0 pb0 Elevation-2dp']/div[@id='ember62']/artdeco-typeahead[@id='ember63']/section[2]/artdeco-pagination[@class='artdeco-pagination pv5']/ul[@class='artdeco-pagination__pages artdeco-pagination__pages--number']/li[@class='artdeco-pagination__indicator artdeco-pagination__indicator--number '][8]/button/span").text)
next_page = driver.find_element_by_xpath("/html[@class='artdeco osx']/body[@class='render-mode-BIGPIPE nav-v2 ember-application boot-complete icons-loaded']/div[@id='ember6']/div[@class='application-outlet ']/div[@class='authentication-outlet']/div[@id='groups']/div[@class='groups-manage']/div[@class='groups-manage__grid']/main[@class='groups-manage__core-rail container ph0 pb0 Elevation-2dp']/div[@id='ember62']/artdeco-typeahead[@id='ember63']/section[2]/artdeco-pagination[@class='artdeco-pagination pv5']/button[@id='ember1441']")
next_page.click()





############# par pages ###############

############# page 1 #############
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

############# pages 2-155 #############
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
