#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ex220
#입력
def print_max(a, b, c) :
    max_val = 0
#if문 작성    
    if a > max_val :
        max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c
    #값 출력
    print(max_val)

