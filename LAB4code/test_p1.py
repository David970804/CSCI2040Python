import os

if os.path.isfile('p1.py'):
    try:
        from p1 import *
        print('Successfully load p1.py')
        test_case = ['1 1 + 2 *', '1 3 + 3 % ']
        expected = [4, 1]
        try:
            calc2 = RPNCalculator()
            print('Testing...')
            answer = list(map(calc2.eval, test_case))
            if answer == expected:
                print('You passed all the tests! But still we will check if you use print "divide by 0" for %.')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing RPNCalculator, please check your code')
    except:
        print('Cannot load RPNCalculator, please check the function name or syntax')
else:
    print("Cannot find p1.py, please put p1.py and this test script in the same folder.")