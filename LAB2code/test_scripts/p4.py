def divisible_sublist(list1,d1,d2):
	return [x for x in list1 if x % d1 ==0 or x % d2 == 0]
