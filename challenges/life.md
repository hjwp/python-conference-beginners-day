# Conway's Game of Life Challenge

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

# Rules

> Any live cell with fewer than two live neighbours dies, as if caused by under-population.
> Any live cell with two or three live neighbours lives on to the next generation.
> Any live cell with more than three live neighbours dies, as if by overcrowding.
> Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


# Hints: (spoilers?)

* Start by thinking of a way to represent the state of the world, or grid.  What kind of data structure will be simple and easy to work with?

* Next, make a way to print out the board, so you can see it

* Then think about how to do a "step", a transition from one moment in time to another.  You'll need to look at each cell, figure out where the neighbouring cells are, whether they're live or dead, and decide one whether it will be alive or dead in the new board.


# Challenges

The first challenge is obviously to get it working.  But then:

* If you used a class-based, Object-Oriented approach, try again with a pure-functional approach, with simple data structures
* Or, vice versa!
* If you're printing out board states to the terminal, are you starting with a random board state?  or a fixed one?
* How about using a gui instead?  Look into Tk or Pygame?  
* Or even a web app?



