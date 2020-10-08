#!/usr/bin/python3.6

import glob
import sys
import subprocess
import os
import argparse


def get_parsed_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", default=False, help="Enable debug build")
    parser.add_argument("-r", "--release", action="store_true", default=False, help="Enable release build")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Enable more info")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_parsed_args()

    #if HasAttr(args, "verbose") is False:
    #    args.verbose

    if args.debug is True and args.release is True:
        print("Can enable either debug or release build")
        sys.exit(1)
    if args.debug is False and args.release is False:
        args.release = True

    if args.verbose is True:
        if args.release is True:
            print("Enabled release build")
        else:
            print("Enable debug build")

    cpp_files = glob.glob("*.cpp")
    target_name = "runme"
    if len(cpp_files) == 1:
        target_name = os.path.basename(cpp_files[0][:-4])
    if args.verbose: print("Target name: '" + target_name + "'")
    #print(cpp_files)
    cmd = ["g++", " ".join(cpp_files), "-o", target_name]
    #print(cmd)
    output = subprocess.check_output(cmd)
