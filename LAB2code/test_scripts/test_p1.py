import os

# Exercise 1
if (os.path.isfile('p1.py')):
    try:
        from p1 import roman_number
        print('Load p1.py')
        test_case = [-1, 0, 24, 44, 49, 1324, 1234, 456, 9999, 10000]
        expected = ['Number is out of range', 'Number is out of range', 'XXIV', 'XLIV',
                    'XLIX', 'MCCCXXIV', 'MCCXXXIV', 'CDLVI', 'MMMMMMMMMCMXCIX', 'Number is out of range']
        try:
            print('Testing...')
            answer = list(map(roman_number, test_case))
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing roman_number, please check your code!')
    except:
        print('Cannot load roman_number, please check the function name or syntax.')
else:
    print('Cannot find p1.py, please put p1.py and this test script in the same folder.')
