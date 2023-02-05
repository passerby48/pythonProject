import random
import string


def codeGenerator(length):
    x = string.digits + string.ascii_letters
    y = length
    for i in range(y):
        j = random.randint(0, 15)
        print(x[j], end="")


def calScore(*p):
    if len(p) < 3:
        print("小于3个，无法计算")
    else:
        ave = (sum(p) - max(p) - min(p)) / (len(p) - 2)
        print(ave)


def intChange():
    num1 = int(input(":"))

    def aa(nn):
        if nn:
            nn = nn / 10


def encode(n):
    nList = (str(n))
    sList = [str((int(e) + 5) % 9) for e in nList]
    sList[0], sList[-1] = sList[-1], sList[0]
    print("".join(sList))


# codeGenerator(5)
# calScore(12, 24, 33, 4)
# intChange()
# encode(123456789)


class b:
    def __init__(self, ss):
        self.name = ss

    def kick(self):
        print("打" + self.name)


b1 = b("lq")
b1.kick()


