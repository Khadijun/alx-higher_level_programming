0X00.PYTHON - HELLO,WORLD

REQUIREMENT
A.Python script
 * The first line of all your files should be exactly #!/usr/bin/python3
 * A README.md file at the root of the repo, containing a description of the repository
 * A README.md file, at the root of the folder of this project, is mandatory
 * Your code should use the pycodestyle (version 2.8.*)
 * All your files must be executable
 * The length of your files will be tested using wc

B.Shell script
 * All your scripts should be exactly two lines long (wc -l file should print 2)
 * The first line of all your files should be exactly #!/bin/bash
 * All your files should end with a new line
 * All your files must be executable

C. C script
 * Allowed editors: vi, vim, emacs
 * All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
 * All your files should end with a new line
 * Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
 * You are not allowed to use global variables
 * No more than 5 functions per file
 * In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
 * The prototypes of all your functions should be included in your header file called lists.h
 * Don’t forget to push your header file
 * All your header files should be include guarded

TASKS.

0. Run Python file :Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

1. Run inline : Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE
2. Hello, print : Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
3. Print integer : Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use f-strings tips

