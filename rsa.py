# RSA implementation in python
from random import randrange
#随机选择两个不相等的质数p,q
#素性检验使用Solovay-Stassen素性检验
#计算p和q的乘积n
#计算n的欧拉函数φ(n) = (p-1)(q-1)
#随机选择一个整数e，1 < e < φ(n)，且e与φ(n)互质

# test if n is probably prime, using accuracy of k
def probablePrime(int n, int k)
	if(n == 2):
		return 1
	else if(n % 2 == 0 or n == 1) return 0
	while(k-- > 0):
		if(!solovayPrime(randrange(1, n - 1, 1), n)):
			return 0
	return 1

# find a random prime between 3 and n - 1
def randPrime(int n):
	prime = randrange(3, n, 2)
	n = n + (n%2)
	while(1):
		if (probablePrime(prime, ACCURACY)):
			return prime
		prime = (prime + 2) % n
#计算e对于φ(n)的模反元素d，使得ed被φ(n)除的余数为1
#ed ≡ 1 (mod φ(n))
#ed - 1 = kφ(n)
#也就是ex + φ(n)y = 1
#可以用扩展欧几里得算法求解
#求得的x也就是要求的d
#将n和e封装成公钥，n和d封装成私钥


#加密方法
#如果是加密整数m(m < n)那么就需要
#求m的e次方被n模的余数c
#c就是密文
#解密方法
#求c的d次方被n模的余数m，m就是明文

if __name__ == "__main__":
	# p, q, n, phi, e, d
	ACCURACY = 5
	SINGLE_MAX = 10000
	EXPONENT_MAX = 1000
	BUF_SIZE = 1024
	
	while(1):
		p = randPrime(SINGLE_MAX)
		print("Got first prime factor, p = %d ...", p)
		q = randPrime(SINGLE_MAX)
		print("Got second prime factor, q = %d ...", q)
	
		n = p * q
		printf("Got modulus, n = pq = %d...", n)
		if(n < 128):
			print("Modulus is less than 128, cannot encode  single bytes. Trying again ...");
		else:
			break