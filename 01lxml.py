#coding:utf-8

from lxml import etree
import re
text = ''' <div> <ul>
        <li class="item-1"><a><!--first item--></a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a>
        </ul> </div> '''
text = re.sub(r"<!--|-->","",text)
html = etree.HTML(text)
# print(html.xpath('//li[@class="item-1"]/a/text()'))
# print(html)
#把element对象转化为字符串
# print(etree.tostring(html).decode())
#调用element的xpath方法,结果是一个列表
href_list = html.xpath('//li[@class="item-1"]/a/@href')
# print(href_list)
text_list = html.xpath('//li[@class="item-1"]/a/text()')
# print(text_list)

#假设li标签表示一条新闻，要把每条新闻组成一个字典
for href in href_list:
    temp = {}
    temp['href'] = href
    temp['title'] = text_list[href_list.index(href)]
    # print('title',text_list[href_list.index(href)])
    # print(temp)
print('*'*50)

#更好的数据组合方式
li_list = html.xpath('//li[@class="item-1"]')
# print(li_list)
for li in li_list:
    item = {}
    # print(li.xpath('./a/@href'))
    item['href'] = li.xpath('./a/@href')[0] if len(li.xpath('./a/@href'))> 0 else None
    item['title'] = li.xpath('./a/text()')[0] if len(li.xpath('./a/text()'))>0 else None
    print(item)
