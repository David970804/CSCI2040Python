import sys
import os
import subprocess

def check_ans(case_no, cmd, expect_ans, score):
        global FLAGS_final_score
        code_ans = subprocess.check_output(cmd, shell=True)
        first_line = code_ans.splitlines()[0]
        if first_line == expect_ans or first_line.decode() == expect_ans:
                print('You passed the test case ' + str(case_no) + ' :)')
                FLAGS_final_score += score
        else:
                print('You failed in the test case ' + str(case_no) + ' :(')
                print('The expected answer is: ' + expect_ans)
                print('But your answer is:', code_ans)
                

cmd_list = ['python p2.py her or test1.txt',
            'python p2.py her orbs test1.txt',
            'python p2.py HER ORBS test1.txt',
            'python p2.py her or',
            'python p2.py text1.txt',
            'python p2.py her text222.txt']
expect_ans_list = ['No match!',
                   'To dew her orbs upon the green',
                   'To dew her orbs upon the green',
                   'Not enough arguments!',
                   'Not enough arguments!',
                   'File does not exist!']
score_list = [6, 8, 10, 2, 2, 2]

FLAGS_final_score = 0
for i in range(6):
        case_no = i+1
        cmd = cmd_list[i]
        expect_ans = expect_ans_list[i]
        score = score_list[i]
        check_ans(case_no, cmd, expect_ans, score)
        
print('You score is: ' + str(FLAGS_final_score) + ' out of 30')
