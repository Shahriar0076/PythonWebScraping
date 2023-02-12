#elements
driver.find_element #for first element
driver.find_elements #for multiple element


# by xpath ###################
myDiv = "/html/body/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/p[3]/span"
driver.find_element(By.XPATH, myDiv).get_attribute('innerText')

# in function 
def getData(xpath):
    try:
        return driver.find_element(By.XPATH, xpath).get_attribute('innerText')
    except:
        return "N/A"


# by class ###################
driver.find_element(By.CLASS_NAME, "card-body")

# by tag ###################
driver.find_element(By.TAG_NAME, 'h1')

# by chaining ###################
driver.find_element(By.CLASS_NAME, "card-body").find_element(By.TAG_NAME, 'h4').get_attribute('innerText') 

# by attributes ###################
.get_attribute('innerText')
.get_attribute('href')