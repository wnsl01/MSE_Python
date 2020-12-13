#!/usr/bin/env python
# coding: utf-8

# In[11]:


#ex160
#리스트 입력
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
#for문 입력
for 변수 in 리스트:
 split = 변수.split(".")
  #조건문 입력
 if (split[1] == "h") or (split[1] == "c"):
    #값 출력
    print(변수)

