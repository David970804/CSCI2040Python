import pexpect

ok = 0

child = pexpect.spawn('python p3.py')

child.sendline('3.7 3')
child.readline()
test1 = child.readline()
current_gpa = float(test1.split()[2])
if current_gpa == 3.7:
	print ('TEST 1 OK!')
	ok += 1
else:
	print ('TEST 1 FAIL.')

child.sendline('3.3 2')
child.readline()
test2 = child.readline()
current_gpa = float(test2.split()[2])
if current_gpa == 3.54:
	print ('TEST 2 OK!')
	ok += 1
else:
	print ('TEST 2 FAIL.')
child.sendline('-2.5 2')
child.readline()
test3 = child.readline().rstrip()
if(test3 == 'Wrong input!' or test3.decode() == 'Wrong input!'):
    print ('TEST 3 OK!')
    ok += 1
else:
    print ('TEST 3 FAIL.')
child.sendline('-1')
child.readline()
test4 = child.readline().rstrip()
if (test4 == 'Program ends.' or test4.decode() == 'Program ends.'):
	print ('TEST 4 OK!')
	ok += 1
else:
	print ('TEST 4 FAIL.')


if ok == 4:
	print ('You pass all the tests!')
