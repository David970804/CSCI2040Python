import sys
import os
import platform
import subprocess

def check_ans(case_no, cmd, expect_ans, score, FLAGS_check_output):
        global FLAGS_final_score
        code_ans = subprocess.check_output(cmd, shell=True)
        if FLAGS_check_output:
            try:
                file_content = open('p3_output.txt')
                code_ans = file_content.readlines()
            except:
                print('Cannot open your output file. :(')
                return 
        else:
            code_ans = [code_ans.splitlines()[0].decode()]
            
        if code_ans == expect_ans or code_ans == expect_ans:
            print('You passed the test case ' + str(case_no) + ' :)')
            FLAGS_final_score += score
        else:
            print('You failed in the test case ' + str(case_no) + ' :(')
            print('The expected answer is: ')
            for line in expect_ans:
                print(line)
            print('But your answer is: ')
            for line in code_ans:
                print(line)     
            
                        
if platform.system()=='Windows':                           
        cmd_list = ['python p3.py do.txt p3_output.txt',
                    'python p3.py doc*.txt p3_output.txt',
                    'python p3.py do?.txt p3_output.txt',
                    'python p3.py document.txt p3_output.txt']
else:
        cmd_list = ['python p3.py "do.txt" p3_output.txt',
                    'python p3.py "doc*.txt" p3_output.txt',
                    'python p3.py "do?.txt" p3_output.txt',
                    'python p3.py "document.txt" p3_output.txt']  
expect_ans_list =[
    ['Number of characters: 961.\n', 'Number of words: 211.\n', 'Number of lines: 28.\n'],
    ['Name of file: doc.txt.\n', 'Number of characters: 378.\n', 'Number of words: 98.\n', 'Number of lines: 20.\n'],
    ['Name of file: do.txt.\n', 'Number of characters: 961.\n', 'Number of words: 211.\n', 'Number of lines: 28.\n',
     'Name of file: doc.txt.\n', 'Number of characters: 378.\n', 'Number of words: 98.\n', 'Number of lines: 20.\n'],
    ['Opening file document.txt failed!']]
score_list = [4, 8, 8, 5]

FLAGS_final_score = 0
for i in range(4):
    case_no = i+1
    cmd = cmd_list[i]
    expect_ans = expect_ans_list[i]
    score = score_list[i]
    check_ans(case_no, cmd, expect_ans, score, i!=3)
        
print('You score is: ' + str(FLAGS_final_score) + ' out of 25')
