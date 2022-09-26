from random import random
from math import exp
def poisson(lamb):
	u=random()
	p0=exp(-lamb)
	pk=p0
	sk=p0
	k=0
	while u>sk:
		pk=pk*lamb/(k+1)
		sk=sk+pk
		k+=1
	return k
lamb=5
for i in range(1000):
	print(poisson(lamb),' ',end=" ")
