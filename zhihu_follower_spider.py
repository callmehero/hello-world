#！/usr/bin/env python
#-*- coding:utf-8 -*-
#author: Zisc
#爬取知乎Lyon的关注者
import requests
import pandas as pd
import time


headers={
    'cookie': 'q_c1=b37a1d7b90a84f438906faf7c6cf9097|1520228823000|1520228823000; _zap=3faf7745-7e96-4bd2-8643-6cf3438cb111; l_cap_id="ZDJlNTU1YWU5MTYwNGNiZDhmMWVmZjFmMmFhMzQ5NGI=|1520415858|460b2e1835d499394ddd6879b46478c02480bd53"; r_cap_id="OTNmNDM5NWQxOTExNDMxYWE0ZmQ5N2QxZTA1MzYxNjk=|1520415858|abe371eba47f2d86d182d0cff67eba6c56c57d1d"; cap_id="OTZlMDRkZTg4MTZkNDA5ZmEyNzc1N2JhMGM1MTI2YWE=|1520415858|d8d158618a87c7bdb41df1a20261f672d94eeae7"; capsion_ticket="2|1:0|10:1520650948|14:capsion_ticket|44:OGIwMjVkODNlNWIxNGNlMmIyNzJhYTlmN2Y0MDdhODc=|53a5760d33e6049d73492f43538bcb2ce7fed14d5fed878caca862e1ba5c09fc"; z_c0="2|1:0|10:1520650979|4:z_c0|80:MS4xV1QzWUJnQUFBQUFtQUFBQVlBSlZUZU9Za0Z1OS1xWmZnSTV6M1BkakhkTjVaU0p0WXlQNFNnPT0=|2a9849214141dee3dc5bc0aebc82b18151e7b298c024eae8f02b2b9ff86d96bd"; __DAYU_PP=NIfbiMnbmnrAjzyi2AMr2977be3849bd; __utmv=51854390.100-1|2=registration_date=20171211=1^3=entry_date=20171211=1; d_c0="ADCvSg9GVw2PTk9RBq7qFY59b6Wt4AMVAMg=|1521975136"; _xsrf=61bbfd92-fc67-409d-9ea0-16a467c91822; __utma=51854390.392313614.1521867386.1522073164.1522243628.12; __utmb=51854390.0.10.1522243628; __utmc=51854390; __utmz=51854390.1522243628.12.12.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/24306639',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
user_data = []
def get_user_data(page):
    for i in range(page):
        url = "https://www.zhihu.com/api/v4/members/better-man007/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20".format(i*20)
        respone = requests.get(url,headers=headers).json()['data']
        user_data.extend(respone)
        print("正在爬取第%s页"%str(i+1))
        time.sleep(3)
if __name__ == '__main__':
    get_user_data(13)
    file = pd.DataFrame.from_dict(user_data)
    file.to_csv("hehe.csv")
