import os

if os.path.isfile('p3.py'):
    try:
        from p3 import load_data
        print('Successfully load p3.py and function load_data')
        test_case = ['dept-prof.pydata']
        expected = [{'Economics': ['Andrew', 'David', 'Jason', 'Julian'], 'Computer Science': ['John', 'James', 'Andrew', 'Michael', 'Leo', 'Kevin'], 'Artificial Intelligence': ['Jack', 'Clare', 'Daisy', 'Alice'], 'Math': ['Ann', 'Andrew', 'David', 'George']}]
        try:
            print('Testing...')
            answer = list(map(load_data, test_case))
            if answer == expected:
                print('You passed the test, but we will also manually grade the function load_data')
            else:
                print('Wrong result!')
        except:
            print('Runtime error when testing load_data, please check your code')
    except:
        print('Cannot load load_data, please check the function name or syntax')

    print()

    try:
        from p3 import query
        print('Successfully load p3.py and function query')
        test_case = ['David', 'John', 'Z']
        expected = [['Economics', 'Math'], ['Computer Science'], []]
        try:
            print('Testing...')
            answer = list(map(query, test_case))
            answer = [sorted(i) for i in answer]
            expected = [sorted(i) for i in expected]
            if answer == expected:
                print('You passed all the tests!')
            else:
                print('Wrong answer, you failed some of the tests!')
        except:
            print('Runtime error when testing query, please check your code')
    except:
        print('Cannot load query, please check the function name or syntax')

    print()

    try:
        from p3 import update
        import pickle
        print('Successfully load p3.py and function update')

        expected = {'Space Engineering': ['Musk', 'Andy', 'Jane'], 'Computer Science': ['John', 'James', 'Andrew', 'Michael', 'Leo', 'Kevin'], 'Math': ['Ann', 'Andrew', 'David', 'George'], 'Economics': ['Andrew', 'David', 'Jason', 'Julian']}

        try:
            print('Testing...')
            update()
            file_object = open('dept-prof-updated.pydata', 'rb')
            answer = pickle.load(file_object)
            file_object.close()
            if answer == expected:
                print('You passed the test, but we will also manually grade the function update')
            else:
                print('Wrong result!')
        except:
            print('Runtime error when testing update, please check your code')
    except:
        print('Cannot load query, please check the function name or syntax')

    print()

    try:
        from p3 import get_depts_size
        print('Successfully load p3.py and function get_depts_size')
        expected = {'Economics': 4, 'Computer Science': 6, 'Math': 4, 'Space Engineering': 3}
        try:
            print('Testing...')
            answer = get_depts_size()
            if answer == expected:
                print('You passed the test, but we will also manually grade the function get_depts_size')
            else:
                print('Wrong result!')
        except:
            print('Runtime error when testing get_depts_size, please check your code')
    except:
        print('Cannot load query, please check the function name or syntax')



else:
    print("Cannot find p3.py, please put p3.py and this test script in the same folder.")