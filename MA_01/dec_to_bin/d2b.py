
DecBinTuple = (float, float)
MAX_DIGITS = 8

def set_max_digits(value : int):
    global MAX_DIGITS
    MAX_DIGITS = value

def results_header(width : int=(MAX_DIGITS + 4)) -> str:
    return "|{:^{w}}|{:^{w}}|\n".format('Decimal', 'Binary', w = width) + \
          ("|" + "-"*(width))*2 + '|\n'

def result_string(nums : DecBinTuple, precision : int=(MAX_DIGITS + 2)) -> str:
    return f'| {nums[0]:<{precision}} | {nums[1]:<{precision}} |\n'

def dec_to_bin(my_dec : float, round : bool=False, base : int=2, precision : int=MAX_DIGITS) -> DecBinTuple:
    i : int = 0
    d_i : float = my_dec
    c_i : float = 0
    my_bin : float = 0
    while my_dec != 0 and i < precision:
        c_i = base * d_i - 1
        d_i *= base
        if c_i >= 0:
            my_bin += 1 * 10**-(i+1)
            d_i = c_i
        i += 1
    if round and my_dec != 0:
        my_bin += 1 * 10**-(i) # Round up
    return (my_dec, my_bin)