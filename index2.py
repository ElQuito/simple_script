# находим медиану массива

list_test = [2,6,54,3,6,7,1,2,4,0,4,6,3,9,3,2,1,6,8,11,3,7,22,34]

def average_test(list_a):
	list_a.sort()
	leng = len(list_a)
	if leng % 2 == 0:
		median = (list_a[leng//2 - 1] + list_a[leng//2])/2
	else:
		median = list_a[leng//2]
	return median


print(average_test(list_test))
