from random import randint
class Bank():
	default_value_sum=212*(10**6)
	default_investors_count=30 *(10**3)
	banks=[]
	def __init__(self):
		self.investors=[]
		s=Bank.default_value_sum
		previ=0
		for i in range(Bank.default_investors_count):
			i=previ+round(randint(round(1),round(7))/10000,4)
			newval=round(s*(i-previ),2)
			self.investors.append(Investor(newval))
			s-=newval
			previ=round(i,4)
class Investor():
	def __init__(self,depo):
		self.deposit=depo
	def __repr__(self):
		return str(self.deposit)
	def __ge__(self, other):
		return self.deposit>=other.deposit
	def __lt__(self,other):
		return self.deposit<other.deposit
	def __eq__(self,other):
		return self.deposit==other.deposit
	def __add__(self,other):
		self.deposit+=other
		return self
Bank.banks=[]
for i  in range(25000):
	b=Bank()
	Bank.banks.append(b)
	s=0
	mind=1000
	for inv in b.investors:
		s+=inv.deposit
for b in Bank.banks:
	b.investors=sorted(b.investors)
	b.investors[0]+=(Bank.default_value_sum-s)
	print(b.investors[0],b.invesstors[1])
	