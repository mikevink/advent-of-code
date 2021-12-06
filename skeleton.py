#!/usr/bin/env python

import sys

if "__main__" == __name__:
    day: str = f"{int(sys.argv[1]):02}"
    # make input dir ${day}/{sample,input}.txt
    # make source file aoc2021/${day}.py, content being two methods part01 and part02, both taking a string parameter (input file name) and returning strings as values;
    # need helper method to read all the contents of a file, separate file maybe
    # make test file, tests/test_${day}.py, with 4 methods, test_${day}_part{01,02}_{sample,input}. only the sample is actually a test, validating against example given result

