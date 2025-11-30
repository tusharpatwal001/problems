from created_complex_number import ComplexNumber

# Test Case 1:
complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, -2)
assert str(complex1) == "3+4i"
assert str(complex2) == "1-2i"
assert str(complex1 + complex2) == "4+2i"
assert str(complex1 - complex2) == "2+6i"
assert str(complex1 * complex2) == "11-2i"
assert str(complex1 / complex2) == "-1.0+2.0i"
assert complex1 != complex2
print("test case 1 passed")

# Test Case 2:
complex3 = ComplexNumber(-2, 5)
complex4 = ComplexNumber(2, 3)
assert str(complex3) == "-2+5i"
assert str(complex4) == "2+3i"
assert str(complex3 + complex4) == "8i"
assert str(complex3 - complex4) == "-4+2i"
assert str(complex3 * complex4) == "-19+4i"
assert str(complex3 / complex4) == "0.8461538461538463+1.2307692307692308i"
assert complex3 != complex4
print("test case 2 passed")
