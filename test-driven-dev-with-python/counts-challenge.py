def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("Fuck OFF") == 3, "should be 4 upper case"

#output "should be 4 upper case"