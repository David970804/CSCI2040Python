import os

if os.path.isfile('p2.py'):
    try:
        from p2 import word_count
        print('Successfully load p2.py')
        test_case = [
            (['python is boring',
            'pythom is a large heavy-bodied snake',
            'The python course is worse taking',
            'The python course is worth taking'], 20, 'python'),
            (['python is boring',
              'pythom is a large heavy-bodied snake',
              'The python course is worse taking',
              'The python course is worth taking'], 10, 'python'),
            (['aba', 'bca', 'baba', 'ab'], 2, 'ab')
                     ]
        expected = [2, 3, 2]
        try:
            print('Testing...')
            answer = [word_count(x, n, str) for (x, n, str) in test_case]
            if answer == expected:
                print('You passed all the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing word_count, please check your code')
    except:
        print('Cannot load word_count, please check the function name or syntax')
else:
    print("Cannot find p2.py, please put p2.py and this test script in the same folder.")
