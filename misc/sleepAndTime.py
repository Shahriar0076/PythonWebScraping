import time

time.sleep(10)

timeout = time.time() + 60*0.5   # 30 secs

while infoNotSaved:
    if time.time() > timeout:
        break

    if condition:        
        infoNotSaved = False #loop stops
    else:
        infoNotSaved = True 