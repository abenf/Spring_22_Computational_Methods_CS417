from ipaddress import v4_int_to_packed
import sys
from dec_to_bin.d2b import *

FLAG_LOOKUP = {'b': set_base_int, 'p': set_max_digits}

def handle_flags(flag : str, *args) -> int:
    offset : int = 1
    for j in range(1, len(flag)):
        settr = FLAG_LOOKUP[flag[j]] # raises keyerror if provided flag is not in FLAG_LOOKUP
        try:
            settr(args[1 + offset]) # raises IndexError if missing arguments
            offset += 1
        except IndexError:
            raise ValueError
    return offset

def main(*args):
    i : int = 0
    if args[1][0] == '-': # if flag is detected
        try:
            i = handle_flags(args[1], *args)
        except KeyError:
            print('''TODO BAD FLAG ERROR MESSAGE''')
            return
        except ValueError:
            print('''TODO MISSING ARGUMENTS ERROR''')
            return
    results : str = results_header()
    for arg in args[i + 1:]:
        dec_alt : DecAltTuple = dec_to_alt(float(arg))
        results += result_string(*dec_alt)
    print(results)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('''TODO USAGE MESSAGE''')
    else: 
        main(*args)