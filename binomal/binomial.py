import math
import numpy as np
from decimal import Decimal

#fair value for filp coin game
n = 10
fair_value = 0
for i in range(7,n+1):
    fair_value += math.comb(n, i) *0.5**i*0.5**(n-i)*i
    #print (math.comb(n, i))
#print(fair_value)


#模擬ST
S0 = 100
sigma = 0.4
n = 4
T = 0.5
r = 0.05
K = 105
delta_t = T/n 
u = np.exp(  sigma * np.sqrt(delta_t))
d = np.exp(  -sigma * np.sqrt(delta_t))
p = (np.exp( r*delta_t) -d)/(u-d) # u 的 risk neutral機率
#print("p",p)
ST = 0
for i in range(n+1):
    ST = S0 *  u**i*d**(n-i)
    #print (math.comb(n, i))
    #print("ST:", ST)
    CT = round( max(ST-K,0),2)
    #print("CT:", CT)


#計算每個node 的機率
for i in range(n+1):
    this_node_prob =  round (math.comb(n, i)*(p)**i*(1-p)**(n-i),2)
    #print(this_node_prob)


#計算call 選擇權價格
call_price = 0

for i in range(n+1):
    ST = S0 *  u**i*d**(n-i)
    CT = round( max(ST-K,0),2)
    this_node_prob =  round (math.comb(n, i)*(p)**i*(1-p)**(n-i),2)
    call_price += CT * this_node_prob
    pv_call_price = np.exp(-r*T)*call_price 

#print("pv_call_price:", round( pv_call_price,2))

def binomial_pricing_EU(S0,sigma,T,r,K,n,type):
    delta_t = T/n 
    u = np.exp(  sigma * np.sqrt(delta_t))
    d = np.exp(  -sigma * np.sqrt(delta_t))
    p = (np.exp( r*delta_t) -d)/(u-d) # u 的 risk neutral機率
    future_price = 0
    if type == "call":
        for i in range(n+1):
            ST = S0 *  u**i*d**(n-i)
            CT = Decimal( max(ST-K,0))
            this_node_prob =  Decimal(combin(n,i)*(p)**i*(1-p)**(n-i))
            future_price += CT * this_node_prob
    elif  type == "put":
        for i in range(n+1):
            ST = S0 *  u**i*d**(n-i)
            PT = Decimal(max(K-ST,0))
            this_node_prob =   Decimal(combin(n,i)*(p)**i*(1-p)**(n-i))
            future_price += PT * this_node_prob
    else:
        return "must input call or put"
    pv_price = Decimal(np.exp(-r*T))*future_price 
    #print("pv_call_price:", round( pv_call_price,2))
    return  round( pv_price,2)

def combin(n,i):
    return math.factorial(n)//( math.factorial(i)*math.factorial(n-i))


N = [4,8,100,1000]
for i in N:
    print("call price:",binomial_pricing_EU(S0,sigma,T,r,K,i,"call"))



N = [4,8,100,1000]
for i in N:
    print("put price:",binomial_pricing_EU(S0,sigma,T,r,K,i,"put"))







