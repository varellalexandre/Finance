from cashmodify import *
class CashFlow:
	def __init__(self,cashflow=[],start=0):
		self.cashflow = []
		self.start = start
		for i in range(self.start):
			self.cashflow.append(0)
		for j in cashflow:
			self.cashflow.append(int(j))

	def __add__(self,o):
		length = len(self.cashflow)
		if len(self.cashflow) < len(o.cashflow):
			length = len(o.cashflow)
		r = CashFlow(start = length)
		for i in range(len(r.cashflow)):
			try:
				r.cashflow[i]  = r.cashflow[i] + self.cashflow[i] 
			except:
				pass
			try:
				r.cashflow[i] = r.cashflow[i] + o.cashflow[i]
			except:
				pass
		return r

	def __sub__(self,o):
		length = len(self.cashflow)
		if len(self.cashflow) < len(o.cashflow):
			length = len(o.cashflow)
		r = CashFlow(start = length)
		for i in range(len(r.cashflow)):
			try:
				r.cashflow[i]  = r.cashflow[i] + self.cashflow[i] 
			except:
				pass
			try:
				r.cashflow[i] = r.cashflow[i] - o.cashflow[i]
			except:
				pass
		return r	

	def toPresent(self,tax):
		present_value = 0
		cashmodify = CashModify()
		for i in range(len(self.cashflow)):
			present_value = present_value + self.cashflow[i]*cashmodify.transform(tax,i,'P/F')
		return present_value

	def toFuture(self,tax,periods=1):
		future_value = self.toPresent(tax)
		return CashModify().transform(tax,periods,'F/P')*future_value

	def toUniform(self,tax,periods=1):
		uniform_value = self.toPresent(tax)
		return CashModify().transform(tax,periods,'U/P')*uniform_value
