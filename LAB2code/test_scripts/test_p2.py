import os

# Exercise 2
if (os.path.isfile('p2.py')):
    try:
        from p2 import recursive_pow
        print('Load p2.py')
        test1 = [-1, 0, 4, 9, -11, 15, 26, -77, 88, 100]
        test2 = [0, 5, 7, 8, 3, 2, 8, 11, 20, 12]
        expected = [1, 0, 16384, 43046721, -1331, 225, 208827064576, -564154396389137449973,
                    775627936381895764407110123826159026176, 1000000000000000000000000]
        try:
            print('Testing...')
            answer = list(map(recursive_pow, test1, test2))
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing recursive_pow, please check your code!')
    except:
        print('Cannot load recursive_pow, please check the function name or syntax.')
else:
    print('Cannot find p2.py, please put p2.py and this test script in the same folder.')
