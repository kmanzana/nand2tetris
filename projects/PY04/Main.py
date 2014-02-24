#============================================================
# USERID:......... wbahn
# PROGRAMMER:..... Bahn, William L.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ PY04
# FILENAME:....... Main.py
# PYTHON VERSION:. 3.3.3
#============================================================

import os
from FileSet import FileSet
from Util import Util
from Parser import Parser
from Code import Code

class Main:

    @staticmethod
    def main():

        print("******************************************")
        print("***          FileSet Report            ***")
        print("******************************************")
        print()

        fileORdir = Util.getCommandLineArgument(1)
        level = Util.getCommandLineArgument(2)
        files = FileSet(fileORdir, "hack")
        files.report()

        print()
        print("******************************************")
        print("***         Processing Report          ***")
        print("******************************************")
        print()

        while files.hasMoreFiles():
            inputFileSpec = files.nextFile()
            print("Processing: %s" % inputFileSpec)
            outputFileSpec = os.path.splitext(inputFileSpec)[0]+".dis"
            inputFile = open(inputFileSpec, "rU")
            outputFile = open(outputFileSpec, "w")
            parser = Parser(inputFile)
            while parser.hasMoreInstructions():
                parser.advance()
                if (parser.instructionType() == "A_TYPE"):
                    value = parser.value()
                    inst = Code.a_type(value)
                if (parser.instructionType() == "C_TYPE"):
                    dest = parser.dest()
                    comp = parser.comp()
                    jump = parser.jump()
                    destMnemonic = Code.destMnemonic(dest)
                    compMnemonic = Code.compMnemonic(comp)
                    jumpMnemonic = Code.jumpMnemonic(jump)
                    inst = Code.c_type(destMnemonic, compMnemonic, jumpMnemonic)
                if (parser.instructionType() == "INVALID"):
                    inst = Code.invalid_type()
                inst += Util.repeatedChar(" ", 20-len(inst))
                inst += "// %05i:" % parser.address()
                inst += " [%s]" % parser.hexInstruction()
                inst += " %s\n" % parser.parsedInstruction()
                outputFile.write(inst)
            outputFile.close()
            inputFile.close()

        print()
        print("Processing of file(s) complete.")
