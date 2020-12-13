#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ex120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
#입력
user = input("좋아하는 과일은?")
#조건문 입력
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")

