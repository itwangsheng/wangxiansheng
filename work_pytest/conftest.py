# _*_ coding : utf-8 _*-
# 作者:鱼
# @Time: 2020\5\16 0016 11:02
#@Email:1710770490@qq.com
#@File:conftest.py
import os,pytest,yaml

print("这是conftest文件")
path = os.path.abspath(r'./config')
print(path)
@pytest.fixture()
def read_yaml():
    with open(path +r'\oxurl.yaml', 'r', encoding='utf-8') as file:
        red = yaml.load(file, Loader=yaml.FullLoader)
        return red