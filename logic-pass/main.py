import math

from sqlalchemy import false;

def remove_char(str,char):
    return str.replace(char,'')


#For some reasone i read it as even so this is the new sul:
def find_primes(n):
   primes = [];
   for num in range(1, n  ): 
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
   return primes
print(find_primes(50))


def count_repeated_characters(str,char):
    count = 0
    for key in str:
        if key == char:
            count +=1
    return count
 
        
