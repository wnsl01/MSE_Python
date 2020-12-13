#!/usr/bin/env python
# coding: utf-8

# In[27]:


#ex270
#Stock 클래스 생성
class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

종목 = []
#값 입력
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
#종목에 삼성 현대차 LG전자 추가
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)
#for문을 이용하여 출력
for i in 종목:
    print(i.code, i.per)


# In[ ]:





# In[ ]:





# In[ ]:




