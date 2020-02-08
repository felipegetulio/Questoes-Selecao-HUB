"""Função que retorna o século correspondente ao ano de entrada.
"""

def century(year):

	if(year%100 == 0):
		return year//100
	
	return (year//100) + 1

'''
n = int(input())
print(century(n))
'''