import sys
from dec_to_bin.d2b import *

def main(*args):
    results : str = results_header()
    for arg in args[1:]:
        dec_bin : DecBinTuple = dec_to_bin(float(arg))
        results += result_string(*dec_bin)
    print(results)

if __name__ == '__main__':
    main(*sys.argv)