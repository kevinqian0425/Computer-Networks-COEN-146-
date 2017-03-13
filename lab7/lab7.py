import math

def main():
    
    #Read input values and check if values are prime. Ask user to re-enter values if inputs are not prime
    p = int(input("Enter prime value for p: "))
    r = int(input("Enter prime value for r: "))

    while (isPrime(p) is False):
        print(p, "must be a prime value")
        p = int(input("Enter prime value for p: "))

    while (isPrime(r) is False):
        print(r, "must be a prime value")
        r = int(input("Enter prime value for r: "))

    #Enter a public and private key
    a = int(input("Enter private key, a: "))
    b = int(input("Enter public key, b: "))

    #Diffie – Hellman algorithm
    A = (p**a)%r
    B = (p**b)%r

    S_Private = (B**a)%r
    S_Public = (A**b)%r

    #Print shared secret key
    if(S_Private == S_Public):
        print("Shared secret key is: ", S_Private)

#function defintion for checking if number is prime
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range (3, int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    
    return True

if __name__ == '__main__':
        main()



