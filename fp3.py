from pymonad.tools import curry
from pymonad.maybe import Just,Nothing

@curry(2)
def add(x, y):
    return x+y

def add10(x):
	return  Maybe.apply(add).to_arguments(Just(10), x)
	
