# _*_ coding : utf-8 _*-
# 作者:鱼
# @Time: 2020\5\14 0014 17:00
#@Email:1710770490@qq.com
#@File:test_pytest.py
import pytest,os,allure
import yaml

from sendinfo_page.oxlogin import login
# path = os.path.abspath(r'./config')
# @pytest.fixture()
# def read_yaml():
#     with open(path +r'\oxurl.yaml', 'r', encoding='utf-8') as file:
#         red = yaml.load(file, Loader=yaml.FullLoader)
#         return red
class Testcase():
    def setup(self):
        print("开始执行")
    def teardown(self):
        print("这是用例尾部")

    @pytest.mark.g1
    @pytest.mark.usefixtures('read_yaml')
    def test01(self,read_yaml):
        # print(*read_yaml)
        b = login(*read_yaml)
        try:
            b.login_info()
        except Exception as e:
            b.ox_attach()
            raise e
    @pytest.mark.g2
    def test02(self):
        print("用例二")
if __name__ == '__main__':
    pytest.main(['-s','test_pytest.py',' --alluredir','./report/xml'])