import numpy as np
import pandas as pd

db = pd.read_csv("statement.csv", dtype = str)

credits = db['Credit']

def change_to_int(num):
    try:
        a = num.split('.')[0]
        a = ''.join(a.split(','))
        a = int(a)
        return a
    except:
        return 0

def add_comma(string, index):
    a = string[:index]
    b = string[index:]
    return a+','+b


def change_to_str(num):
    num = list(str(num))
    if len(num) <= 3:
        return ''.join(num)+'.00'

    i = len(num)-3
    num.insert(i, ',')
    i -= 2
    while(i > 0):
        num.insert(i,',')
        i -= 2
    num = ''.join(num)
    return num+'.00'


int_credits = []
for x in credits:
    int_credits.append(change_to_int(x))

total = change_to_str(sum(int_credits))
print(total)