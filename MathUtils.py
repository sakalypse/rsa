from math import *
import random

def exponentiationModulaire(x,k,n):
	"""
	retourne l'exponentiation Modulaire : x^k mod n
	params: x: la valeur x
	params: k: exposant de x
	params: n: le modulo
	return: l'exponentiation Modulaire
	"""
	result = 1
	while k > 0:
		if (k & 1) > 0:
			result = (result * x) % n
		k >>=1
		x = (x ** 2) % n
	return result

def euclideEtendu(a,b):
	"""
	retourne l'euclideEtendu
	params: a:
	params: b:
	return: r1:
			u1:  
			v1:
			tel que r1 = u1 * a + v1 * b 
	"""
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
	return [r1,u1,v1]

def inverseModulaire(a, N):
	resultEuclide = euclideEtendu(a,N)
	return resultEuclide[1] % N

def generationExposants(p,q):
	"""
	retourne c, nombre premier avec phi de n et d, inverse modulaire de c
	params: p:
	params: q:
	return: c et d en tableau
	"""
	c = random.randint(3,(p-1)*(q-1)-1)
	while (testDePrimalite(c)!=1 or euclideEtendu(c,(p-1)*(q-1))[0]!=1):
		c = random.randint(3,(p-1)*(q-1)-1)	
	d = inverseModulaire(c, (p-1)*(q-1))	
	return [c,d]

def testDePrimalite(n):
	"""
	Retourne vrai en faux en testant si n est un nombre premier
	params: n: nombre a tester
	return: 1 ou 0 en fonction du test
	"""
	if n%2==0:
		return 0
	if 3<sqrt(n):
		for i in range (3,int(sqrt(n)),+2):
			if n%i==0:
				return 0
	return 1
	
def chiffrement(m,n,c):
	"""
	retourne le message chiffré
	params: m: le message à chiffré
	params: n: p*q
	params: c: l'entier premier avec phi de n
	return: le message chiffré
	"""
	return exponentiationModulaire(m,c,n)

def dechiffrement(mChiffre,n,d):
	"""
	retourne le message déchiffré
	params: mChiffre: le message à déchiffré
	params: n: p*q
	params: d: l’inverse modulaire de c modulo phi de n.
	return: le message déchiffré
	"""
	return exponentiationModulaire(mChiffre,d,n)

if __name__ == '__main__':
	print(exponentiationModulaire(4,13,497))
	print(inverseModulaire(334, 223))
	print(euclideEtendu(135,101))
	p=7307
	q=5923
	n = p*q
	phin = (p-1)*(q-1)
	c = 11
	d = inverseModulaire(c,phin)
	m = 4 #message
	
	print('c = ',c,' ; d = ',d)
	mChiffre = chiffrement(m, n, c)
	print('Message chiffré : ', mChiffre)
	m = dechiffrement(mChiffre, n, d)
	print('Message déchiffré : ', m)

