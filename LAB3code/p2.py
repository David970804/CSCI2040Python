def quicksort(a):
	if len(a) <=1:
		return a
	else:
		pivot=a[len(a)//2]
		small=[x for x in a if x < pivot]
		big=[x for x in a if x > pivot]
		middle=[x for x in a if x==pivot]
		return quicksort(small)+list(middle)+quicksort(big)


