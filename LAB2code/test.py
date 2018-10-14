import sys
sys.path.append(r"C:\Users\David\Desktop\CSCI2040\LAB2code")

import p1
print(p1.roman_number(24))
print(p1.roman_number(10000))

import p5
r1 = (4, 3)
print(p5.is_square(r1))
print(p5.height(r1))
print(p5.width(r1))
print(p5.area(r1))
print(p5.perimeter(r1))
r2 = (-1, 3)
print(p5.check_valid(r2))

import p6
test_str = "Alice was born in 1996. "
print( p6.count_alphabet(test_str))
print(p6.vowel_capitalization(test_str))
print(p6.concat(test_str, "She is 22 now. "))
print(p6.search(test_str, "born"))
print(p6.search(test_str, "now"))