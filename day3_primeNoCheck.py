number = int(input("Enter a number: "))
is_primeNo = True

if number <= 1:
     is_primeNo = False
else: 
    for i in range(2, int(number ** 0.5)+1):      
        if num % i == 0:
            is_primeNo = False     
            break
if is_primeNo:
    print(numner, "is a prime number.")
else:
    print(number, "is not a prime number.")            
    
