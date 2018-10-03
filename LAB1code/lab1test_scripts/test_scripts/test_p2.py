import pexpect

ok = 0

child = pexpect.spawn('python p2.py')

child.sendline('4')
child.readline()

child.sendline('1')
child.readline()

flag = True
for i in [1,2,3,4]:
	line = child.readline().rstrip()
	print (line)
	if not (line == '1'*i or line.decode() == 'a'*i):
		flag = False
if (flag == True):
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')


child.sendline('2')
child.readline()

child.sendline('^_^')
child.readline()

flag = True
for i in [1,2]:
	line = child.readline().rstrip()
	print (line)
	if not (line == '^_^'*i or line.decode() == '^_^'*i):
		flag = False
if (flag == True):
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')


child.sendline('-1')
child.readline()
test3 = child.readline().rstrip()
print(test3)
if (test3 == 'Program ends.' or test3.decode() == 'Program ends.'):
	print ('TEST 3 OK!')
	ok += 1
else:
	print ('TEST 3 FAIL.')


if ok == 3:
	print ('You pass all the tests!')
