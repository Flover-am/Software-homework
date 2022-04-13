import operator
import re
if __name__ == '__main__':
    a = '122222111222 11'
    f = re.finditer('1',a)
    for i in f :
        print(i)


def search_n(s, c, n):
    """寻找第n个字符'a'"""
    r = s.find(c)
    while n > 1 and r >= 0:
        r = s.find(c, r + 1)
        n -= 1
    return r

# 做个实验
print(search_n("fdasadfadf", "a", 3))
# 结果为7，正确
