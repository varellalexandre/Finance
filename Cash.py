class CashFlow:
	def __init__(self,cashflow=[],start=0):
		self.cashflow = []
		self.start = start
		for i in range(self.start):
			self.cashflow.append(0)
		for j in cashflow:
			self.cashflow.append(int(j))

	def __add__(self,o):
		aux = []
		if (len(self.cashflow)) < (len(o.cashflow)):
			diference = (len(o.cashflow))-(len(self.cashflow))
			for i in range(diference):
				self.cashflow.append(0)
			aux = o.cashflow
		elif len(self.cashflow) > len(o.cashflow):
			diference = (len(self.cashflow))-(len(o.cashflow))
			for i in o.cashflow:
				aux.append(int(i))
			for i in range(diference):
				aux.append(0)
		for i in range(len(self.cashflow)):
			aux[i] = self.cashflow[i]+aux[i]
		return CashFlow(cashflow=aux)

	def __sub__(self,o):
		aux = []
		if (len(self.cashflow)) < (len(o.cashflow)):
			diference = (len(o.cashflow))-(len(self.cashflow))
			for i in range(diference):
				self.cashflow.append(0)
			aux = o.cashflow
		elif len(self.cashflow) > len(o.cashflow):
			diference = (len(self.cashflow))-(len(o.cashflow))
			for i in o.cashflow:
				aux.append(int(i))
			for i in range(diference):
				aux.append(0)
		for i in range(len(self.cashflow)):
			aux[i] = self.cashflow[i]-aux[i]
		return CashFlow(cashflow=aux)

	def toPresent(self,tax):
		present_value = 0
		cm = CashModify()
		for i in range(len(self.cashflow)):
			present_value = present_value + self.cashflow[i]*cm.transform(tax,i,'P/F')
		return present_value

	def toFuture(self,tax,periods=1):
		pass

	def toUniform(self,tax,periods=1):
		pass


class CashModify:
	def PGivenA(self,tax,periods):
		return (((1+tax)**periods)-1)/(((1+tax)**periods)*tax)

	def PGivenF(self,tax,periods):
		return (1+tax)**periods

	def transform(self,tax,periods,conversion='F/P'):
		i = 0
		if conversion=='P/A' or conversion=='P/U':
			return self.PGivenA(tax,periods)
		elif conversion=='A/P' or conversion=='U/P':
			return (1/self.PGivenA(tax,periods))
		elif conversion=='F/P':
			return self.PGivenF(tax,periods)
		elif conversion=='P/F':
			return (1/self.PGivenF(tax,periods))
		elif conversion=='F/A' or conversion=='F/U':
			return self.PGivenA(tax,periods)*self.PGivenF(tax,periods)
		elif conversion=='A/F' or conversion=='U/F':
			return (1/self.PGivenA(tax,periods))*(1/self.PGivenF(tax,periods))




