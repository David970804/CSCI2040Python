import os

if os.path.isfile('p2.py'):
    try:
        from p2 import quicksort
        print('Successfully load p2.py')
        test_case = [[1, 2, 4, 5, 1, 3, 2, -1], [], [4, 3, 2, 1]]
        expected = [[-1, 1, 1, 2, 2, 3, 4, 5], [], [1, 2, 3, 4]]
        try:
            print('Testing...')
            answer = list(map(quicksort, test_case))
            if answer == expected:
                print('You passed all the tests! But still we will check if you use list comprehension')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing quicksort, please check your code')
    except:
        print('Cannot load quicksort, please check the function name or syntax')
else:
    print("Cannot find p2.py, please put p2.py and this test script in the same folder.")