#!/usr/bin/env python
# coding: utf-8

# In[2]:


#ex200
#값 입력
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
#수익금 계산
profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
#수익금 출력
print(profit)

