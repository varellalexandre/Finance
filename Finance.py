from Cash import *

if __name__=='__main__':
	a = [2,3,4,5,1,34,12,41,2,3,123,2,3,3,3,3,3,3,3,3]
	b = [3,2,1,4]
	ca = CashFlow(cashflow=a)
	cb = CashFlow(cashflow=b,start=3)
	cc = ca+cb
	print(ca.cashflow)
	print(cb.cashflow)
	print(cc.cashflow)
	print(cb.toPresent(0.1))