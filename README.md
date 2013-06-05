KeePassPQ
=========

Experimental port of KeePass 2.x using Python and Qt (PyQt)


About
=====

"Its crazy but it just might work"

There are people who will argue that this is not a good idea. They are probably
right.

So, here's the deal. KeePass 2.x is technically cross platform - at least on the
desktop (Windows/Linux/Mac). The problem is that KeePass is written using the
System.Windows.Forms library. Mono (used on Linux and Mac) has very poor support
for this library (very buggy and no one is fixing it). So, on Windows, KeePass
is top notch, but leaves Linux and Mac users wanting something better.

One possible solution would be to rewrite KeePass using a user interface library
that has good cross platform support. For me, this would be Qt. It has the
ability to look "native" on Windows/Linux/Mac without any special coding. And
more importantly, it seems to be well supported and is open source.

OK. Now we have a graphical tool kit, but there is a problem. Qt is written in
C++ and KeePass 2.x is written in C#, so we need to find some bridge between the
two languages. There have been a couple attempts at writing C# bindings for Qt.
The most recent is Qyoto. It creates C declarations for all of the C++ functions
using a tool called Smoke Generator and then creates C# code that P/Invokes the
auto-generated C code which in turn call the Qt C++ code. It works decently, but
it seems like too much overhead there is not much of a community supporting it.
There is also Cxxi aka CppSharp, which looks interesting, but is currently only
being developed on Windows. It allows you to call C++ libraries directly from C#
without having to go through the extra C bindings. This is probably the best
option, but I have not explored it too much yet due to the immaturity of
Cxxi/CppSharp.

Well. Looks like we aren't going to be using Qt in C# any time soon. So what
about calling C# from C++. Maybe it is possible, but I have yet to find a way
that doesn't involve modifying existing C# libraries to make them callable.

So what are we left with? Well, my crazy idea is to find a language that has
support for both calling C++ (or existing Qt bindings) and the ability to call
C# libraries. (I know. I keep saying C# when I mean 'managed' or 'Common
Language Runtime'. Deal with it.) As it turns out, Python appears to have a very
widely used Qt bindings call PyQt. In fact, there is even an IDE (eric) that has
built-in support for PyQt. PyQt5 is still being developed, so we'll start with
PyQt4. Python 3 on the other hand is looking good, so we will use Python 3.x
instead of Python 2.x. So far so good. It also turns out that there is a library
called Python for .NET. This can be used to call C# libraries directly from
Python. It is not widely used, but seems to have some active development going
on. There is also IronPython, which is an implementation of Python written in
C#. This would be perfect, but it has two problems against it. It can't call 
CPython libraries, meaning it can't use PtQt and also, it only supports Python
2.x and there has yet to be an effort to implement Python 3.x.

So here's what we have going on. The UI is written in Python. It uses PyQt so
that we can use Qt. It uses Python for .NET so that we can use KeePassLib rather
than rewriting the guts of KeePass. It is alot of dependencies (.NET or Mono,
Python, Qt, PyQt and Python for .NET - although the last one can and probably
should be integrated into the final product) and interop between languages 
(that's the crazy part) but it really seems to be the best option I have found
for a cross-platform KeePass program.


Resources
=========

KeePass 2.x source code:
https://github.com/dlech/keepass2

Qt:
http://qt-project.org

Python:
http://python.org

PyQt:
http://www.riverbankcomputing.com/software/pyqt

Python for .NET:
https://github.com/dlech/pythonnet
