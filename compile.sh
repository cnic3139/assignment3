#!/bin/bash
set -e

BUILD_DIR=build

if [ ${#} != 1 ]; then
	echo "Usage: ${0} filename.vpl" >&2
	exit 1
fi

# builds the ANTLR-generated parse using the grammar file
java -jar /usr/local/lib/antlr-4.7-complete.jar -Dlanguage=Python3 -o ${BUILD_DIR} VPL.g
touch ${BUILD_DIR}/__init__.py

# uses the ANTLR-generated parser to convert the VPL program to ASM
./vpl2asm.py ${1} > /dev/null # ANTLR warnings are annoying
                              # write to file for output instead?

# compiles the ASM and C file together
gcc -Wall -W main.c ${1}.s -o my_program

