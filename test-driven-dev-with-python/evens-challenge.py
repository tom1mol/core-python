def even_number_of_evens(numbers):
    if numbers == []:           #check to see if list is empty
        return False
    else:                       #set a "num of evens variable" that increments each time even num found
        evens = 0
        
    for number in numbers:
        if number % 2 == 0:     #if number is even..increment evens counter
            evens += 1
    
    if evens == 0:              #if evens counter = 0  return false
        return False
    else:
        return evens % 2 == 0   #returns true/false depending on whether evens is odd/even

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, ("One even number")
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, 3 even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, 4 even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")