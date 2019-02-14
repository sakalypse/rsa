import math

import MathUtils

CORRESPONDANCE = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SIZE = len(CORRESPONDANCE)

def stringToInt(string):
    """
    transforme une chaine de caractère en nombre
    :param string: la chaine de caractère à convertir
    :return: le nombre converti (au format int)
    """
    number = 0
    for i in range(0, len(string)):
        c = string[i]
        correspondanceIndex = CORRESPONDANCE.find(str.upper(c))
        number += math.pow(SIZE, len(string) - 1 - i) * correspondanceIndex
    return int(number)
	
def intToString(number):
	"""
	transforme un entier en chaine de caractère
	:param number: l'entier à convertir
	:return str: la chaine de caractère convertie
	"""
	r=number%SIZE
	q=int((number-r)/SIZE)
	string = ""
	while q%SIZE > 0:
		string = CORRESPONDANCE[r] + string
		r=q%SIZE
		q=int((q-r)/SIZE)
	string = CORRESPONDANCE[r] + string
	return string