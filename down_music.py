#！/usr/bin/env python
#-*- coding:utf-8 -*-
#author: Zisc
import re
import os
import urllib
import requests
import time
from lxml import etree

"""
# 面向过程
music_page = "http://www.htqyy.com/top/musicList/new?pageIndex=0&pageSize=20"
get_music = requests.get(music_page).text
data = re.findall('value="([0-9]+)"',get_music)
print(data)

# music_html = etree.HTML(get_music)
# music_list = music_html.xpath('//input/@value')

for i in music_list:
    try:
        music_link = "http://f1.htqyy.com/play7/{}/mp3/4".format(str(i))
        urllib.request.urlretrieve(music_link,r'F:\\music\\'+str(i)+'.mp3')
        print("正在下载%s歌"%str(i))
    except:
        print("出错了")
"""
"""
采用面向对象(感觉复杂了hehe)
需求分析:
    1、获得每一页的url，返回 http://www.htqyy.com/top/musicList/new?pageIndex=0&pageSize=20
    2、从每一页中，取得每一页对应歌曲的编号 music_link = "http://f1.htqyy.com/play7/{}/mp3/4".format(str(i))
    3、下载函数，urllib.request.urlretrieve(url,'路径')
"""
class MusicSpider:
    def __init__(self):

        self.filePath =('F:\\music\\')#这是我保存音乐的路径名
    def creat_File(self):
        filePath = self.filePath
        if not os.path.exists(filePath):  # 判断路径是否存在，没有则创建
            os.makedirs(filePath)

    def get_pageNum(self): #获得总共页数，每页有20首，这里十分粗糙，加载页数的按钮是JS加载（不会爬），不晓得怎么获取最终页数，待改进。
        url = "http://www.htqyy.com/top/{}".format(Keywork)
        if url =="http://www.htqyy.com/top/hot":
            Page_num = 25
        elif url =="http://www.htqyy.com/top/new":
            Page_num = 5
        elif url =="http://www.htqyy.com/top/recommend":
            Page_num = 8
        return Page_num

    def getLinks(self,num):
        music_list = []
        for i in range(num):
            url = "http://www.htqyy.com/top/musicList/{}?pageIndex={}&pageSize=20".format(Keywork,str(i))
            music_list.append(url)
        return music_list

    def getMusicNum(self,mlist): #这里用正则匹配每首歌正确的编号
        music_num=[]
        for i in mlist:
            html = requests.get(i).text
            data = re.findall('value="([0-9]+)"', html)
            music_num.extend(data) #保存所有歌曲的正确编号
        return music_num

    def downLoad(self,rlist): # 从每首歌正确的编号拼接构成真实链接并下载保存

        for i in rlist:
            try:
                music_link = "http://f1.htqyy.com/play7/{}/mp3/4".format(str(i))
                urllib.request.urlretrieve(music_link, self.filePath + str(i) + '.mp3')
                print("正在下载编号为%s的歌" % str(i))
                time.sleep(2)
            except:
                print("出错了")

    def main_fuction(self):
        self.creat_File() #创建目录
        count = self.get_pageNum() #获得页数
        print("We have found:{} page!".format(str(count))) #障眼法，告诉有多少页，其实没什么卵用，页数都是我自己观察网页然后直接知道的
        num = self.getLinks(count)#知道多少页，然后就知道翻页范围
        MusicNum = self.getMusicNum(num)
        get_Load = self.downLoad(MusicNum)

if __name__ == '__main__':
    Keywork = input("请选择下载的类型:") #提供hot new recommend
    spider = MusicSpider()
    spider.main_fuction()

