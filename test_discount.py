from discount import calculate_discount
#TC01
def test_vip_customer():
    assert calculate_discount(60000000) == 0.1
#TC02
def test_nomal_customer():
    assert calculate_discount(30000000) == 0
#TC03
def test_reach_customer():
    assert calculate_discount(49000000) == 0.1
