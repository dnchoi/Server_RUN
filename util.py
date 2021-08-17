import argparse
import sys


def _get_exec_args(parser):
    argv = sys.argv[1:]
    if "--" in argv:
        argv = argv[:argv.index("--")]

    args = parser.parse_args(argv)

    return args


def _get_script_args():
    argv = sys.argv

    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []

    parser = argparse.ArgumentParser()  # 0 or 1

    args, unknownargs = parser.parse_known_args(argv)

    return unknownargs


def get_opt_split(parser):
    return _get_exec_args(parser), _get_script_args()

