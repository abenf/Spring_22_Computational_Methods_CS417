import sys
from dec_to_bin.d2b import *

MSG_USAGE = '''

Convert decimal numbers to alternative base (default = base 2) using selected precision (default = 8)

./main.py -[options] [option_arg_base, option_arg_prec] [decimal_number_to_convert_0, decimal_number_to_convert_1...]

    options:
        b: changes base to corresponding integer value >= 2
        p: changes display precision to corresponding integer value > 0, < 20

        for multiflag use with example base=4, prec=9, options should be entered with arguments as follows:

        ./main.py -bp 4 9 [decimal_numbers_to_convert]
        ./main.py -pb 9 4 ["]
'''
MSG_BAD_FLAGS = '''

One or more flags selected is invalid.

Valid flags:
    -b, -p, -bp, -pb
'''
MSG_MISSING_ARGS = '''

One or more missing optional arguments.
'''

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
        print(MSG_USAGE)
    else: 
        main(*args)