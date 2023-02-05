from urllib.request import urlopen
import re
from lxml import etree
import time
import os

html = urlopen("https://www.12371.cn/special/dsxxjc/xxwd/pz/?ivk_sa=1025883j")
text = bytes.decode(html.read())
list0 = re.findall("https.*shtml", text)

i = 1

for url in list0:
    # text = bytes.decode(html.read())
    # xpath = r"/html/body/div[2]/div/div[1]/div[5]/div[2]/div/div[3]/div/div/p[3]/strong"

    # html = etree.parse(url)
    # result = etree.tostring(html, pretty_print=True)  # pretty_print=True 会格式化输出
    # print(result)

    html = urlopen(url)
    text = bytes.decode(html.read())
    # print(text)

    # tree = etree.HTML(text)
    # get_list = tree.xpath('/html/body/div[2]/div/div[1]/div[5]/div[2]/div/div[3]/div/div/p[3]/strong')
    # print(get_list)
    # list1 = re.findall(r'<strong>.*</strong>', text)
    # print(list1)
    # file = open(r'D:\tt.txt', 'a')
    # file.write(list1[0])
    # file.close()

    # file = open(r'D:\ttxxtt\tt' + str(i) + '.txt', 'a+',encoding='utf-8')
    # file.write(text)
    # file.close()

    html = etree.HTML(text)
    j = 3
    while j<20:
        xx = html.xpath("/html/body/div[2]/div/div[1]/div[5]/div[2]/div/div[3]/div/div/p[" + str(j) + "]/text()")
        # print(html.xpath("/html/body/div[2]/div/div[1]/div[5]/div[2]/div/div[3]/div/div/p[" + str(j) + "]/text()"))
        file = open(r'D:\ttxxtt\xx' + str(i) + '.txt', 'a+', encoding='utf-8')
        file.write(xx[0])
        file.close()
        j = j + 1



    i = i + 1

    time.sleep(0.5)
