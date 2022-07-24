import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Web_table:
    def finding_web_elements(self):
        serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get("file:///C:/Users/veeresh/Documents/WebTable.html")
        driver.implicitly_wait(10)
        total_rows = str(len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr")))
        total_coloms =str(len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th")))
        cells = str(len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr/th")))

        print("Number of rows :- " + total_rows)
        print("Number of coloms :- " + total_coloms)
        print("Total number of cells :- " +cells)
        time.sleep(3)
        #only_numeric_value = driver.find_elements(By.XPATH,"")


        driver.close()

#        for r in range(2,+row):
#            for c in range(1, +coloms):
#                value = driver.find_elements(By.XPATH,"/html/body/table/tbody/tr["+str(r)+"]/th["+str(c)+"]").text
#            print(value)
#        print()

table = Web_table()
table.finding_web_elements()