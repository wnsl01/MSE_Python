#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ex130
#코드 입력
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#변동폭, 시가 최고가 정의
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])
#명령문 입력
if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")

