# ！/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
"""
功能:获取本机IP地址, 查询IP地址
原理:爬取国内的查询网站，观察请求参数，简单的抓包分析，然后写匹配规则把对应内容匹配出来
缺点:如果网页改版，则代码报废
"""

class GetLocalIpAddress(object):
    def __init__(self):
        self.headers = {"User-Agent": UserAgent().random}
        self.sourse_html = 'http://www.ip138.com/ips138.asp?'

    def get_local_ip(self):
        response = requests.get(self.sourse_html, headers=self.headers)
        response.encoding = None  # 编码问题
        bsObj = BeautifulSoup(response.text, 'lxml')
        ip_address = bsObj.find_all('table', {'align': 'center'})[1].find_all('td', {'align': 'center'})
        local_ip = ip_address[1].get_text()
        return local_ip


class GetIpAddress(object):
    def __init__(self):
        self.headers = {"User-Agent": UserAgent().random}
        # http://www.ip138.com/ips1388.asp?ip=121.97.110.145&action=2
        self.sourse_html = 'http://www.ip138.com/ips138.asp?ip={}&action=2'

    def demand_ip(self, ip):
        self.sourse_html = self.sourse_html.format(ip)
        response = requests.get(self.sourse_html ,headers=self.headers)
        response.encoding = None
        # print(response.text)
        bs0bj = BeautifulSoup(response.text, 'lxml')
        ip_address_tag = bs0bj.find("ul", {'class': 'ul1'}).find_all('li')[0]
        ip_address = ip_address_tag.get_text().strip()
        return ip_address


if __name__ == '__main__':
    test = GetIpAddress()
    test1 = GetLocalIpAddress()
    print(test1.get_local_ip())
    print(test.demand_ip('121.97.110.145'))