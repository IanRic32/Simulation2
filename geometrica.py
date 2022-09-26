from random import random
from math import log
def geometrica(p):
	u=random()
	return 1+ int(log(1-u)/log(1-p))
suma=0
n=10000
for i in range(n):
	r=geometrica(.25)
	if i <50:
		print(r)
	suma=suma+r
print(suma/n)