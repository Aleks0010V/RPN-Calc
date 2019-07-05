from calc import calculate, rpn, solve, calc

'''
Tests for calculate
'''

def test_substracting():
    assert calculate(5, 45, '-') == 40

def test_adding():
    assert calculate(5, 45, '+') == 50

def test_dividing():
    assert calculate(5, 45, '/') == 9

def test_multiplication():
    assert calculate(5, 45, '*') == 225

def test_negative_0():
    assert calculate(-1, -3, '-') == -2

def test_negative_1():
    assert calculate(10, -15, '*') == -150

def test_negative_2():
    assert calculate(-3, 33, '/') == -11

################################################################################

'''
Tests for rpn
'''

def test_rpn_0():
    assert rpn(['45', '-', '5', '|']) == [45, 5, '-']

def test_rpn_1():
    assert rpn(['45', '+', '5', '|']) == [45, 5, '+']

def test_rpn_2():
    assert rpn(['45', '-', '5', '*', '9', '+', '6', '/', '2', '|']) == [45, 5, 9, '*', '-', 6, 2, '/', '+']

def test_rpn_3():
    assert rpn(['1', '*', '2', '*', '3', '*', '4', '*', '5', '|']) == [1, 2, '*', 3, '*', 4, '*', 5, '*']

def test_rpn_4():
    assert rpn(['1', '*', '2', '/', '3', '*', '4', '/', '5', '|']) == [1, 2, '*', 3, '/', 4, '*', 5, '/']

def test_rpn_5():
    assert rpn(['(', '8', '+', '2', '*', '5', ')', '/', '(', '1', '+', '3', '*', '2', '-', '4', ')', '|']) == [8, 2, 5, '*', '+', 1, 3, 2, '*', '+', 4, '-', '/']

################################################################################

'''
Tests for solve
'''

def test_solve_0():
    assert solve([45, 5, 9, '*', '-', 6, 2, '/', '+']) == 3

def test_solve_1():
    assert solve([45, 5, '+']) == 50

def test_solve_3():
    assert solve([45, 5, '-']) == 40

def test_solve_4():
    assert solve([1, 2, '*', 3, '*', 4, '*', 5, '*']) == 120

def test_solve_5():
    assert solve([25, 4, '*', 3, '*', 10, '/', 5, 6, '*', 3, '/', 4, '*', '-', 10, 11, '*', 12, '*', 15, '/', '+']) == 78

################################################################################

'''
Tests for calc
'''

def test_calc_0():
    assert calc('45 - 5') == 40

def test_calc_1():
    assert calc('( 66 - 6 * 11 + 5 - 12 * 7 / 8 ) / 4') == -1.375

def test_calc_2():
    assert calc('( 65 - 56 * 2 / ( 5 - 6 ) + 25 )') == 202

def test_calc_3():
    assert calc ('( 8 + 2 * 5 ) / ( 1 + 3 * 2 - 4 )') == 6
