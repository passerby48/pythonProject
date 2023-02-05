import re


def t1():
    # A.文件？
    # B.break跳出所有循环
    # C.continue跳出本次循环
    # D.错
    return "B"


def t2():
    # for i in range(10, 0, -1):
    #     print(i, end=" ")
    return "C"


def t3():
    # buhui
    return "buhui"


def t4():
    # 不会
    return "buhui"


def t5():
    # buhui
    return "buhui"


def t6():
    # print(eval("600+10"))
    return "C"


def t7():
    # print(eval("7%2"))
    return "B"


def t8():
    # d={1: "a", 2: "c", 3: "d", 4: "e"}
    # print(len(d.values()))
    return "C"


def t9():
    # d={"a",2,3,1,4, "a"}
    # print(len(d))
    return "D*"


def t10():
    # B?
    return "B?"


def t11():
    # ls = ["20.20", "Python"]
    # ls.extend([2020, "2020"])
    # print(ls)
    return "D*"


def t12():
    # ls = ["20.20", "Python"]
    # ls.append([2020, "2020"])
    # print(ls)
    return "B*"


def t13():
    # ls = [1, "abc", "PYTHON"]
    # print(ls[2][-1])
    return "A"


def t14():
    # ls = [1, "a",2, ["b", "abc"]]
    # print(ls[3][-1][0])
    return "A"


def t15():
    # parame = {value01,value02,...}
    return "A"


def t16():
    # d = {key1 : value1, key2 : value2, key3 : value3 }
    return "D"


def t17():
    # 变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数字打头
    return "BCD"


def t18():
    # def func(**q):
    #     for e in q:
    #         print(e + "1")
    # func(a=1)
    # func(1, 2)
    # func(a=1, b=2)
    # func(a="1", b="2")
    return "ACD"


def t19():
    # txt = ["ab666", "1234", "12.35", "Aa112"]
    # text=re.match("[a-b0-9]{4,5}",txt)
    # print(text)
    # 题错了？
    return "AB"


def t20():
    # 基本的数据类型：数字型、字符串、元组、列表、字典、集合
    # 不可变数据类型：数字型、字符串、元组
    # 可变数据类型：列表、字典、集合
    return "ACD*"


def t21():
    # print(27/3**2)
    return "3.0*"


def t22():
    # t=("a", "@", "b", "@", "c")
    # print("".join(t))
    return "a@b@c"


def t23():
    # DictColor = {"seashell": "海贝色", "gold": "金色", "pink": "粉红色", "brown": "棕色", "purple": "紫色",
    #              "tomato": "西红柿色"}
    # print(DictColor.get("brown", 0))
    return "棕色*"


def t24():
    # d = {"li": "m", "alice": "f", "jerry": "f"}
    # for k in d:
    #     print(k, end=" ")
    return "li alice jerry*"


def t25():
    # ss="I love NAU."
    # print(ss[7:-1])
    return "NAU*"


def t26():
    # L = [1, 2, 3, 4, 5, 2, 1, 3, 6, 4, 4, 4]
    # print(set(L))
    return "print(set(L))*"


def t27():
    # t = (84, 76, 63, 55, 98, 100, 53)
    # sum = 0
    # for num in t:
    #     sum = sum + num
    # ave = sum / len(t)
    # print(round(ave,1))
    return """
    sum = 0
    for num in t:
        sum = sum + num
    ave = sum / len(t)
    print(round(ave,1))
    *"""


def t28():
    #
    return " "


def t29():
    # dd = {"Barry": 39, "Jerry": 63, "Anna": 20, "Bob": 22, "Amy": 50, "Dora": 53, "Jessica": 31}
    # i = 0
    # for age in dd.values():
    #     if age < 30:
    #         print(list(dd.keys())[i], ":青年")
    #     elif age < 40:
    #         print(list(dd.keys())[i], ":中青年")
    #     elif age < 50:
    #         print(list(dd.keys())[i], ":中年")
    #     else:
    #         print(list(dd.keys())[i], ":中老年")
    #     i = i + 1
    return """ 
    i = 0
    for age in dd.values():
        if age < 30:
            print(list(dd.keys())[i], ":青年")
        elif age < 40:
            print(list(dd.keys())[i], ":中青年")
        elif age < 50:
            print(list(dd.keys())[i], ":中年")
        else:
            print(list(dd.keys())[i], ":中老年")
        i = i + 1
    *"""


def t30():
    # txt = "张明：13512747745、马小小 15612347859、王玥 025-58311235、 赵照 01084567896、黄小罗 025-58314758"
    # num = re.findall("\d+-\d+|\d+", txt)
    # print(num)
    return '''
    txt = "张明：13512747745、马小小 15612347859、王玥 025-58311235、 赵照 01084567896、黄小罗 025-58314758"
    num = re.findall("\d+-\d+|\d+", txt)
    print(num)
    '''


# for i in range(31):
#     print("print(\"第"+str(i)+"题:\\t\",t" + str(i) + "(), \"\\n\")")

def answer():
    print("第1题:\t", t1(), "\n")
    print("第2题:\t", t2(), "\n")
    print("第3题:\t", t3(), "\n")
    print("第4题:\t", t4(), "\n")
    print("第5题:\t", t5(), "\n")
    print("第6题:\t", t6(), "\n")
    print("第7题:\t", t7(), "\n")
    print("第8题:\t", t8(), "\n")
    print("第9题:\t", t9(), "\n")
    print("第10题:\t", t10(), "\n")
    print("第11题:\t", t11(), "\n")
    print("第12题:\t", t12(), "\n")
    print("第13题:\t", t13(), "\n")
    print("第14题:\t", t14(), "\n")
    print("第15题:\t", t15(), "\n")
    print("第16题:\t", t16(), "\n")
    print("第17题:\t", t17(), "\n")
    print("第18题:\t", t18(), "\n")
    print("第19题:\t", t19(), "\n")
    print("第20题:\t", t20(), "\n")
    print("第21题:\t", t21(), "\n")
    print("第22题:\t", t22(), "\n")
    print("第23题:\t", t23(), "\n")
    print("第24题:\t", t24(), "\n")
    print("第25题:\t", t25(), "\n")
    print("第26题:\t", t26(), "\n")
    print("第27题:\t", t27(), "\n")
    print("第28题:\t", t28(), "\n")
    print("第29题:\t", t29(), "\n")
    print("第30题:\t", t30(), "\n")

answer()
