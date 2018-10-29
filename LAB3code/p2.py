def quicksort(a):
	if len(a) <=1:
		return a
	else:
		pivot=a[len(a)//2]
		small=quicksort([x for x in a if x < pivot])
		big=quicksort([x for x in a if x > pivot])
		middle=[x for x in a if x==pivot]
		return small+list(middle)+big


