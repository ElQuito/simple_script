# соритровка пузырьком

list = [4,8,7,5,34,2,1,8,9,7,0,46,67,43,32,87,9,76,4,3,2,145,678,64,90,54,87,23,44,55,22,33,68,29,19,27,74,92]


leng = len(list)
swapped = 'true'
while swapped != 'false':
	i = 1
	swapped = 'false'
	while i < leng:
		if list[i - 1] > list[i]:
			list[i - 1], list[i] = list[i], list[i - 1]
			swapped = 'true'
		i+=1
			
print(list)