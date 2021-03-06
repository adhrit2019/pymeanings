PyMeanings
==========

Video Demo: 
------------

Description:
------------

Introduction
------------

This is my final project in `CS50x
Harvard <https://cs50.harvard.edu/x>`__. This program can work in Debian
Linux based computers (but it can work on Mac OS also, although I've not
checked). This project is a program that finds meanings of words. This
version of the program uses internet and it will run with a keyboard
shortcut. If you want to find a meaning of a word then follow the
following steps:

1. Connect to the internet.
2. Select the word you want to find the meaning of.
3. Press the keyboard shortcut you had set (Go to `'Setting up your
   PyMeanings' <#setting-up-your-pymeanings>`__)

Setting up your PyMeanings
--------------------------

Installing dependencies
~~~~~~~~~~~~~~~~~~~~~~~

1. ``xsel``: Check that ``xsel`` is installed in your system by typing
   ``xsel --version`` in your terminal. If it is not installed then
   install it by typing ``sudo apt install xsel`` in your terminal.

``xsel`` is a program that retrieve and set the X selection as it is
given in the manual page accessed by typing ``man xsel``. It is the
program responsible for capturing the selected text by the user.

Installing pymeanings
~~~~~~~~~~~~~~~~~~~~~

This program works on `Python <https://python.org>`__ version = 3.7+.
Install the package by typing in your terminal
``pip install pymeanings``

The keyboard shortcut can be anything you want. In your terminal run
``which pymeaning``. Assign your keyboard shortcut to the location given
the bash script you had run. Following are some links which can tell you
how to make keyboard shortcuts in different Linux-based OS:

1. For
   `Xubuntu <https://blog.programster.org/xubuntu-setting-keyboard-shortcuts>`__
2. For
   `Ubuntu <https://help.ubuntu.com/stable/ubuntu-help/keyboard-shortcuts-set.html.en>`__
3. For `Linux
   Mint <https://www.technipages.com/linux-mint-how-to-create-new-custom-keyboard-shortcuts/amp>`__
4. For `Mac OS
   X <https://support.apple.com/en-in/guide/mac-help/mchlp2271/mac>`__

Different outputs
-----------------

If the output gives you an "Error" window. Then it must be a loss of
steps you made. Following are the list of errors:

1. Message: "Please select word for finding meaning". Then it means you
   forgot to select the word.
2. Message: "Can't find meaning of '{your word}'. Check your internet
   connection or the word you selected might not mean anything!!". Then
   it means you are disconnected from the internet or the word you
   selected does not make sense.

If the output is something else other than the errors and shows a bulb
symbol, then it means you followed the steps properly.

**Best of Luck with PyMeanings**

*Adhrit Pramanik*
