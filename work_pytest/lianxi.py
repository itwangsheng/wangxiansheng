# _*_ coding : utf-8 _*-
# 作者:鱼
# @Time: 2020\5\13 0013 16:04
#@Email:1710770490@qq.com
#@File:lianxi.py
import hashlib

str ='zzz'

h = hashlib.md5()

h.update(str.encode(encoding='utf-8'))

print("这是加密后的字符："+h.hexdigest())