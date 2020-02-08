"""Função que retorna o somatório dos n primeiros números primos.
"""

def is_prime(n):

	if(n%2==0 or n%3==0 or n<5):
		return (n==2) or (n==3)

	i = 5
	while(i*i <= n):
		if(n%i==0 or n%(i+2)==0):
			return False
		i += 6

	return True


def n_prime_sum(n):

	prime_sum = 0
	num = 2

	while(n):
		if(is_prime(num)):
			prime_sum += num
			n -= 1
		num += 1

	return prime_sum

'''
n = int(input())
print(n_prime_sum(n))
'''