#!/usr/bin/env python
# coding: utf-8

# In[1]:


ex290
#부모클래스 생성
class 부모:
  def __init__(self):
    print("부모생성")
#자식클래스 생성
class 자식(부모):
  def __init__(self):
    print("자식생성")
    #자식클래스에서 부모클래스 내용 사용
    super().__init__()

나 = 자식()


# In[ ]:




