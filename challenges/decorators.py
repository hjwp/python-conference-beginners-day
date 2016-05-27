"""
Challenge: use decorators to trace time taken for function calls

Check out my_program, which relies on 3 different functions.  But
which one takes the most time?

We could add a start_time = time.time() to the beginning of each one,
and a print(time.time() - start_time) at the end, but that would be
very repetitive.  Figure out how to use a decorator to apply this
print pattern to all the functions, without duplicating code.

For bonus points: the little time printout should include the name
of the function

"""

from datetime import datetime

def my_program():
    main_screen_turn_on()
    if somebody_set_us_up_the_bomb():
        take_off_every_zig()

def main_screen_turn_on():
    print('\n'.join(['*' * 80] * 25))



def somebody_set_us_up_the_bomb():
    if datetime.now().microsecond % 7 == 0:
        return True
    return False


def take_off_every_zig():
    for i in range(1, 10001):
        print('Go {}! '.format(i), end='')


"""
For bonus bonus points:

- now make a new decorator that will retry a function up to n times, until
it gets a certain value:

    @repeat(times=5, until_value=True)
    def somebody_set_us_up_the_bomb():
    ...
"""

