"""
Imagine you wanted to reimplement "head" and "grep" in python.  Here's a first cut:
"""

def head(max_lines, filenames):
    for fn in filenames:
        with open(fn) as f:
            for ix, line in f:
                if ix >= max_lines:
                    return
                print(line, end='')


def grep(needle, filenames):
    for fn in filenames:
        with open(fn) as f:
            for line in f:
                if needle in line:
                    print(line, end='')

"""
There's a lot of duplicated code there!  Now we could build a helper function like this:
"""

def getlines(filenames):
    for fn in filenames:
        with open(fn) as f:
            return f.readlines()

"""
but then head would be inefficient, because getlines always reads every single line in the file.

Find out how to use a generator to make a version of getlines that is "lazy"

More info here: http://anandology.com/python-practice-book/iterators.html
"""

