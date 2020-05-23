# _*_ coding : utf-8 _*-
# 作者:鱼
# @Time: 2020\5\14 0014 15:07
#@Email:1710770490@qq.com
#@File:besaobject.py
import os,allure
import yaml
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
path = os.path.abspath(r'./config')
print(path)

class besa_Object():
    #寻找元素
    def locats(self,locators):
        locat = self.driver.find_element(*locators)
        return locat
    #点击
    def ox_clik(self,locators):
        self.locats(locators).click()
    #输入
    def ox_sendkey(self,locators,text):
        self.locats(locators).send_keys(text)
    #鼠标悬停
    def ox_ache(self,locators):
        ActionChains(self.driver).move_to_element(self.locats(locators)).perform()
    #显示等待
    def ox_wait(self):
        pass
    def write_yaml(self):
        with open(path+'/oxurl.yaml','w',encoding='utf-8') as file:
            yaml.dump(['cc', 'http://39.98.138.157/shopxo/index.php'],file)
    def read_yaml(self):
        with open(path+'/oxurl.yaml','r',encoding='utf-8') as file:
            red = yaml.load(file,Loader=yaml.FullLoader)
            return red
    #截图
    def ox_attach(self):
        file_name=path+r'/attach/1.png'
        self.driver.save_screenshot(file_name)#截图函数
        with open(file_name,'rb') as file:
            f= file.read()
        allure.attach(f,'denglu',allure.attachment_type.PNG) #把图片添加到alluer报告

    #选择浏览器
    def ox_browser(self,moth):
        if moth == 'cc':
            self.driver = webdriver.Chrome()
        if moth == 'ie':
            self.driver = webdriver.Ie()
# b= besa_Object()
# b.write_yaml()
# print(b.read_yaml())