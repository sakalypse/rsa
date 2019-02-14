import math

import MathUtils

correspondance = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
size = len(correspondance)

def stringToInt(string):
    """
    transforme une chaine de caractère en nombre
    :param string: la chaine de caractère à convertir
    :return: le nombre converti (au format int)
    """
    number = 0
    for i in range(0, len(string)):
        c = string[i]
        correspondanceIndex = correspondance.find(str.upper(c))
        number += math.pow(size, len(string) - 1 - i) * correspondanceIndex
    return int(number)
	
def intToString(number):
	"""
	transforme un entier en chaine de caractère
	:param number: l'entier à convertir
	:return str: la chaine de caractère convertie
	"""
	r=number%size
	q=int((number-r)/size)
	string = ""
	while q%size > 0:
		string = correspondance[r] + string
		r=q%size
		q=int((q-r)/size)
	string = correspondance[r] + string
	return string