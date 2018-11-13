
    
def test_are_equal(actual, expected):       #test 2 values equal. raises assertionerror if not
                                            #actual is actual value produced
                                            #expected is expected value
                                            
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):                   #raise assertionerror if both values not equal
                                            #a is actual value and 
                                            #b is expected value
                
    assert a != b, "did not expect {0} but got {1}".format(a,b)


def test_is_in(collection, item):           #check that a collection contains a given value. raise 
                                            #assertionerror if item not in collection
                                            #collection is the collection to be tested
                                            #item is item being searched for
                                            
    assert item in collection, "{0} does not contain {1}".format(collection, item)
                                        
# Test to fail the `test_are_equal` function
test_are_equal(1, 1)

# Test to fail the `test_not_equal` function
test_not_equal(1, 2)

# Test to fail the `test_is_in` function
test_is_in([1, 3, 2 ], 2)
    