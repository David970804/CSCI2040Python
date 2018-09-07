import pexpect

ok = 0

child = pexpect.spawn('python p1.py')

child.sendline('10.15')
child.readline()

child.sendline('33.2')
child.readline()

child.sendline('abc')
child.readline()
test1 = child.readline().rstrip()
if (test1 == 'Your input is not a number!' or test1.decode() == 'Your input is not a number!'):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

child.sendline('13.1')
child.readline()

child.sendline('-2.01')
child.readline()
test2 = child.readline()
smallest = float(test2.split()[5])

if (smallest == 10.15):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')

if ok == 2:
	print ('You pass all the tests!')
