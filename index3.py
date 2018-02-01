# разница диагоналей матрицы по модулю

#1,2,3
#4,5,6
#7,8,9

#1 ,2 ,3 ,4
#5 ,6 ,7 ,8
#9 ,10,11,12
#13,14,15,16
import math


list_matrix = [1,2,3,4,5,6,7,8,9]
list_matrix1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
list_matrix2 = [1,2,3,4,7,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

def matrix(list_a):
	leng = len(list_a)
	sqr = math.sqrt(leng)
	diagonal1 = 0
	diagonal2 = 0
	i = 0
	while i < (leng + 1):
		diagonal1 = diagonal1 + list_a[int(i)]
		i = i + sqr + 1
		
	i2 = sqr - 1
	while i2 < (leng - 1):
		diagonal2 = diagonal2 + list_a[int(i2)]
		i2 = i2 + sqr - 1
		
	return math.fabs(diagonal1 - diagonal2) 
		



print(matrix(list_matrix2))
