from urllib.request import urlopen
import re
from lxml import etree

html = urlopen("https://www.12371.cn/special/dsxxjc/xxwd/pz/?ivk_sa=1025883j")
text = bytes.decode(html.read())
list0 = re.findall("https.*shtml", text)

i = 1

for url in list0:
    html = urlopen(url)
    text = bytes.decode(html.read())

    html = etree.HTML(text)
    tt = html.xpath('//div[@class="word"]/p/text()')
    xx = html.xpath('//div[@class="word"]/p/span/text()')
    t = len(tt)
    x = len(xx)

    j = 0
    while j < t:
        if tt[j]:
            file = open(r'D:\xx.docx', 'a+', encoding='utf-8')
            file.write(tt[j])
            file.write("\n")
            file.close()
        j = j + 1

    file = open(r'D:\xx.docx', 'a+', encoding='utf-8')
    file.write("要点传真\n")
    file.close()

    k = 0
    while k < x:
        if xx[k]:
            file = open(r'D:\xx.docx', 'a+', encoding='utf-8')
            file.write(xx[k])
            file.write("\n")
            file.close()
        k = k + 1

    if i % 3 == 0:
        file = open(r'D:\xx.docx', 'a+', encoding='utf-8')
        file.write("\f")
        file.close()
    else:
        file = open(r'D:\xx.docx', 'a+', encoding='utf-8')
        file.write("\n\n")
        file.close()

    print(i)
    i = i + 1

