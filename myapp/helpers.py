from selenium import webdriver
from selenium.webdriver.common.by import By
import threading
import csv 

def loadDriver():
    return webdriver.Firefox();

def openPage(driver,url):
    driver.get(url)

def runJs(driver,js):
    driver.execute_script(js)

def readCSV(filename):
    with open(filename, 'r') as file:
        return csv.reader(file)
        

def writeCSV(variableArray,filename):
    rows = [ variableArray ] 
    with open(filename, 'a') as csvfile:         
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerows(rows)

def getElement(driver,name,type,multiple):
    if type=='class':
        itemType = By.CLASS_NAME
    elif type=='id':
        itemType = By.ID
    elif type=='tag':
        itemType = By.TAG_NAME
    elif type=='xpath':
        itemType = By.XPATH

    if multiple == True:
        return driver.find_elements(itemType, name)
    else:
        return driver.find_element(itemType, name)



