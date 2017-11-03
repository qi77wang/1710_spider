#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: duanzi_spider.py
# Author: wangqi
# mail: qi77wang@163.com
# Created Time: 2017年10月30日 星期一 16时01分55秒

import urllib2
import re
import time

class Spider(object):
    """
        内涵段子爬虫类
    """
    def __init__(self, page):
        self.page = page       #首次默认爬取的页面数
        self.flag = True    #决定是否继续爬取

    def load_page(self, page):
        '''
        @brief      定义一个url请求网页的方法
        @para page  需要请求第几页
        @returns    返回简单处理的数据
        '''
        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"
        
        user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
        headers = {"User-Agent":user_agent}

        req = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(req)
        html = response.read()
        #某些网站的中文是gbk格式，爬下来后显示乱码，此处将其转换为utf-8
        gbk_html = html.decode("gbk").encode("utf-8")

        #这里讲接收到的html进行简单的处理，其实放到下一个方法中应该也可以，但放在
        #这里应该有一定道理，如果现在这种，传的是list，反之传的是html
        #找到所有的段子内容<div class = "f18 mb20"></div>
        # .*? 匹配任意字符
        # 加上 re.S，表示正则表达式会将这个字符串作为一个整体，在整体中进行匹配。
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
        item_list = pattern.findall(gbk_html)
        return item_list

    def write_to_file(self, text):
        '''
        @brief      将文本写入到文件中
        @text       要写入的文本
        '''
        #此处可以加上容错，操作文件应该加
        f = open("./story.txt", "a")
        f.write("============================================================")
        f.write(text)
        f.close()

    def print_one_page(self, item_list, page):
        '''
        @brief              拿到简单处理的数据，进一步处理
        @para   item_list   简单处理后的数据list
        @para   page        爬取的页码
        '''
        print("第" + str(page) + "页爬取完毕")
        for item in item_list:
            item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "")
            item = item.replace("&ldquo;", "“").replace("&rdquo;", "”").replace("&hellip;", "...")
            # print(item)
            self.write_to_file(item)

    def do_work(self):
        '''
        @brief  爬虫主程序
        '''
        while self.flag:
            try:               #发现过一个bug，有时候好像网络不太顺畅时，程序会报错，这样应该可以
                item_list = self.load_page(self.page)
            except urllib2.URLError, e:
                print e.reason
                continue
            #对得到的段子 item_list 处理
            self.print_one_page(item_list, self.page)
            self.page += 1
            print("爬取下一页请按回车，退出请输入q")
            command = raw_input()
            if command == "q":
                self.flag = False

            time.sleep(0.01)

if __name__ == "__main__":
    print('''
    ==========================
          内涵段子小爬虫
    ==========================                
    ''')
    print("请输入爬取的起始页码")
    start_page = int(raw_input())

    mySpider = Spider(start_page)
    mySpider.do_work()






    
        
