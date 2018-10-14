import os

# Exercise 4
if (os.path.isfile('p4.py')):
    try:
        from p4 import divisible_sublist
        print('Load p4.py')
        test1 = [[21, 25, 9, 16, 28], [12, 43, 4, 66, 123, 654]]
        test2 = [3, 4]
        test3 = [7, 9]
        expected = [[21, 9, 28], [12, 4]]
        try:
            print('Testing...')
            answer = list(map(divisible_sublist, test1, test2, test3))
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing divisible_sublist, please check your code!')
    except:
        print('Cannot load divisible_sublist, please check the function name or syntax.')
else:
    print('Cannot find p4.py, please put p4.py and this test script in the same folder.')
