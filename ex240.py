#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ex240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
#함수 2부터 2를 넣고 함수 1에 그 값을 넣은 뒤 함수 0에 넣는다.

