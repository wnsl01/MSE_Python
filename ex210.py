#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ex210
#message1()정의
def message1():
    print("A")
#message2()정의
def message2():
    print("B")
#message1(), message2()로 message3() 정의
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()
#message3() 명령
message3()

