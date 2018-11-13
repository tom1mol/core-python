def number_of_evens(numbers):
    return 0 


def test_are_equal(actual, expected):   ##if not equal..error message with values using format function
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual) 
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b) 
#a(expected)not equal b(actual)                                     # !=(not equal)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
                                #collection does not contain item
    
test_are_equal(number_of_evens([1,2,3,4,5]), 2) 
#call testing function(test_are_equal).pass in array 1,2,3,4,5.. expect number 2(2 even numbers)
