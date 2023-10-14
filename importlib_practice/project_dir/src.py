# to run in ubuntu set add working dir (root of the project) to PYTHONPATH
# export PYTHONPATH=$PWD
#  check all import sources in sys.path

import sys
import importlib

from importlib_practice.some_pack.new_set_of_funcs import func3


from set_of_funcs import func1, func2

hyphen_set_module = importlib.import_module("importlib_practice.some_pack.hyphen-set")


if __name__ == '__main__':
    print(sys.path)
    func1()
    func2("some arg 2")
    func3()
    hyphen_set_module.func5()
