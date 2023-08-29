from pymonad.tools import curry

@curry(2)
def strcat(x,y):
	return x+y

hello_smth = strcat('Hello, ')

def make_hello_msg(greeting_word, punctation_mark, greeted_name, closing_mark):
    return greeting_word + punctation_mark + ' ' + greeted_name + closing_mark      

@curry(4)
def first_step(greeting_word, punctation_mark, closing_mark, greeted_name):
    return make_hello_msg(greeting_word, punctation_mark, greeted_name, closing_mark)
    
final = first_step("Hello")(",")("!")

