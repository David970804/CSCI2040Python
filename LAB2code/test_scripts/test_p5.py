import os
import math

# Exercise 5
if (os.path.isfile('p5.py')):
    try:
        from p5 import *
        print('Load p5.py')
        # test input
        rectangles = [(-1, 0), (3, 4), (10, 10)]

        # expected answers
        expected_ans = [[False],
                        [True, False, 5.0, 3, 4, 12, 14],
                        [True, True, math.sqrt(200), 10, 10, 100, 40]]
        try:
            print('Testing...')
            actual_ans = []
            # test case 1: (-1,0)
            actual_ans.append([check_valid(rectangles[0])])


            # test case 2: (3, 4)
            actual_ans.append([check_valid(rectangles[1]),
                               is_square(rectangles[1]),
                               diagonal_len(rectangles[1]),
                               height(rectangles[1]),
                               width(rectangles[1]),
                               area(rectangles[1]),
                               perimeter(rectangles[1])])

            # test case 2: (10, 10)
            actual_ans.append([check_valid(rectangles[2]),
                               is_square(rectangles[2]),
                               diagonal_len(rectangles[2]),
                               height(rectangles[2]),
                               width(rectangles[2]),
                               area(rectangles[2]),
                               perimeter(rectangles[2])])
            
            if actual_ans == expected_ans:
                print("You passed all the tests!")
            else:
                print("Wrong answer, you failed the tests!")
        except:
            print('Runtime error when testing Rectangle, please check your code!')
    except:
        print('Cannot load Rectangle, please check the class name or syntax.')
else:
    print('Cannot find p5.py, please put p5.py and this test script in the same folder.')
