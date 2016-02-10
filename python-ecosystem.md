Find these notes at:

https://github.com/hjwp/
    python-conference-beginners-day/

    python-ecosystem.md


Email me at: obeythetestinggoat@gmail.com



# The Python Ecosystem

This document starts with bullet point notes for presenters, and then at the end has further reading + notes for students


# The origin story

> Python is free software. What does that mean?

* Free software and Open Source.  MIT hackers, the Mac and PC revolution, Stallman, GNU, Linux, Torvalds



# The world around us

> What are programming languages like and what makes Python special?

* Programming languages: Assembly, compiled, dynamic. Python's relationship to C. Other similar languages - Ruby, JavaScript, Go.  Mention Java, Lisp?

(insert some examples of assembly etc?  hello world in different languages?)

































# Python's journey

> Who is this Guido person anyway?

* Python -- ramping up to version 2
* the standard library
* Adoption by Google, NASA...
* Python 3
* PEPs
* Pypy
* Adoption in education
* The future of Python: asyncio, pypy, type hinting...


































# Actually doing stuff with Python (packages!  libraries!)

> OK, we know what Python is, now how do we get stuff done?

* Packages.  Pypi (not to be confused with pypy).  easy-install, pip.
* Web dev
* Science stuff
* Desktop stuff + mobile, Kivy
































# Actually writing code  (Git! Agile! etc)

> You don't have to learn these yet-immediately-right-now necessarily, but you
> will want to learn them soon, and you'll want to at least know vaguely what
> they are...

* Version control.  Why it's better than backups.  Git vs Mercurial vs the bad old days of subversion etc
* Open source projects, contributing, Github, sprints
* Testing, Agile development, Lean

































# The Python Community

* The justin django-migrations story
* DjangoGirls


































# Resources and Further reading

History and Free software:
* "In the Beginning was the Command Line" by Neal Stephenson: http://www.cryptonomicon.com/beginning.html 
* "Hackers" by Steve Levy: http://www.stevenlevy.com/index.php/books/hackers 
* The GNU Philosophy articles: https://www.gnu.org/philosophy/philosophy.html 
* The Cathedral and the Bazaar: http://www.catb.org/esr/writings/cathedral-bazaar/ 

Programming languages and Python:
* Paul Graham on the advantages that a good language can bring: http://www.paulgraham.com/avg.html
* Guido himself on the history and philosopy of Python: https://www.python.org/doc/essays/foreword/
* The Python docs: https://docs.python.org/

Science stuff:
* High Performance Python (book): http://shop.oreilly.com/product/0636920028963.do
* Jake Vanderplaas: https://jakevdp.github.io/ 

Web Dev
* the DjangoGirls tutorial - an excellent guide for total beginners, from "how the internet works" up to getting a blog site live on the Internet. http://tutorial.djangogirls.org/ 
* http://www.obeythetestinggoat.com -- a good guide for after you've written your first proper Python project.  TDD, Git, deployments. Focused on web development.  More disclosure:  this was written by the first author of this doc.

Git et al
* "Just enough Git to be (less) Dangerous" - http://eev.ee/blog/2015/04/24/just-enough-git-to-be-less-dangerous/


# Some definitions and notes to read in your own time (handout)

## Python

**Monty Python** an English sketch show from the 70s, famous for its absurdist sketches, which Guido named his programming language after.  Google for: "The Cheese Shop", "Dead Parrot", "Bicycle Repair Man", "The Philosophers' Drinking Song", "The Philosophers football", "The Life of Brian", amongst so many others.  The whole snake thing is wrong really, but it's cute, so we like it...

**Python 2 vs Python 3** it's been a slow process, but it's just starting to feel like Python 2 really is the legacy version.

**Guido van Rossum (the BDFL)** Guido is Python's inventor, and today we call him the BDFL - Benevolent Dictator For Life

**PEP** A Python Enhancement Proposal, a public discussion document describing a proposed improvement to Python

**dunder** short for "double-underscore", so you might pronounce `__init__` as "dunder-init".  You don't have to say this if you don't want to though ;)

**duck typing** - some programming languages are strict about objects belonging to particular types, and what types are allowed as arguments to functions, and so on.  Python prefers a "duck typing" approach ("if it walks like a duck, and sounds like a duck, then it is a duck") whereby any object that implements the right methods can "pretend" to be of the right type, so it can be used by a function...

**the REPL** - another word for the interactive interpreter.  It stands for Read-Evaluate-Print-Loop, which is what interpeters do...

**the GIL**  - the "Global Interpreter Lock", an unfortunate feature of the cPython interpreter that means only one thread can do work at any given time -- which is why Python isn't usually very good at multithreading (this is a subtle topic, and things like PyPy are making changes here".

**type hinting** a terrible idea.


## Packages:

**package**: is the word for a bundle of Python files that you can use as a tool. A "library".  Sometimes called a "module", although that's probably a less precise use of the term.

**PyPI**: the Python Package Index.  Used to be known as the Cheese Shop (because http://www.youtube.com/watch?v=PPN3KTtrnZM).  A public directory of python packages, including links to their source code.  Anything on PyPI can be pip installed.  Anyone can upload a package to Pypi, all you need is to read the docs and create a special installation file called *setup.py*.  (not to be confused 

**pip**: the standard Python command-line package installer.  "pip install package-name" is the basic command.  There used to be one called `easy_install`, essentially the same, now is less used.  You can also manually download the source code for a package and install it by running the setup.py file, `python setup.py install`.

**vitural environments** or [virtualenvs](http://docs.python-guide.org/en/latest/dev/virtualenvs/) constitute a very useful python tool to keeps dependencies in separate places and avoid conflicts. Packages can be installed globally or inside a virtualenv.


## Web dev:

**HTML** Hypertext Markup Language is the code for web pages.  What you see when you click "view source" in your browser.  You know, `<html></html>` and all that stuff.

**JavaScript** a hideous car crash of a language that everyone looks down on, partially for good reasons, and partially because they're jealous that it's so popular, because it's the only language you can use in a browser.  It's not that bad, really.

**REST** "Representational State Transfer" is a standard for structuring URLs and how to do HTTP requests for data structures over the Internet.  Used for APIs.  A common pattern these days is to have a basic HTML site which does most of its interaction with your database via javascript and a REST API, instead of doing "normal" browser form interactions...

**WSGI** the Web Server Gateway Interface is the standard protocol or API for request/response (traditional HTTP, ie not websockets/webrtc etc) web apps.  Django, Flask etc all use WSGI.  You could write your own web app that complies with the WSGI standard without using any of them, but it would be a little pointless.

**websockets** are an alternative to the traditional request/response protocol for the web.  They let you open a 2-way, "real-time" conduit between your web page and the server, so you can do real-time updates without needing to refresh the browser or use javascript.  Think chat apps, notifications, etc.  lots of websockets in twitter and facebook...

**Django** is probably the most popular framework.  It comes with lots of built-in tools like the "admin", a web ui for admin users to create database entries, a templating language for generating HTML, an "ORM" to make it easy to work with the database, and so on.

**Flask** is a more "lightweight" alternative -- it doesn't include an ORM or a templating language, and its way of dealing with URLs is simpler, and you can use other ORMs (sqlalchemy is popular) and templating languages (jinja2 usually), but after a while, if your project is going to be complex, the third-party tools start to have inter-dependencies that do end up constraining your choices.   Best for smaller projects, microservices etc.

**bottle** is a micro-micro-micro framework.  It's a single file!

**web2py** is super beginner-friendly, but scorned by more experienced programmers, perhaps unfairly.

**Pyramid** is very flexible and based on components you can choose to use or not.  The slightly intimidating, harcore user's choice. Also, they have the coolest t-shirts.

**Tornado** is the first non-wsgi web app framework in our list.  It's often used to do websockets, but it can also do traditional request/response stuff.

**Twisted** is the second, it's been around for ages, it actually does all sorts of network stuff, from serial port connections all the way up to being its own web server. Requires a slightly "twisted" way of thinking about programming (callbacks, "deferred" objects...).

**Virtual Machine providers** - people who will host virtual servers for you. **Amazon Web Services (AWS)** is the biggest; Amazon rents out virtual machines and server services -- VMs, but also storage (S3), load balancing, databases...  They have lots of competitors, like **Rackspace**, **Linode**, **Digital Ocean** and more (with varying level of capabilities)

**PaaS (Platform-as-a-Service) providers** - people who want to rent you a service rather than a virtual machine.  Usually you trade off convenience (eg, not having to worry about sysadmin, OS updates, load balancing) against flexibility (you may not be able to do everything you could do on your own server).  The biggest is **Heroku**, see also **PythonAnywhere** for a Python-focused one [1]

* [1] disclosure: original author works for PythonAnywhere.

**Docker** is the trendy technology of the month.  It's a lightweight alternatives to a VM - instead of one physical server running lots of virtual servers, you have one physical or virtual server running lots of "containers", which are little sandboxes that pretend to the process that runs inside them that they are all alone on a server, when in fact they are not.  You can start a VM in 20-60s, but you can start a container in less than a second.



## (Data) Science stuff:

**numpy & scipy** are two of the most popular scientific python libraries.  Numpy has lots of tools for doing maths on big arrays of numbers, and scipy has lots of stats and analysis functions.  scipy depends on numpy.  If you're on windows, they may not "pip install" cleanly, so go to the scipy website and download installers, or look into Conda.

**IPyton and the IPython Notebook** (now [Jupyter project](http://jupyter.org/)) is an HTML notebook environment based on iPython shell. As we saw earlier, Ipython is an enhanced Python interpreter. The Ipython Notebook allows to combine code execution, text and plots and has become the go-to coding environment for the scientific Python world.

**pandas** is popular data analysis library that reproduces a lot of functionalities found in R and contains plotting functionalities. It is used a lot for dealing with tables of data (CSV, Excel) but also handles other formats like text files, HTML, json, SQL...

**scikit-learn** is machine learning library built on top of SciPy/Numpy. It integrates a wide range of classification, clustering and regression algorithms.

**nltk** is a natural language processing library. It provides tools for the classification, tokenization, stemming, tagging, parsing... of human language data.

**matplotlib** is a well-revered plotting library for Python.

**seaborn** is a data visualisation library based on matplotlib (but much nicer visually).

**bokeh** is an interactive data visualisation tool in the browser (like D3.js).



## Open source, version control

**Version control system (VCS)** - a system for managing snapshots of your source code.  Popular ones these days are git and mercurial.  In the bad old days you had subversion and CVS.

**Git** - probably the most popular version control system (it was built by Linus and the other kernel developers to manage the Linux source code).  It's also probably the least user-friendly!  
(link to that git-emailing-patches guide?)

**Mercurial (hg)** - is a slightly friendlier version of git, written in Python.  It's used to manage the Python source code.

**GitHub** is the world's most popular code sharing site, and centralised git hosting tool.  You can also put mercurial repos on there.  There used to be **Google code**, but that's been retired, and there's sourceforge, which almost everyone has downloaded something off at some point.  GitHub is like sourceforge but more focused on nerds, and with less random adware all over everything.

**Bitbucket** is the plucky underdog to GitHub's thousand-pound gorilla

**GitLab** lets you host your own github

**Maintainer** is a person who decides what commits to accept into an open source project.  They may not do the bulk of the work, or be a single person...

**Patches** are a syntax showing changes to a file.  Also (more or less) called a **diff**.  The `patch` command can apply a patch to a file.  Git is essentially a big complicated system for managing patches.

**Fork**  refers to the idea of taking a copy of an open source project, and maybe taking it off in a new direction -- either permanently (MariaDB is a fork of the Oracle version of MySQL, LibreOffice is a fork of OpenOffice), or maybe just in the very short term, while a developer tries out a new idea, before submitting patches to merge back into the main project

**Pull Request** is Github's way of managing contributions from random developers to open source projects.  Developer forks the main repo, makes a few commits, then does a "pull request" to ask the owner of the main repo to merge her changes.

**Sprints** are focused periods of contributions to an open-source project, usually where people get together physically in a single room, and new contributors can get advice directly in person from the maintainer(s).  There are usually sprints at the end of a conference!  They're usually very welcoming to beginners...


## Development methodologies

**Agile software development**  Traditionally, software was developed in the "waterfall" model: requirements gathering first, then design, then build, then test.  In the 90s, people started to try a different mode, with much shorter development cycles (weeks rather than months), aiming to get new features out in front of users as fast as possible, in smaller chunks.  **Extreme Programming (XP)** was the first, and **Scrum** is now quite popular with corporations.  **Kanban** has something to do with this too.

**Lean Startup** is a counterpart to the agile model, where rather than taking months or years to build a fully-featured product and then trying to sell it to consumers, you instead try to build a **Minimum Viable Product**, the simplest, smallest thing that could possibly be useful, show it to users asap, and then iterate on it

**Automated Testing** is a practice that grew out of XP, which is the idea that you can have automated tests for your software.  **unit tests** are small tests for individual little bits of your code, although you can also write end-to-end tests for the whole programming.  **TDD** (Test-Driven-Development) is the crazy idea that you can actually write tests *before* you write the actual code...

