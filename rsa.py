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
		q=int(r1/r2)
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
	return resultEuclide[1]

#return c et d
def generationExposants(p,q):
	i=2
	while euclideEtendu(i,(p-1)*(q-1))[0]!=1 or i <= ((p-1)*(q-1)):
		i+=1
	if i==((p-1)*(q-1)):
		print("C non trouvé")
		return
	else:
		c = i

	d = inverseModulaire(c, (p-1)*(q-1))

	print(c)
	print(d)

generationExposants(7307,5923)
#print(inverseModulaire(7,10*16))
