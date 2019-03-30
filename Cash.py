class CashFlow:
	def __init__(self,cashflow=[],start=0):
		self.cashflow = []
		self.start = start
		for i in range(self.start):
			self.cashflow.append(0)
		for j in cashflow:
			self.cashflow.append(int(j))

	def __add__(self,o):
		if (len(self.cashflow)) < (len(o.cashflow)):
			diference = (len(o.cashflow))-(len(self.cashflow))
			for i in range(diference):
				self.cashflow.append(0)

		for i in range(len(self.cashflow)):
			self.cashflow[i] = self.cashflow[i]+o.cashflow[i]

	def __sub__(self,o):
		if (len(self.cashflow)) < (len(o.cashflow)):
			diference = (len(o.cashflow))-(len(self.cashflow))
			for i in range(diference):
				self.cashflow.append(0)

		for i in range(len(self.cashflow)):
			self.cashflow[i] = self.cashflow[i]-o.cashflow[i]

	def toPresent(self,tax):
		present_value = 0
		for i in range(len(self.cashflow)):
			present_value = present_value + self.cashflow[i]*CashModify.transform('P/F',tax,i+self.start)
		return present_value
		
	def toFuture(self,tax,periods=1):
		pass

	def toUniform(self,tax,periods=1):
		pass


class CashModify:
	def transform(self,conversion='F/P',tax,periods):
		i = 0
		if conversion=='P/A' or conversion=='P/U':
			return self.PGA(tax,periods)
		elif conversion=='A/P' or conversion=='U/P':
			return (1/self.PGA(tax,periods))
		elif conversion=='F/P':
			return self.PGF(tax,periods)
		elif conversion=='P/F':
			return (1/self.PGF(tax,periods))
		elif conversion=='F/A' or conversion=='F/U':
			return self.PGA(tax,periods)*self.PGF(tax,periods)
		elif conversion=='A/F' or conversion=='U/F':
			return (1/self.PGA(tax,periods))*(1/self.PGF(tax,periods))

	def PGA(self,tax,periods):
		return (((1+tax)**periods)-1)/(((1+tax)**periods)*tax)

	def PGF(self,tax,periods):
		return (1+tax)**periods



