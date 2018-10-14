import os

# Exercise 3
if (os.path.isfile('p3.py')):
    try:
        from p3 import letter_count
        print('Load p3.py')
        test_case = ['This is a test! Just Write somEthIng RAndOmlY123',
                     'The quick brown fox jumps over the lazy dog',
                     'CSCI2040--Introduction to Python',
                     'Teacher: Prof. John C.S. Lui',
                     'Have fun!']
        expected = [[('a', 2), ('d', 1), ('e', 3), ('g', 1), ('h', 2), ('i', 4), ('j', 1), ('l', 1), ('m', 2), ('n', 2), ('o', 2), ('r', 2), ('s', 5), ('t', 6), ('u', 1), ('w', 1), ('y', 1)], [('a', 1), ('b', 1), ('c', 1), ('d', 1), ('e', 3), ('f', 1), ('g', 1), ('h', 2), ('i', 1), ('j', 1), ('k', 1), ('l', 1), ('m', 1), ('n', 1), ('o', 4), ('p', 1), ('q', 1), ('r', 2), ('s', 1), ('t', 2), ('u', 2), ('v', 1), ('w', 1), ('x', 1), ('y', 1), ('z', 1)], [('c', 3), ('d', 1), ('h', 1), ('i', 3), ('n', 3), ('o', 4), ('p', 1), ('r', 1), ('s', 1), ('t', 4), ('u', 1), ('y', 1)], [('a', 1), ('c', 2), ('e', 2), ('f', 1), ('h', 2), ('i', 1), ('j', 1), ('l', 1), ('n', 1), ('o', 2), ('p', 1), ('r', 2), ('s', 1), ('t', 1), ('u', 1)], [('a', 1), ('e', 1), ('f', 1), ('h', 1), ('n', 1), ('u', 1), ('v', 1)]]
        try:
            print('Testing...')
            answer = list(map(letter_count, test_case))
            if answer == expected:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing letter_count, please check your code!')
    except:
        print('Cannot load letter_count, please check the function name or syntax.')
else:
    print('Cannot find p3.py, please put p3.py and this test script in the same folder.')
