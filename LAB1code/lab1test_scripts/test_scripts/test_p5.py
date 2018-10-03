import pexpect

ok = 0

child = pexpect.spawn('python p5.py')

child.sendline('210')
child.readline()

child.sendline('012')
test1 = child.readline().rstrip()
cmp_str = 'No, you must input a palindrome: 012'
if (test1 == cmp_str or test1.decode() == cmp_str):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')


child.sendline('NbaABn')
test2 = child.readline().rstrip()
cmp_str = 'No, you must input a palindrome: NbaABn'
if (test2 == cmp_str or test2.decode() == cmp_str):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

test3 = child.readline().rstrip()
cmp_str = 'Welcome to the wonderland!'
if (test3 == cmp_str or test3.decode() == cmp_str):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')

if ok == 3:
	print ('You pass all the tests!')
