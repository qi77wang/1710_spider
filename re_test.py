#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File Name: re_test.py
# Author: wangqi
# mail: qi77wang@163.com
# Created Time: 2017年10月30日 星期一 11时55分29秒

#引入正则表达式re模块
import re

#要匹配的源文件
src = "3.1415926, 364.1616, 1111, 0000, 0.55555"
#compile方法，提供输入匹配规则，生成规则实例
pattern = re.compile(r'\d+\.+\d*')      #规则最后不加*，只能显示小数点后一位数字
#findall 返回全部匹配到的字符串列表
result = pattern.findall(src)

for i in result:
    print(i)