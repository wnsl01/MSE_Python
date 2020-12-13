#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ex180
#리스트 입력
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
#volarity 리스트 생성
volatility = []
#for문으로 변동폭 저장
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])

