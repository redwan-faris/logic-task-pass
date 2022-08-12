def remove_char(str,char):
    return str.replace(char,'')

def find_prime_numbers(n):
    primes = []
    for number in range(n):
        if(number % 2 ==0):
            primes.append(number)
    return primes

def count_repeated_characters(str,char):
    count = 0
    for key in str:
        if key == char:
            count +=1
    return count

print(count_repeated_characters('reddeeee','d'))
        
