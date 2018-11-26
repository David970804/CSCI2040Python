import os

if os.path.isfile('p4.py'):
    try:
        from p4 import get_average_grades
        print('Successfully load p4.py')
        expected = [70, 65.5, 75, 73]
        try:
            print('Testing...')
            answer = get_average_grades('grades.csv')
            if answer == expected:
                print('You passed all the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except Exception as e:
            print('Runtime error when testing get_average_grades, the error message is as follows:')
            print (e)
    except:
        print('Cannot load get_average_grades, please check the function name or syntax')
else:
    print("Cannot find p4.py, please put p4.py and this test script in the same folder.")
