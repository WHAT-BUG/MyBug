'''
@Date               : 2020-03-16 10:38:04
@Author             : Dr.Ren
@Description        : 
@LastEditTime       : 2020-03-16 11:01:23
'''
'''
字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。
例如：
输入：19
输出：2
输入：258
输出：2
输入：0219
输出：3
'''

def how_many_ways(digitarray):
    # implement here
    num = 1
    for i in range(len(digitarray)-1):
        first = digitarray[i]
        if first in ["1","2"]:
            second = digitarray[i+1]
            if int(first+second) <26:
                num +=1
    print(num)       
    return num

while True:
    num0 = input("请输入数字：")
    if not num0.isdigit():
        print("请输入数字")
        continue
    how_many_ways(num0) 
        
        
        
        
