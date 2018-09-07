import pexpect

ok = 0

child = pexpect.spawn('python p4.py')

child.sendline('9')
test1 = child.readline().rstrip()
cmp_str = 'Player 1, write down your number secretly:'
if (test1 == cmp_str or test1.decode() == cmp_str):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

child.sendline('0')
child.readline()
test2 = child.readline().rstrip()
cmp_str = 'Your guess is too low!'
if (test2 == cmp_str or test2.decode() == cmp_str):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')


child.sendline('100')
child.readline()
test3 = child.readline().rstrip()
cmp_str = 'Your guess is too high!'
if (test3 == cmp_str or test3.decode() == cmp_str):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')

child.sendline('12')
child.readline()
child.readline()

child.sendline('9')
child.readline()
test4 = child.readline().rstrip()
cmp_str = 'You are right after trying for 4 times. Program ends.'
if (test4 == cmp_str or test4.decode() == cmp_str):
	print ('TEST 4 OK!')
	ok += 1
else:
	print ('TEST 4 FAIL.')
############################ TEST 5 will test the guess-fail case ###################
child = pexpect.spawn('python p4.py')
child.sendline('5')
child.readline()
child.sendline('6')
child.readline()
child.readline()
child.sendline('4')
child.readline()
child.readline()
child.sendline('-1')
child.readline()
child.readline()
child.sendline('-50')
child.readline()
child.readline()
child.sendline('100')
child.readline()
child.readline()
child.sendline('-100')
child.readline()
test5 = child.readline().rstrip()
cmp_str = 'You have tried 6 times and it is still wrong! The answer is 5 and program ends.'
if (test5 == cmp_str or test5.decode() == cmp_str):
    print ('TEST 5 OK!')
    ok += 1
else:
    print ('TEST 5 FAIL.')

if ok == 5:
	print ('You pass all the tests!')
