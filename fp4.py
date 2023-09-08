from pymonad.list import  ListMonad
from pymonad.maybe import Nothing, Just
from pymonad.state import State
from pymonad.tools import curry


@curry(2)
def to_left(num, x):
    return ListMonad((x[0] + num, x[1]))

@curry(2)
def to_right(num, x):
    return ListMonad((x[0] + num, x[1]))


to_left  = lambda num, x: ListMonad((x[0] + num, x[1]))
to_right  = lambda num, x: ListMonad((x[0] , x[1] + num))
banana = lambda x: ListMonad((0, 0 + 5))

if_valid = lambda x: ListMonad((x[0], x[1])) if abs(x[0] - x[1]) < 4 else None

@curry(2)
def step(action, state):
    print(state, action)
    result = ListMonad(state).bind(action).bind(if_valid)
    return result if result is not None else Nothing 


