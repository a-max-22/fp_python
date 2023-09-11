from pymonad.tools import curry
from pymonad.state import State

user_init = {'items': [], 'money': 2000}

items = {'apples': 70,
         'wine': 300,
         'milk': 80,
         'chips': 100
         }
    
user_state = State.insert(user_init['items'])


@curry(2)
def buy(item_key, user_items):
    def count_computation(money_remained):
        return user_items + [item_key], money_remained - items[item_key]
    return State(count_computation)

finale = user_state.then(buy('wine')).then(buy('apples')).then(buy('chips')).then(buy('chips')).then(buy('milk'))

finale.run(user_init['money'])
