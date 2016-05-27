'''
Challenge: context managers

Let's take our decorators challenge from earlier, and say
we want to implement a lock.  Say we're running lots
of my_programs in parallel, and you want to restrict
some functions to only being called once at a time.

Let's say we use a tempfile to hold the lock:
'''

def hold_lock():
    filename = tempfile.NamedTemporaryFile(delete=False).name
    with open(filename, 'w') as f:
        f.write('locked')
    return filename


def release_lock(lock_name):
    os.remove(lock_name)

'''
Incidentally, you've seen in the Python docs that you're meant
to use "with open" -- that's actually already a context manager.
Building our own might take away some of the air of mystery from it...

So we want to run "hold_lock" before each function starts, and
"release_lock" at the end.

So you could use a decorator, but what if the function
raises an exception?  now you have to have a try/except
and it gets yucky...

You might want to try this to get a feel for the ugliness.

But a context manager would be much nicer!

Find out how to write a context manager that calls hold_lock
before a function runs, and calls release_lock at the end,
even if the function raises an exception.

For bonus points:  make it so that the user can also write
to the lock file, for debugging purposes, when they're
"inside" the context manager...
'''



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
        if datetime.now().microsecond % 42 == 0:
            raise Exception('all your base!')
        print('Go {}! '.format(i), end='')

