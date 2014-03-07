#============================================================
# USERID:......... wbahn
# PROGRAMMER:..... Bahn, William L.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ N/A
# FILENAME:....... Util.py
# PYTHON VERSION:. 3.3.3
#============================================================

#============================================================
# This file is a collection of functions that have general
# utility.
#============================================================

import sys # To process command line arguments

class Util:

    @staticmethod
    def getCommandLineArgument(num):
        arg = None
        if num < len(sys.argv):
            arg = sys.argv[num]
        return arg

    @staticmethod
    def repeatedChar(char, count):
        string = ""
        for each in range(count):
            string += char
        return string

#============================================================
