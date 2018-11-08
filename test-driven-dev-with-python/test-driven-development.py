def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else:
        evens = 0               #initialise a variable to say currently zero evens   
        
        
                                    #loop to check each number and see if it's even
    for n in numbers:
        if n % 2 == 0:              #remainder when divided by 2 is zero(modulo)..then is even number
            evens += 1              #if even...increment by 1
            
    return evens % 2 == 0           #returns true if number of evens is even
        
        
        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "2 even numbers"
assert even_number_of_evens([2]) == False, "1 even number"

print("All tests passed!")