
DecBinTuple = (float, float, int) # (decimal, binary, sign)
MAX_DIGITS = 8

def set_max_digits(value : int):
    global MAX_DIGITS
    MAX_DIGITS = value

def results_header(width : int=(MAX_DIGITS + 4)) -> str:
    return f'|{"Decimal":^{width}}|{"Binary":^{width}}\n' + ("|" + "-"*(width))*2 + '|\n'
          
def result_string(my_dec : float, my_bin : float, sign : int, width : int=(MAX_DIGITS + 2)) -> str:
    s : str = ' '
    if sign < 0:
        s = '-'
    if len(str(my_bin)) > width:
        my_bin = round(my_bin, MAX_DIGITS)
    return f'|{s}{my_dec:<{width}} |{s}{my_bin:<{width}} |\n'

def dec_to_bin(my_dec : float, base : int=2, precision : int=MAX_DIGITS) -> DecBinTuple:
    sign : int = (my_dec >= 0) - (my_dec < 0)
    i : int = 0
    d_i = my_dec = abs(my_dec)
    c_i : float = 0
    my_bin : float = 0
    while my_dec != 0 and i < precision:
        c_i = base * d_i - 1
        d_i *= base
        if c_i >= 0:
            my_bin += 10**-(i + 1)
            d_i = c_i
        i += 1
    return (my_dec, my_bin, sign)