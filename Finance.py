from Cash import *

if __name__=='__main__':
	a = [2,2,2,2,2,2]
	b = [-10,1,-2,3,3,3,3,3]
	ca = cashflow.CashFlow(cashflow=a)
	cb = cashflow.CashFlow(cashflow=b,start=1)
	cc = ca+cb
	lista = [cb]
	cash = cashengineering.CashEngineering(lista)
	print(cash.TIR()[0])