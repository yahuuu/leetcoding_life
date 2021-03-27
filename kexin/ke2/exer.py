# 1
import decimal

print('%.20f' % 3.14) # 输出3.14000000000000012434
print(decimal.Decimal('3.14')) # 精确的始终只用两位小数表示

decimal.getcontext().rounding=decimal.ROUND_HALF_UP  #4舍5入  ROUND_HALF_DOWN 不入
c1=decimal.Decimal('2.135').quantize(decimal.Decimal('0.00'))
print(c1)

c2=decimal.Decimal('2.145').quantize(decimal.Decimal('0.00'))
print(c2)


# 2
def multipliers():
    return [lambda x: i * x for i in range(4)]

# 3
it = iter([0, 1, 2, 3, 4, 5])
def func():
    return next(it)
for j in iter(func, 4):
    print(j)

# 4
import re
m = re.match('(\w\w\w)-(\d?)', 'abc-123')
print(m.group())  # abc-1
print(m.groups())  # ('abc', '1')
print(m.group(0))  # abc-1
print(m.group(1))  # abc
print(m.group(2))  # 1

# 5
print(3 and 55)
print(33 or 5)

# 6
a = 1,2
print(a)

# 7
# 保留两位小数，看第三位数，d<5舍弃，d>5进位，
# d==5:d后面有非零数字近卫， 没有就奇数进位偶数不进位
print(round(0.375, 2))  #0.38 #奇进偶舍
print(round(0.365, 2))  #0.36 #奇进偶舍
print(round(0.3651, 2))  #0.36 #奇进偶舍
print(round(0.5, 0))  #0.36 #奇进偶舍
print(round(1.5, 0))  #0.36 #奇进偶舍

# 8
if () is ():
    print('() is ()')
# () is ()
if () == ():
    print('() == ()')

# 9
print(ord('a'))

# 10
import subprocess
def listdir_right(directory_):
    return subprocess.check_output(['notepad.exe', directory_], shell=False)
if __name__ == "__main__":
    # _out = listdir_right("d:/abc.txt && calc.exe")
    _out = listdir_right("d:/abc.txt")
