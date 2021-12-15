# Is the number Prime or Not

def isPrime(n):
    for i in range(2, n):
        if (n%i==0):
            break
    else:
        return True
    return False

# print(isPrime(4))

########################################################################

# Print all the prime numbers till the end 

def Primetill(n):
    for i in range(2, n+1):
        is_Prime = isPrime(i)
        if is_Prime:
            print(i)

print(Primetill(20))
