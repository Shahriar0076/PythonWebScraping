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

    
hp.openPage(driver,'https://softexpo.com.bd/exhibitor/lists/3/open-pavilion')
work()
hp.openPage(driver,'https://softexpo.com.bd/exhibitor/lists/2/mini-pavilion')
work()
hp.openPage(driver,'https://softexpo.com.bd/exhibitor/lists/2/mini-pavilion/30')
work()
hp.openPage(driver,'https://softexpo.com.bd/exhibitor/lists/2/mini-pavilion/60')
work()
hp.openPage(driver,'https://softexpo.com.bd/exhibitor/lists/1/stall')
work()
hp.openPage(driver,'https://softexpo.com.bd/exhibitor/lists/1/stall/30')
work()
hp.openPage(driver,'https://softexpo.com.bd/exhibitor/lists/1/stall/30')
work()
