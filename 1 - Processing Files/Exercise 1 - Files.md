# Exercise 1 - Processing Files

In this exercise you will write a Python program
which reads input from a file and writes an output file
based on the input. The focus is on the structure of the
program and not on the transformation, therefore the
transformation is very simple: for each line of the input
file write the length of the line into the output file.

## Goals
* Write a clearly structured program
* Read and write Files
* Think about errors

## Specification
### Processing
An input file like
```
Lorem ipsum dolor sit amet, at
etiam intellegam assueverit mel,
veritus legendos
abhorreant cu eum, ex pro natum
expetendis.
```
is read line by line and the length of each line is written
to an output file like so:
```
30
32
16
31
11
```
### User Interface
1. The program is called `countlines.py`.
1. It will be run from the command line with one
   or two arguments.
1. If the number of arguments is wrong, a help text reminding
   the user of the usage of arguments is printed. (see example below)
1. The first argument is the name of the
   inputfile, the second argument is the output file.
1. If the name of the outputfile is not specified then
   The output file should be the name of the inputfile
   without extension followed by .out.txt
   E.g. if the inputfile is `example.txt` and no output filename is
   given, the outputfilename should be `example.out.txt`.
1. If the outputfile exists the program writes an error message
   and quit without modifying any file.
1. If the inputfile or outputfile can not be opened, an appropriate
   error message is printed.
1. When the program is finished it prints a message with the number
   of lines processed.

Examples (assume `input.txt` exists)
```
C:\Workspace\Exercise>python countlines.py input.txt output.txt
12 lines processed.

C:\Workspace\Exercise>python countlines.py input.txt
12 lines processed.

C:\Workspace\Exercise>python countlines.py input.txt
ERROR: the ouputfile "input.out.txt" already exists. Aborted.

C:\Workspace\Exercise>python countlines.py
Usage: countlines.py <input> [<output>]
       if <output> is missing it defaults to <input>.out.txt

C:\Workspace\Exercise>python countlines.py missing.txt
ERROR: No such file or directory: 'missing.txt'

C:\Workspace\Exercise>python countlines.py input.txt missing\output.txt
ERROR: No such file or directory: 'missing\output.txt'
```

### Program structure
1. The program is split into at least three functions
  * a function `main()` called at program start
    responsible for getting the arguments, opening the files
    and writing the usage and error messages.
  * a function `get_outputfilename(inputfilename)` which
    determines the name of the outputfile in case the program
    was called with one argument
  * a function `write_line_lengths(inputfile, outputfile)` which
    takes two open file objects, reads each line in the inputfile
    and writes its length to the outputfile.
1. The functions must have a docstring. (Consider copying the above)
1. The files are opened as context managers with the `with` statement.
1. The length of a line does not include the final `\n`
   "end of line" character.
1. You should use the `if __name__ == '__main__':` idiom.

## Python documentation references.
* Getting the command line arguments:
  [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv)
* [Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).
* The [`if __name__ == '__main__':` idiom](https://docs.python.org/3/library/__main__.html)
* [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
