import functools

def second_max(first_max, second_max, item):
	return item if item > second_max and item < first_max else second_max
	

def find_second_max(list):
	if len(list) < 2: 
		return None 
	first_max = functools.reduce(lambda max,item : max if item <= max else item, list, list[0])
	return functools.reduce(lambda x, y: second_max(first_max, x,y), list, list[0])
	
