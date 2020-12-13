#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ex300
#값 입력
per = ["10.31", "", "8.00"]

#for문 사용 try코드 사용
for i in per:
    try:
        print(float(i))
    #예외가 발생시 수행하는 except코드 사용
    except:
        print(0)
    #예외가 없을시 수행하는 else코드 사용
    else:
        print("clean data")
    #항상 수행할 코드(출력)
    finally:
        print("변환 완료")


# In[ ]:




