import sys
from .MA_01.machine_assignment_01 import *

def main(argc : int, *args):
    results : str = RESULTS_HEADER
    for i in range(argc):
        dec_bin : DecBinTuple = dec_to_bin(args[i])
        results += result_string(dec_bin)
    print(results)


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)