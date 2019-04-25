class CashModify:
	def atop(self,tax,periods):
		tax = tax/100
		return (((1+tax)**periods)-1)/(((1+tax)**periods)*tax)

	def ptoa(self,tax,periods):
		tax = tax/100
		return (((1+tax)**periods)*tax)/(((1+tax)**periods)-1)

	def ptof(self,tax,periods):
		tax = tax/100
		return (1+tax)**periods

	def ftop(self,tax,periods):
		tax = tax/100
		return 1/((1+tax)**periods)

	def atof(self,tax,periods):
		tax = tax/100
		return (((1+tax)**periods)-1)/tax

	def ftoa(self,tax,periods):
		tax = tax/100
		return tax/(((1+tax)**periods)-1)

	def transform(self,tax,periods,conversion='F/P'):
		i = 0
		if conversion=='P/A' or conversion=='P/U':
			return self.atop(tax,periods)
		elif conversion=='A/P' or conversion=='U/P':
			return self.ptoa(tax,periods)
		elif conversion=='F/P':
			return self.ptof(tax,periods)
		elif conversion=='P/F':
			return self.ftop(tax,periods)
		elif conversion=='F/A' or conversion=='F/U':
			return self.atof(tax,periods)
		elif conversion=='A/F' or conversion=='U/F':
			return self.ftoa(tax,periods)




