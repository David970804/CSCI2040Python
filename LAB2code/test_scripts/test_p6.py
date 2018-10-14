import os

# Exercise 6
if (os.path.isfile('p6.py')):
    try:
        from p6 import *
        print('Load p6.py')
        try:
            print('Testing...')
            test_string = 'Alice was born in 1996. '

            actual_ans = []
            actual_ans.append(count_alphabet(test_string))
            actual_ans.append(vowel_capitalization(test_string))
            actual_ans.append(concat(test_string, 'She is 22 now. '))
            actual_ans.append(search(test_string, 'born'))
            actual_ans.append(search(test_string, 'now'))
            expected_ans = [14, 'AlIcE wAs bOrn In 1996. ',
                            'Alice was born in 1996. She is 22 now. ', 10, -1]
            if actual_ans == expected_ans:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing TextProcessor, please check your code!')
    except:
        print('Cannot load TextProcessor, please check the class name or syntax.')
else:
    print('Cannot find p6.py, please put p6.py and this test script in the same folder.')
