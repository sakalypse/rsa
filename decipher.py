import math
import MathUtils
import StringUtils
	
def TrouverClePrivee(n, c):
	"""
	Trouve la clé privée associée à une clé publique
	param n: n de la clé publique
	param c: d de la clé publique
	return: l'entier d de la clé publique
	"""
	
	divider = [d for d in range(2, int(math.sqrt(n))) if n%d == 0]
	p = divider[0]
	q = n/p
	d = int(MathUtils.inverseModulaire(c, (p - 1) * (q - 1)))
	return d
	
if __name__ == '__main__':
	print(MathUtils.dechiffrement(106, 221, 1997))

	n=int(input("entrez la valeur 'n' de votre cle publique: "))
	c=int(input("entrez la valeur 'd' de votre cle publique: "))
	
	d=TrouverClePrivee(n, c)
	print ("la cle privee est {}".format(d))
	choix=input("voulez vous utiliser cette cle pour dechiffrer un message? (o/n)")
	if choix == "o":
		message = input("Entrez le message chiffre:")
		messageInt = StringUtils.stringToInt(message)
		print("message int: {}".format(messageInt))
		messageDecripte=MathUtils.dechiffrement(messageInt, n, d)
		print("message descripte: {}".format(messageDecripte))
		messageDecripteStr=StringUtils.intToString(messageDecripte)
		print("le message dechiffre est: {}".format(messageDecripteStr))