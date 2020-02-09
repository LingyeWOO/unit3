Prime numbers
=============
1. Goal: The goal of this program is to determine if the numbers within a particular range is prime or not
2. Version 1

    a. Test all divisors from 2 through n-1
    
   ```.py
   def is_prime_v1(n):
    if n == 1:
      return False # 1 is not prime

    for d in range(2, n):
      if n % d == 0:
        return False
    return True
   ```

    b. Limitations: the time required to execute this program is around 5 seconds, which is too long.

3. Verision 2 

    a. Test all divisors from 2 through square root of (N)
    ```.py
    import math
    import time
    
   def is_prime_v2(n):
    if n == 1:
      return False # 1 is not prime

      # Fins the maximum divisor
      max_divisor = math.floor(math.sqrt(n))

      for d in range(2, 1 + max_divisor):
        if n % d ==0:
          return False
        return True

    # Test the program
    for n in range(1, 21):
      print(n, is_prime_v2(n))
    ```

    b. Limitations: in a sense it is still doing unnecessary job such as testing the even numbers.
    
4. Final version

    a. Test if n is even
    
    b. Test only odd divisors
    
```.py 
import math 

def is_prime(n): 
# Return 'true' if 'n' is a prime number. False otherwise. 

# If 'n' is 2, it is prime. 
# If 'n' is even and not 2 (ex. 4, 6, 8...), then it is not prime. 
if n == 2: 
  return True
if n > 2 and n % 2 == 0: 
  return False
  
max_divisor = math.floor(math.sqrt(n))
for d in range (3, 1 + max_divisor, 2):
  if n % d == 0:
    return False
  return True 
  ```

