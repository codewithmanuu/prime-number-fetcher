from sympy import primerange

# Get all prime numbers less than or equal to 10


class HelperClass:
    """ Fetching prime numbers using sympy library"""
    def get_prime(self,n):
        primes = list(primerange(1,n+1))
        return primes
    
    """ Fetching prime numbers using custom function """

    def isPrime(self,n):
        if(n==1 or n==0):  return False
        for i in range(2,n):
            if(n%i==0):
                return False
        return True

    def get_primes(self,n):
        primes = []
        for i in range(1,n+1):
            if(self.isPrime(i)):
                primes.append(i)
        return primes