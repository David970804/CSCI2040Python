import subprocess

def check_ans(case_no, code_ans, expect_ans, score):
        global FLAGS_final_score
        if code_ans == expect_ans or code_ans.decode() == expect_ans:
                print('You passed the test case ' + str(case_no) + ' :)')
                FLAGS_final_score += score
        else:
                print('You failed in the test case ' + str(case_no) + ' :(')
                print('The expected answer is: ' + expect_ans)
                print('But your answer is:', code_ans)

FLAGS_final_score = 0
cmd = 'python only_call_by_test_p4.py'
code_ans_list = subprocess.check_output(cmd, shell=True)
code_ans_list = code_ans_list.splitlines()

expect_ans_list = ['list length 0',
 'Current linked list: 20-->15-->10-->20-->none',
 'True',
 'False',
 'list length 5',
 'Current linked list: 20-->10-->15-->20-->30-->none',
 'Current linked list: 10-->15-->20-->30-->none']

score_list = [2.5, 2.5, 2.5, 2.5, 5, 6, 4]

for i in range(7):
        case_no = i+1
        code_ans = code_ans_list[i]
        expect_ans = expect_ans_list[i]
        score = score_list[i]
        check_ans(case_no, code_ans, expect_ans, score)
        
print('You score is: ' + str(FLAGS_final_score) + ' out of 25')
print('More details about those test cases can be found in only_call_by_test_p4.py')
