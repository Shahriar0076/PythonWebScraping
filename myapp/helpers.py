from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import csv 
import time;
import requests


#selenium browser control
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

def readtext(filename,array=False):
    if array==True:
        with open(filename, "r") as file:
            return file
    else:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

def writetext(text,filename):
    with open(filename, "a") as file:
        file.write(text + "\n")

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

def click(driver):
    driver.click()

def writeText(driver,text):
    driver.send_keys(text)

#mouse and keyboard automation
def getAttribute(driver,name):
    return driver.get_attribute(name)

def mousePosition():
    return pyautogui.position()

def mouseMove(x,y):
    pyautogui.moveTo(x,y)

def mouseClick(x,y):
    pyautogui.click(x,y)

def mouseDoubleClick(x,y):
    pyautogui.doubleClick(x,y)

def keyboardPress(buttonName):
    pyautogui.press(buttonName)

def keyboardKeyDown(buttonName):
    pyautogui.keyDown(buttonName)

def keyboardKeyDown(buttonName):
    pyautogui.keyUp(buttonName)

def keyboardPressHotkey(buttonOneName,buttonTwoName):
    pyautogui.hotkey(buttonOneName,buttonTwoName)

def keyboardWrite(text):
    pyautogui.write(text)

def sleep(seconds):
    time.sleep(seconds)

def getTimeInSeconds():
    return time.time();

#api request
def getRequest(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()        
    else:
        print("Request failed with status code", response.status_code)
        return False

def postRequest(url,data):
    # data = {"name": "John", "email": "john@example.com"}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print("Request failed with status code", response.status_code)
        return False;