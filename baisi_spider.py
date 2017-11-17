#coding:utf-8
import re
import requests
import json


class BaisiSpider(object):
    def __init__(self):
        self.temp_url ="http://www.budejie.com/text/{}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}
        self.url_list = [self.temp_url.format(i) for i in range(1,51)]

    def parse_url(self,url):
        res =requests.get(url,headers = self.headers)
        html_str = res.content.decode()
        return html_str

    def get_content_list(self,html_str):
        # content_list =re.findall(r'<div class="j-r-list-c-desc">.*?<a.*?>(.*?)</a>',html_str,re.S)
        # 提取段子的内容
        content_list = re.findall(r"<div class=\"j-r-list-c-desc\">.*?<a.*?>(.*?)</a>", html_str, re.S)
        #替换段子中的br为空
        content_list = [re.sub('<br />','',i) for i in content_list]
        return content_list

    def save_data(self,content_list):
        with open('bs_dz04.txt','a') as f:
            for content in content_list:
                content_str = json.dumps(content,ensure_ascii=False,indent=2)
                f.write(content_str)
                f.write('\n')
        print('保存成功')


    def run(self):
        #获取url
        html_str = ''
        content_list =''
        for url in self.url_list:
            #向url发送请求，获取向应
            print('正在解析:',url)
            html_str =self.parse_url(url)
            content_list = self.get_content_list(html_str)
            self.save_data(content_list)


if __name__ =="__main__":
    bs = BaisiSpider()
    bs.run()


