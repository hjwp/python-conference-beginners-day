# Welcome

* What are we going to do today?

* Intros of each coach

* Intros of each participant

* Run-through of each tutorial option
    - beginners + DG
    - Dive into Python (http://www.diveinto.org/python3/) aka DiP
    - challenges


* Split out into tables
    - beginners (incl DiP)
    - intermediates
    - aim to have at least one coach per table


# Some tips:

* terminal stuff demos
    - up arrow
    - tab-completion
    - ctrl+r
(Use Git-Bash on Windows)

* Python console:
    - use IPython!
    - same bits re tab-completion etc


## Installing Python (and pip)


* On Windows, just download the Python 3 installer from python.org.  Make sure you tick the option that says **add python.exe to Path**

* On Mac, again, download the Python 3 installer from python.org

* On Linux, use your package manager.  On Ubuntu, if you don't have pip, use 

    apt-get install python3-pip


## Install Git-Bash (for Windows)

Although Python does have excellent Windows support, there's a lot of stuff out there on the web that tends to assume you're on Linux or a Mac.  Git-Bash gives you a command-line that's more Unixey, so more likely to be similar to what online tutorials assume you have.

Download and install Git from https://git-scm.com/download/win
Make sure you choose **Run Git and included Unix tools from the Windows command prompt**. 
Then use "Git Bash" for all your command-line stuff.  You can now use ls, grep, and all that sort of unixey goodness!

* Copy + paste:
    - The first time you open it, right click its title bar, edit the defaults, and set "edit mode" to be the default.  That'll let you use the mouse to do copy and paste.  When you have a selection, hit enter for it to be copied
    - Use Alt-Space, E, P for paste (sigh)


## Terminal shortcut tips

A few things I wish someone had told me much earlier on in my unixey adventures!

**Up arrow** in a terminal, lets you re-run the previous command.  Up, then press enter.  Or you can modify it.  UP again goes further back in time, and down if you overshoot.

**Tab completion** press tab once to see if the terminal can autocomplete the current command, whether it's an executable, or the path to a file, or even (sometimes) the arguments to a program.  Press tab twice to see a list of options

**Ctrl+R** enters history-search mode.  Type part of a previous command to try and find it and re-run it.

**Ctrl+D** is a shortcut to exit a program (actually, it sends the "end of file, EOF" character).  It can exit Python, but it can also exit your main command-line terminal, so careful!  If you're on windows and it doesn't work, try Ctrl+Z.

**Ctrl+C** interrupts stuff, in Python or Bash.  Good for stopping sprawling screens of text!


## Installing IPython

IPython is an alternative to the regular Python command-line interpreter.  It gives you much better tab-completion and a slighty better way of dealing with history and indentation.  You can install it with 

    pip install ipython
    # or, on mac/linux
    sudo pip3 install ipython

Try the %paste command instead of the normal Ctrl+V for pasting mutli-line stuff into Ipython.

IPython is very popular, particularly with the science crowd, but if you fancy being a bit different, try **bpython** instead.


