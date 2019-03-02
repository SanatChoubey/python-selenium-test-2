from selenium import webdriver
from bs4 import BeautifulSoup as bs
from time import sleep
   



def code1():
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    sleep(3)
    select= driver.find_element_by_name('username')
    select.send_keys('thequotesline')
    select2= driver.find_element_by_name('password')
    select2.send_keys('sanatc123')
    select.submit()
    sleep(3)


    for i in range(1,400):

        try:

            driver.get('https://www.instagram.com/p/BuLtsAEAaXF/')
            sleep(3)
            select3= driver.find_element_by_xpath('//a[@class="zV_Nj"]')
            select3.click()
            sleep(4)
    
            select4=driver.find_element_by_xpath('//div[@class="                  Igw0E     IwRSH      eGOV_        vwCYk                                                                            i0EQd                                   "]/div/div/div[@class="                  Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB          HVWg4                  _0mzm- ZUqME"][1]/div[3]/button')
            select4.click()
            sleep(3)
            select5=driver.find_element_by_xpath('//div[@class="                  Igw0E     IwRSH      eGOV_        vwCYk                                                                            i0EQd                                   "]/div/div/div[@class="                  Igw0E   rBNOH        eGOV_     ybXk5    _4EzTm                                                                                   XfCBB          HVWg4                  _0mzm- ZUqME"][4]/div[3]/button')
            select5.click()
          
            print(i)
            sleep(10)
        except:
            print('err occurred')
            sleep(5)

   




code1()



