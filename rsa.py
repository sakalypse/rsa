from math import *
import random

def exponentiationModulaire(x,k,n):
	#convertion de l'exposant k en écriture binaire
	listeBinaire = []
	ki=k
	while ki!=0:
		r=ki%2
		listeBinaire.append(int(r))
		ki = (ki-r)/2

	#calcul des xi exposant 2 exposant i
	listeX = []
	for i in range(len(listeBinaire)):
		if listeBinaire[i] == 1:
			listeX.append(x**(2**i))

	#multiplication des xi
	xk = 1
	for i in range(len(listeX)):
		xk *= listeX[i]
		
	#return l'application du modulo
	return xk % n

def euclideEtendu(a,b):
	r1, r2 = a,b
	u1, v1 = 1,0
	u2, v2 = 0,1
	while(r2!=0):
		q=r1//r2
		rBuffer = r1
		uBuffer = u1
		vBuffer = v1

		r1=r2
		u1=u2
		v1=v2

		r2 = rBuffer - q*r2
		u2 = uBuffer - q*u2
		v2 = vBuffer - q*v2
	print(r1, u1, v1)
	return [r1,u1,v1]

def inverseModulaire(a, N):
	resultEuclide = euclideEtendu(a,N)
	return resultEuclide[1]

#retourne c et d
def generationExposants(p,q):
	c = random.randint(3,(p-1)*(q-1)-1)
	while (testDePrimalite(c)!=1 or euclideEtendu(c,(p-1)*(q-1))[0]!=1):
		c = random.randint(3,(p-1)*(q-1)-1)	
	d = inverseModulaire(c, (p-1)*(q-1))	
	return [c,d]

def testDePrimalite(n):
	if n%2==0:
		return 0
	if 3<sqrt(n):
		for i in range (3,int(sqrt(n)),+2):
			if n%i==0:
				return 0
	return 1

#retourne le message chiffré
def chiffrement(m,n,c):
	return exponentiationModulaire(m,c,n)

#retourne le message déchiffré
def dechiffrement(mChiffre,n,d):
	return exponentiationModulaire(mChiffre,d,n)

def mainTest():
	p=3
	q=11
	n = p*q
	phin = (p-1)*(q-1)
	c = 3
	d = inverseModulaire(c,phin)
	m = 4 #message
	
	print('c = ',c,' ; d = ',d)
	mChiffre = chiffrement(m, n, c)
	print('Message chiffré : ', mChiffre)
	m = dechiffrement(mChiffre, n, d)
	print('Message déchiffré : ', m)
	
mainTest()
