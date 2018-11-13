def test_are_equal(actual, expected):   #test 2 values equal. otherwise assertionError. 

    assert expected == actual, "Expected {0}, but got {1}".format(expected, actual)
    
def test_not_equal(a, b):   #test 2 values not equal. 
    
    assert a != b, "Did not extpect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):   # check a value is contained in a collection. raise assertionError if not
    
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    
    assert item not in collection, "{0} is not in {1}".format(item, collection)
    
    
def test_between(lower_limit, upper_limit, actual):
    
    assert lower_limit <= actual <=upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)
    
test_are_equal(3,3)     

test_not_equal(0, 1)            #passes because 0 != 1 

test_is_in([1,2], 2)            #passes because 2 is in the list

test_not_in([1,2,3,4,5], 6)     #passes because 6 not in the list

test_between(1, 10, 9)          #passes because 9 is between 1-10
    
        
        