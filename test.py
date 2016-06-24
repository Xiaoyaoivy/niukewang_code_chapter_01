# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def qiushibaike():  # 调用糗事百科主页输出内容
    content = requests.get('http://qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()


def demo_string():
    stra = 'hello worlD'
    print 1, stra.capitalize()  # 首字母大写，其余小写
    print 2, stra.replace('worlD', 'nowcoder')  # 替换

    strb = '   \n\rhello nowcoder \r\n  '
    print 3, strb.lstrip()  # 去掉前面空格回车
    print 4, strb.rstrip()  # 去掉后面回车空格

    strc = 'hello w'
    print 5, strc.startswith('hel')  # 判断是否以开头
    print 6, strc.endswith('x')  # 判断是否以结尾
    print 7, stra + strb + strc
    print 8, len(strc)  # 求字符串长度
    print 9, '-'.join(['a', 'b', 'c'])
    print 10, strc.split(' ')  # 分割


def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 2, True, not True
    print 3, 1 < 3, 5 > 2
    print 4, 2 << 3, 8 >> 1  # 移位
    print 5, 5 | 3, 5 & 3, 5 ^ 3  # 或，与，异或（位操作）
    x, y = 2, 3.3
    print x, y, type(x), type(y)


def demo_buildinfunction():
    print 1, max(2, 1), min(5, 3)
    print 2, len('xxx'), len([1, 2, 3])
    print 3, abs(-2)
    print 4, range(1, 10, 3)
    print 5, dir(list)  # 打印函数名
    x = 2
    print 6, eval('x+3')
    print 7, chr(65), ord('a')


def demo_controlflow():
    score = 65
    if score > 99:
        print 1, 'A'
    elif score > 60:
        print 2, 'B'
    else:
        print 3, 'C'

    while score < 100:
        print score
        score += 10
    score = 65
    # for(int i = 0;i < 10; i++)
    # continue, break , pass
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do_specipal
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break


def demo_list():
    lista = [1, 2, 3]  # vector
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb  # 操作符重载
    print 6, lista
    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)  # 弹出元素
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13, listb * 2
    # tumple是一种不可变更的list，只读
    tupleaa = (1, 2, 3)
    listaa = [1, 2, 3]
    listaa.append(4)
    print 14, listaa


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_dict():
    dicta = {4: 16, 1: 1, 2: 4, 3: 9}  # key:value
    print 1, dicta
    print 2, dicta.keys(), dicta.values()
    print 3, dicta.has_key(1), dicta.has_key('3')
    for key, value in dicta.items():
        print 'key-value', key, value
    dictb = {'+': add, '-': sub}
    print 4, dictb['+'](1, 2)  # 下标
    print 5, dictb.get('-')(15, 3)  # 方法，get
    dictb['*'] = 'x'
    print 6, dictb
    dicta.pop(4)
    print 7, dicta
    del dicta[1]
    print 8, dicta


def demo_set():  # set不可以做加法
    seta = set((1, 2, 3))
    # 两种定义方法
    a = [1, 2, 3]
    seta = set(a)
    setb = set((2, 3, 4))
    print 1, seta
    # seta.add(4)
    # print 2, seta
    print 3, seta.intersection(setb), seta & setb  # 并
    print 4, seta | setb, seta.union(setb)  # 交
    print 5, seta - setb
    seta.add('x')
    print 6, seta
    print 7, len(seta)
    print 8, seta.add(4)


class User:
    type = 'USER'

    def __init__(self, name, uid):  # 成员函数初始化函数，用self开头
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Guest(User):
    type = 'GUEST'

    def __repr__(self):
        return 'im guest ' + self.name + ' ' + str(self.uid)


class Admin(User):  # 管理员，从user继承
    type = 'ADMIN'

    def __init__(self, name, uid, group):  # 属于某个组
        User.__init__(self, name, uid)  # 调用基类
        self.group = group

    def __repr__(self):
        return 'im guset' + self.name + ' ' + str(self.uid) + ' ' + self.group


def create_user(type):  # 创建组
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 1, 'g1')
    else:
        return Guest('gu1', 201)
        # raise ValueError('error')


# 异常处理
def demo_exception():
    try:
        print 2 / 1
        print 2 / 0
        raise Exception('Raise Error', 'NowCoder')
    except Exception as e:
        print 'error:', e
    finally:#不管代码前面是否有问题，都打印
        print 'clean up'


if __name__ == '__main__':
    # user1 = User('u1', 1)
    # print user1
    # admin1 = Admin('a1', 101, 'g1')
    # print admin1
    #
    # print create_user('Guest')  # 多态
# qiushibaike()
# demo_string()
# demo_operation()
# demo_buildinfunction()  # 内置函数
# demo_controlflow()  # 控制流
# 四组结构：list,dictory,tumple,
# demo_list()
# demo_dict()
# demo_set()  # 集合
# 面向对象，重载=多态
    demo_exception()