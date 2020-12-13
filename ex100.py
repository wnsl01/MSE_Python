#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ex100
#값 입력
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
#zip과 dict을 사용하여 딕셔너리를 생성한다
close_table = dict(zip(date, close_price))
#출력
print(close_table)

