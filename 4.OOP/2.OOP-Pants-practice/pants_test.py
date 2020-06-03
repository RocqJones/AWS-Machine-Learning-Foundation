from pants import Pants

def check_results():
    pants = Pants('red', 35, 36, 15.12)

    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12
    
    pants.change_price(10) == 10
    assert pants.price == 10
    
    assert pants.discount(.1) == 9
    
    print('You made it to the end of the check. Nice job!')

check_results()