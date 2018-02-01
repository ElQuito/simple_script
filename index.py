# выводим топ N пользователей по продажам по городам  

import json
with open('dictonaty.json', encoding="utf8") as f:
	test = f.read()	
content = json.loads(test)
temp_t2 = ''
for row0 in content['country']:	
	if row0['city'] == temp_t2: continue	
	temp_t2 = row0['city']	
	temp_t = ''
	dictonary = {}	
	for row1 in content['country']:		
		if row1['user_id'] == temp_t: continue
		temp_t = row1['user_id']
		i = 0		
		for row2 in content['country']:
			if temp_t == row2['user_id'] and temp_t2 == row2['city']:			
				i+=1					
		dictonary[temp_t] = i				
	genexp = ((k, dictonary[k]) for k in sorted(dictonary, key=dictonary.get, reverse=True))	
	i2 = 0	
	for k, v in genexp:	
		i2+=1		
		if i2 > 2:		
			break		
		if v != 0:		
			print(temp_t2, k, v)