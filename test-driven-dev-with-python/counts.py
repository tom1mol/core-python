def count_upper_case(message):      #count num uppercase characters in a message
    count = 0                       #starts by setting counter value to zero
    for c in message:               #walks through the message
        if c.isupper():             #If character is uppercase
            count += 1              #counter is incremented
    return count                    #count is returned when walkthrough complete
    
#print(count_upper_case("Hello World FANNY"))  #this counts 7 uppercase letters

assert count_upper_case("") == 0,"Empty string"
assert count_upper_case("A") == 0, "One upper case"     #fails...One upper case
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("%£$$") == 0, "Special characters"
#the way assert works..if it throws an error..program execution stops at that point

print("All the tests passed")