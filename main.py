#!/usr/bin/python

import sys
import getopt

from CompilePackage import CompilePackage


def main(argv):
    package = ''
    verbose = 'HIGH'
    try:
        opts, args = getopt.getopt(argv, "hi:v:", ["input=", "verbose="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_help()
            sys.exit()
        elif opt in ('-v', '--verbose') and arg in ('LOW', 'MEDIUM', 'HIGH'):
            verbose = arg
        elif opt in ('-i', '--input'):
            package = arg
    if package != '':
        print('Input file: {}\nVerbosity: {}'.format(package, verbose))

    compiler = CompilePackage()
    compiler.compile_startup()
    compiler.compile()


def print_help():
    print('SleepyCoati.py [OPTION]... [FILE]...')
    print('Available options:\n\t-h, --help\tShow help guide\n\t-v, --verbose\tChange verbosity, [LOW|MEDIUM|'
          'HIGH]\n\t-i, --input\tDeclare input package for compilation')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print_help()
