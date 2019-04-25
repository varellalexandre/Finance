from cashflow import *

class CashEngineering:
	def __init__(self,list_options=[],market_tax = 6):
		self.tma = market_tax
		assert type(list_options) is list
		for i in list_options:
			assert isinstance(i, CashFlow)
		self.list_options = list_options

	def setTMA(self,tma):
		self.tma = tma

	def VPL(self):
		try:
			best_option = self.list_options[0]
			vpl = best_option.toPresent(self.tma)
			for i in range(len(self.list_options)-1):
				vpl = (best_option - self.list_options[i+1]).toPresent(self.tma)
				if vpl < 0:
					best_option = self.list_options[i+1]
			return vpl,best_option
		except:
			return None

	def VUL(self):
		try:
			best_option = self.list_options[0]
			vul = best_option.toUniform(self.tma)
			for i in range(len(self.list_options)-1):
				vul = best_option.toUniform(self.tma,periods=len(best_option.cashflow)) - self.list_options[i+1].toUniform(self.tma,periods=len(self.list_options[i+1].cashflow))
				if vul < 0:
					best_option = self.list_options[i+1]
			return vul,best_option
		except:
			return None

	def secTir(self,a,acc = .0001,cont = 1000):
"""		x = 1000
		y = CashEngineering(list_options=[a])
		y.setTMA(100)
		yold = CashEngineering(list_options=[a])
		yold.setTMA(0)
		vpl = 100
		while i<cont and (vpl>acc or vpl< -1*acc):
			i = i+1
			xold
			y.setTMA(xold)
			yold.setTMA(xtemp)
			x = xold - y.VPL()[0]*((xold-xtemp)/self.oneIfZero((y.VPL()[0]-yold.VPL()[0])))
			y.setTMA(x)
			vpl = y.VPL()[0]
		return vpl"""
				

	def TIRM(self,cashflow,capitacao,reinvestimento):
		presente = CashFlow(cashflow = [0 for i in cashflow.cashflow],market_tax=capitacao)
		futuro  = CashFlow(cashflow = [0 for i in cashflow.cashflow],market_tax=futuro)
		for i in range(len(cashflow.cashflow)):
			if cashflow.cashflow[i] >= 0:
				futuro[i] = cashflow.cashflow[i]
			else :
				presente[i] = cashflow.cashflow[i]
		presente.toPresent(capitacao)
		futuro.toFuture(reinvestimento)
		resp = futuro - presente
		return CashEngineering(list_options = [resp]).TIR()

	def TIR(self):
		for i in range(len(self.list_options)-1):
			if self.list_options[i].cashflow[0]<self.list_options[i+1].cashflow[0]:
				self.list_options[i].cashflow[0],self.list_options[i+1].cashflow[0] = self.list_options[i+1].cashflow[0],self.list_options[i].cashflow[0]
		tir = 0
		best_option = self.list_options[0]
		for i in range(len(self.list_options)-1):
			tir = self.secTir(best_option-self.list_options[i+1])
			if tir<self.tma:
				best_option = self.list_options[i+1]
		else:
			tir = self.secTir(best_option)
		return tir,best_option


	def WACC(self,fp,fd,re,rd,t):
		self.tma = ((fp/(fp+fd))*re)+((fd/(fp+fd))*rd)*(1-t)
		return self.tma

	def CAPM(self,beta,rm,rf = 0.06):
		self.capm = rf + beta*(rm-rf)
		return self.capm

	def oneIfZero(self,a):
		if a == 0:
			return 1
		return a





