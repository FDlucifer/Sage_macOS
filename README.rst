Sage_MacOS
==========

The Sage_MacOS project aims to provide a simple, streamlined macOS application which
runs SageMath and can be installed by the usual process of dragging the application
bundle to the /Applications directory.  There is currently a signed and notarized
release of such an app for SageMath 9.4 available in the Releases section, which
is accessable from the right hand side of this page.

The structure of the application bundle is that the main executable is a python
script (run by exec in bash) which runs a small tkinter application.  The
application opens a small window which can launch Sage, either as a command line
program or as a Jupyter notebook.  The command line interface can run either in
Terminal.app or, if it is installed, in iTerm.app.

Once Sage is launched, the app exits.  This behavior is similar to that of Apple's
Launchpad.app.  The application icon can be placed in the dock to make it easy to
launch Sage at any time. 

There is a backwards incompatibility with the former Sage app distributed by
sagemath.org which was removed from Sage 9.3.  That app included a bash script
at the top level of the bundle (e.g. /Applications/SageMath.app/sage).  But
placing a script in that location prevents signing the bundle, since it violates
Apple's specifications for the structure of an application bundle.  Instead, this
app provides a separate installer package which creates an executable bash script
named /usr/local/bin/sage that can be used to run sage from a shell or script.

*  .. image:: https://img.shields.io/github/downloads/3-manifolds/Sage_macOS/v1.2.2/total.svg
*  .. image:: https://img.shields.io/github/downloads/3-manifolds/Sage_macOS/v1.2/total.svg
*  .. image:: https://img.shields.io/github/downloads/3-manifolds/Sage_macOS/v1.1/total.svg
