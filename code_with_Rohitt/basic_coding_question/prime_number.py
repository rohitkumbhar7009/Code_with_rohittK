def is_prime(n):
    if n<=1:
        return False 
    for i in range(2,int(n**0.5) +1):
        if  n % i == 0:
            return False
        return True
    

# Example 
# ✅ 1. Check if a Number is Prime
num = 29 
if is_prime(num):
    print(f"{num} is a Prime Number")

else: 
    print(f"{num} is not a Prime Number")


# ✅ 2. Print All Prime Numbers up to N
def print_primes_upto(n):
     for num in range(2,n+1):
        if is_prime(num):
         print(num,end=" ")

print_primes_upto(50)

# ✅ 3. Using Sieve of Eratosthenes (Efficient for Large N)
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit +1)
    p=2
    while p*p <=limit:
        if primes[p]:
            for i in range(p*p,limit+1,p):
                primes[i]=False
        p += 1

    for i in range(2,limit+1):
        if primes[i]:
            print(i,end = " ")

sieve_of_eratosthenes(50)