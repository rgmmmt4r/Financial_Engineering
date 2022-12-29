 


1.之前修資工系的專題研究，報告時留下的PTT   
CRR_option_pricing_b04303117 .pdf  
Go to file : https://github.com/rgmmmt4r/Financial_Engineering/blob/master/CRR_option_pricing_b04303117%20.pdf  


2.學習 https://www.codearmo.com/python-tutorial/options-trading-binomial-pricing-model  後，  
模仿教學做出了Binomial Option pricing 的Python 程式碼  
Go to file : https://github.com/rgmmmt4r/Financial_Engineering/blob/master/binomal/binomial.py  


這份code中，使用者可以定價選擇權。  
詳細的說，使用者只需要呼叫  binomial_pricing_EU(S0,sigma,T,r,K,n,type) 即可印出選擇權價格，  
其中 n 是binomial option 切的期數， type 可以是 "call" 或是 "put"   

另外在這份code中，從Yahoo Finance 爬下TSLA的股價，並且畫出定價模型與實際價格的差距
https://github.com/rgmmmt4r/Financial_Engineering/blob/master/binomal/coin%20fliping%20and%20option%20pricing%20for%20TSLA.ipynb  
  
3.學習 https://www.codearmo.com/python-tutorial/options-trading-black-scholes-model 後，  
模仿做出了 Black Scholes Pricing 的程式碼，  
https://github.com/rgmmmt4r/Financial_Engineering/blob/master/Black%20Scholes/Black%20Scholes.ipynb  
這份code中，畫出了在各種變數改變時，選擇權價值變動的圖，  
並且也考慮了有股利的情況。
  
  
4. 使用實作出 Put-call parity，畫出兩個投資組合價值，印證兩個投組價值相同。  
https://github.com/rgmmmt4r/Financial_Engineering/blob/master/Put%20Call%20Parity/Put%20Call%20Parity.ipynb  
