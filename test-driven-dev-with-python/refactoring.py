#follow on from test-driven-development
def is_even(number):            
    return number % 2 == 0      #returns true/false whether number even/not

def even_number_of_evens(numbers):
    
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)
    
    """     this reduces to line 7/8 above
    evens = 0               #initialise a variable to say currently zero evens   
        
        
                                    #loop to check each number and see if it's even
    for n in numbers:
        if is_even(n):              #remainder when divided by 2 is zero(modulo)..then is even number
            evens += 1              #if even...increment by 1
            
    if evens == 0:                  # if number of evens = 0
        return False
    else:    
        return is_even(evens)           #returns true if number of evens is even
        """
        
        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "2 even numbers"
assert even_number_of_evens([2]) == False, "1 even number"
assert even_number_of_evens([1,3,9]) == False, "3 odd numbers"

print("All tests passed!")