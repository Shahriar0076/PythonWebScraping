import helpers as hp

driver = hp.loadDriver()
# hp.openPage(driver,'https://softexpo.com.bd/exhibitor/lists/2/mini-pavilion')

# item = hp.getElement(driver,'navbar-nav','class',False)
# items = hp.getElement(item,'a','tag',True)

# for item in items:
#     print(item.get_attribute('href') )

# item.click() #for clicking

def work():
    cards = hp.getElement(driver,'sponsor-content','class',True)
    for card in cards:
        h3 = hp.getElement(card,'h3','tag',False)
        link = hp.getElement(h3,'a','tag',False)
        print(link.get_attribute('href'))

    
hp.openPage(driver,'websiteURL')
work()
hp.openPage(driver,'websiteURL')
work()


###############

cards = driver.find_element(By.ID, 'dynamic_filter').find_elements(By.CLASS_NAME, 'sponsor-content')
for card in cards:
    card.find_element(By.TAG_NAME, 'h3').find_element(By.TAG_NAME, 'a').get_attribute('href')
        





for card in cards:
    driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/nav/ul/li[9]/a').click()

while(True):
    links = driver.find_elements(By.CLASS_NAME, 'col-xl-3').find_elements(By.CLASS_NAME, 'btn-info')
    for link in links:
        link.get_attribute('href')        
    driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/div/div[2]/div/ul/li[5]/a').click()

while(True):
    cards = driver.find_elements(By.CLASS_NAME, 'col-xl-3')
    for card in cards:        
        card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/div/div[2]/div/ul/li[5]/a').click()

driver = webdriver.Firefox();

links = [
'https://ispab.org/members?page=1',
'https://ispab.org/members?page=2',
'https://ispab.org/members?page=3',
'https://ispab.org/members?page=4',
'https://ispab.org/members?page=5',
'https://ispab.org/members?page=6',
'https://ispab.org/members?page=7',
'https://ispab.org/members?page=8',
'https://ispab.org/members?page=9',
'https://ispab.org/members?page=10',
'https://ispab.org/members?page=11',
'https://ispab.org/members?page=12',
'https://ispab.org/members?page=13',
'https://ispab.org/members?page=14',
'https://ispab.org/members?page=15',
'https://ispab.org/members?page=16',
'https://ispab.org/members?page=17',
'https://ispab.org/members?page=18',
'https://ispab.org/members?page=19',
'https://ispab.org/members?page=20',
'https://ispab.org/members?page=21',
'https://ispab.org/members?page=22',
'https://ispab.org/members?page=23',
'https://ispab.org/members?page=24',
'https://ispab.org/members?page=25',
'https://ispab.org/members?page=26',
'https://ispab.org/members?page=27',
'https://ispab.org/members?page=28',
'https://ispab.org/members?page=29',
'https://ispab.org/members?page=30',
'https://ispab.org/members?page=31',
'https://ispab.org/members?page=32',
'https://ispab.org/members?page=33',
'https://ispab.org/members?page=34',
'https://ispab.org/members?page=35',
'https://ispab.org/members?page=36',
'https://ispab.org/members?page=37',
'https://ispab.org/members?page=38',
'https://ispab.org/members?page=39',
'https://ispab.org/members?page=40',
'https://ispab.org/members?page=41',
]

for link in links:
    driver.get(link)
    cards = driver.find_elements(By.CLASS_NAME, 'job-box')
    for card in cards:        
        card.find_element(By.CLASS_NAME, 'title').get_attribute('href')



while(True):
    elements = driver.find_element(By.ID, 'example').find_elements(By.TAG_NAME, 'td')

    for element in elements:
        element.text

    driver.execute_script("$('#example_next').click()")


cards = driver.find_element(By.CLASS_NAME, 'committe').find_elements(By.CLASS_NAME, 'col-md-6')
for card in cards:        
    card.text


driver = webdriver.Firefox();
driver.get('https://e-cab.net/member-list')


while True:
    cards = driver.find_element(By.ID, 'example-content').find_elements(By.CLASS_NAME, 'card-footer')
    for card in cards:
        card.find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.execute_script('var pagination=document.querySelector(".pagination"),activePageItem=pagination.querySelector("li.page-item.active"),nextPageItem=activePageItem.nextElementSibling;nextPageItem.querySelector("a.page-link").click();')
    time.sleep(2)


cards = driver.find_element(By.ID, 'example-content').find_elements(By.CLASS_NAME, 'card-footer')
for card in cards:
    card.find_element(By.TAG_NAME, 'a').get_attribute('href')



    driver.find_element(By.TAG_NAME, 'body').text