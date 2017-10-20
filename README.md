# COMP3109 Assignment 3

## Dependencies
This code requires Python3 and pip3 to be installed on your system.
In order to run this code, you need to have **ANTLR** installed, both as a *.jar* file and via *pip3*. To install the *.jar*, navigate to http://www.antlr.org and follow the "quick start" guide for your specific OS. To install ANTLR so that it can be imported for use in Python3, run the following command:
```bash
sudo pip3 install antlr4-python3-runtime
```

To build the program, run the provided file *compile.sh*, with the VPL input file name as the first argument. This script uses the grammar to generate various ANTLR files, runs the python program to produce the output assembly file, and then compiles this with a given C file to produce the final executable *my_program*. This can then be executed in the usual fashion. 