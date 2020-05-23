# _*_ coding : utf-8 _*-
# 作者:鱼
# @Time: 2020\5\14 0014 15:42
#@Email:1710770490@qq.com
#@File:oxlogin.py
from time import sleep

from besapage.besaobject import besa_Object
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class login(besa_Object):
    el = (By.XPATH,'/html/body/div[2]/div/ul[1]/div/div/a[1]')
    el1 = (By.XPATH,'/html/body/div[4]/div/div[2]/div[2]/form/div[1]/input')
    el2 = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[2]/input')
    el3 = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
    el4 = (By.XPATH, '//*[@id="js_climit_li"]/li[1]/div[1]/h3/a')
    el5 = (By.XPATH, '//*[@id="js_climit_li"]/li[1]/div[2]/div/div/div/div/dl[1]/dd[1]/a')

    def __init__(self,moth,url):
        self.ox_browser(moth)
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def login_info(self):
        self.ox_clik(self.el)
        self.ox_sendkey(self.el1,'yu23')
        self.ox_sendkey(self.el2,'12345678')
        self.ox_clik(self.el3)
        self.ox_attach()
        sleep(3)
        self.ox_ache(self.el4)
        self.ox_clik(self.el5)
        self.driver.quit()


if __name__ == '__main__':
    b = login('cc','http://39.98.138.157/shopxo/index.php')
    b.login_info()