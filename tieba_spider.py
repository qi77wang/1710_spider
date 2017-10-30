#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: tieba_spider.py
# Author: wangqi
# mail: qi77wang@163.com
# Created Time: 2017年10月27日 星期五 14时40分01秒

import urllib2

def load_page(url):
    '''
    @brief 通过url请求爬取到html静态页面源码
    @param url 要爬取的url地址
    @return html静态页面源码
    '''
    #方法下紧接'''的习惯需要养成
    user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
    headers = {'User-Agent':user_agent}

    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    html = response.read()

    return html

def write_file(file_name, text):
    '''
    @brief 将字符串内容写到文件中
    @param file_name 文件路径
    @param text  要写进的字符串
    '''
    print('正在存储文件' + file_name)
    f = open(file_name, 'w+')
    f.write(text)
    f.close()

def tieba_spider(start_page, end_page, url):
    '''
    @brief 爬虫主程序
    @param start_page 爬虫贴吧的起始页数
    @param end_page 爬虫贴吧的结束页数
    @param url 要爬取的url地址
    '''    
    for i in range(start_page, end_page+1):
        #根据百度贴吧的url中的页码pn规律
        # 当你打开第一页 pn = 0
        # 当你打开第二页 pn = 50
        # 当你打开第三页 pn = 100
        # 当你打开第四页 pn = 150 -0
        # ....
        # 所以 pn = 50* (page-1)
        pn = 50*(i -1)
        print('正在下载第' + str(i) + '个网页')
        html = load_page(url+str(pn))
        file_name = str(i)+".html"
        write_file(file_name, html)

if __name__ == '__main__':
    # url = raw_input('请输入贴吧的地址，去掉 pn= 后面的数字')
    url = "http://tieba.baidu.com/f?kw=lol&ie=utf-8&pn="
    begain = int(raw_input('请输入开始的页数'))
    last = int(raw_input('请输入结束的页数'))

    tieba_spider(begain, last, url)
