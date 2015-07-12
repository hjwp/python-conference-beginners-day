# The Python Ecosystem

# The origin story

* Free software and Open Source.  Stallman, GNU, Linux, Torvalds

### Resources and further reading

* "In the Beginning was the Command Line" by Neal Stephenson: http://www.cryptonomicon.com/beginning.html 
* "Hackers" by Steve Levy: http://www.stevenlevy.com/index.php/books/hackers 
* The GNU Philosophy articles: https://www.gnu.org/philosophy/philosophy.html 




# The world around us

* Programming languages: Assembly, compiled, dynamic. Python's relationship to C. Other similar languages - Ruby, JavaScript, Go.  Mention Java, Lisp?

(insert some examples of assembly etc?  hello world in different languages?)


### Resources and further reading:

Paul Graham on the advantages that a good language can bring: http://www.paulgraham.com/avg.html




# Python's journey

* Python -- versions, 2 vs 3.  the standard library
* PEPs




### Resources

* Guido himself on the history and philosopy of Python: https://www.python.org/doc/essays/foreword/



# Actually doing stuff

* Packages.  Pypi.  easy-install, pip.
* Web dev
* Science stuff
* Github



### Some definitions:


#### Packages:

**package**: is the word for a bundle of Python files that you can use as a tool. A "library".  Sometimes called a "module", although that's probably a less precise use of the term.

**PyPI**: the Python Package Index.  Used to be known as the Cheese Shop (because http://www.youtube.com/watch?v=PPN3KTtrnZM).  A public directory of python packages, including links to their source code.  Anything on PyPI can be pip installed.  Anyone can upload a package to Pypi, all you need is to read the docs and create a special installation file called *setup.py*.

**pip**: the standard Python command-line package installer.  "pip install package-name" is the basic command.  There used to be one called `easy_install`, essentially the same, now is less used.  You can also manually download the source code for a package and install it by running the setup.py file, `python setup.py install`.


#### Web dev:

**WSGI** the Web Server Gateway Interface is the standard protocol or API for request/response (traditional HTTP, ie not websockets/webrtc etc) web apps.  Django, Flask etc all use WSGI.  You could write your own web app that complies with the WSGI standard without using any of them, but it would be a little pointless.

**websockets** are an alternative to the traditional request/response protocol for the web.  They let you open a 2-way, "real-time" conduit between your web page and the server, so you can do real-time updates without needing to refresh the browser or use javascript.  Think chat apps, notifications, etc.  lots of websockets in twitter and facebook...

**Django** is probably the most popular framework.  It comes with lots of built-in tools like the "admin", a web ui for admin users to create database entries, a templating language for generating HTML, an "ORM" to make it easy to work with the database, and so on.

**Flask** is a more "lightweight" alternative -- it doesn't include an ORM or a templating language, and its way of dealing with URLs is simpler, and you can use other ORMs (sqlalchemy is popular) and templating languages (jinja2 usually), but after a while, if your project is going to be complex, the third-party tools start to have inter-dependencies that do end up constraining your choices.   Best for smaller projects, microservices etc.

**bottle** is a micro-micro-micro framework.  It's a single file!

**web2py** is super beginner-friendly, but scorned by more experienced programmers, perhaps unfairly.

**Pyramid** is very flexible and based on components you can choose to use or not.  The slightly intimidating, harcore user's choice. Also, they have the coolest t-shirts.

**Tornado** is the first non-wsgi web app framework in our list.  It's often used to do websockets, but it can also do traditional request/response stuff.

**Twisted** is the second, it's been around for ages, it actually does all sorts of network stuff, from serial port connections all the way up to being its own web server. Requires a slightly "twisted" way of thinking about programming (callbacks, "deferred" objects...).



#### Science stuff:

**numpy & scipy** are two of the most popular scientific python libraries.  Numpy has lots of tools for doing maths on big arrays of numbers, and scipy has lots of stats and ananalysis functions.  scipy depends on numpy.  If you're on windows, they may not "pip install" cleanly, so go to the scipy website and download installers, or look into Conda.

**IPyton and the IPython Notebook** - as we saw earlier, Ipython is an enhanced Python interpreter.  The Ipython Notebook is the real darling of the scientific Python world though, it gives you a sort of interactive notebook interface, a bit like matlab I'm told.

**pandas** is popular for dealing with tables of data.  Lets you do excel-style pivottables, for example

**matplotlib** is a well-revered tool for drawing graphs


##### Science Resources:

High Performance Python (book): http://shop.oreilly.com/product/0636920028963.do

Jake Vanderplaas: https://jakevdp.github.io/ 



#### Open source on the web, version control

**Version control system (VCS)** - a system for managing snapshots of your source code.  Popular ones these days are git and mercurial.  In the bad old days you had subversion and CVS.

**Git** - probably the most popular version control system (it was built by Linus and the other kernel developers to manage the Linux source code).  It's also probably the least user-friendly!  
(link to that git-emailing-patches guide?)

**Mercurial (hg)** - is a slightly friendlier version of git, written in Python.  It's used to manage the Python source code.

**GitHub** is the world's most popular code sharing site, and centralised git hosting tool.  You can also put mercurial repos on there.

**Bitbucket** is the plucky underdog to GitHub's thousand-pound gorilla

**GitLab** lets you host your own github

**Patches** are a syntax showing changes to a file.  Also (more or less) called a **diff**.  The `patch` command can apply a patch to a file.  Git is essentially a big complicated system for managing patches


# Original notes.

Intro to Open Source (15 mins) brief lecture on Free Software, Linux, Open Source, Github, sprints, etc

Intro to Python (5 mins) what can you do with Python, a bit of history, etc.

The Python ecosystem (15 mins): what is pip, pypi, 3 vs 2, standard library, ...

Overview of the Python Web Development landscape (15 mins):  django, flask, web2py etc, but also AWS, Heroku, PythonAnywhere, HTML, javascript...

Overview of the Scientific Python landscape (15 mins) numpy, scipy, ipython notebook, pandas, scipy conferences etc

“Getting the best out of the conference” session (30 mins) -- suggested talks, don’t be afraid to ask stupid questions, what is an open space, what is a birds-of-a-feather session, etc



