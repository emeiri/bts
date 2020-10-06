#!/usr/bin/python3.6

import glob
import sys
import subprocess

if __name__ == "__main__":
    if len(sys.argv) == 1:
        cpp_files = glob.glob("*.cpp")
        print(cpp_files)
        cmd = ["g++", " ".join(cpp_files)]
        print(cmd)
        output = subprocess.check_output(cmd)
