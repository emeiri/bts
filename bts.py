#!/usr/bin/python3.6

import glob
import sys
import subprocess
import os

if __name__ == "__main__":
    if len(sys.argv) == 1:
        cpp_files = glob.glob("*.cpp")
        target_name = "runme"
        if len(cpp_files) == 1:
            target_name = os.path.basename(cpp_files[0][:-4])
        print(cpp_files)
        cmd = ["g++", " ".join(cpp_files), "-o", target_name]
        print(cmd)
        output = subprocess.check_output(cmd)
