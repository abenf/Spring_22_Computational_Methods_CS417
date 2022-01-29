from math import modf, log

AltBaseListTuple = list[list[int], list[int]] # fractional and whole number parts
DecAltTuple = (float, AltBaseListTuple, int) # (decimal, alt base number -> [integer, fractional], sign)
MAX_DIGITS = 8  # precision
BASE_INT = 2    # number base
BASE_IS_GT_25 = False   # number base is greater than 25 (set in set_base_int)


def convert_number_list(number_list : list[int]) -> list[str]:
    for k, digit in enumerate(number_list):
        number_list[k] = convert_gt_ten_digit(digit)
    return number_list

def convert_gt_ten_digit(value : int):
    gt_ten_digit : str = ""
    no_of_Zs = 0
    if value >= 26:
        i, value = divmod(value, 26)
        no_of_Zs = BASE_INT//(i*26 + 10)
    if value >= 10:
        value = chr(55 + value)
    gt_ten_digit += 'Z'*no_of_Zs + str(value) + ";"*BASE_IS_GT_25
    return gt_ten_digit

def set_max_digits(value : int): 
    global MAX_DIGITS
    value = int(value)
    if value < 1 or value > 20:
        print("Invalid precision; revert to default")
        return
    MAX_DIGITS = value

def set_base_int(value : int): 
    global BASE_INT
    global BASE_IS_GT_25
    value = int(value)
    if value < 2:
        print("Invalid base; revert to default")
    BASE_INT = value
    if value > 25:
        BASE_IS_GT_25 = True

def results_header(width : int=(MAX_DIGITS + 4)) -> str:
    base_str = "Base " + str(BASE_INT)
    return f'|{"Decimal":^{width}}|{base_str:^{width}}|\n' + ("|" + "-"*(width))*2 + '|\n'

def alt_base_string(alt_base_list : list[int]) -> str:
    alt_str = ''.join(str(zeros_and_ones) for zeros_and_ones in alt_base_list)
    if BASE_IS_GT_25:
        alt_str = alt_str[:-1]
    return alt_str # convert contents of list[int] to strings and join
          
def result_string(my_decimal : float, my_alt_base_num : AltBaseListTuple, sign : int, width : int=(MAX_DIGITS + 2)) -> str:
    s : str = (sign >= 0)*' ' + (sign < 0)*'-' # add a minus sign if number is negative
    alt_base_str =  alt_base_string(my_alt_base_num[0]) 
    try: # don't print fractional if my_alt_base_num is a whole number
        alt_base_str += '.' + alt_base_string(my_alt_base_num[1])
    except IndexError:
        pass
    return f'|{s}{my_decimal:<{width}} |{s}{alt_base_str[:width]:<{width}} |\n'

def cut_trailing_zeros(my_list : list[int]) -> list[int]:
    i : int = 0
    val_at_index_is_zero : bool = True
    while val_at_index_is_zero:
        i -= 1
        val_at_index_is_zero -= (my_list[i] != 0) # search backwards for final non-zero digit
    if i == -1:
        return my_list
    return my_list[:i+1]

def dec_to_alt(my_decimal : float) -> DecAltTuple:
    sign : int = (my_decimal >= 0) - (my_decimal < 0) # determine and store sign of inputted decimal number
    my_alt_base_list : AltBaseListTuple = []
    fractional, integer = modf(abs(my_decimal)) # split integer and fractional elements
    integer = int(integer)

    my_alt_base_list.append(convert_integer(integer))
    alt_fractional = convert_fractional(fractional)
    if alt_fractional:
        my_alt_base_list.append(alt_fractional)

    return (abs(my_decimal), my_alt_base_list, sign)

def convert_integer(buffer : int) -> list[int]:
    base = BASE_INT
    i  : int = 0
    try:
        int_magnitude = int(log(buffer, base)) # throws ValueError if buffer == 0
        if int_magnitude == 0: 
            raise Exception()
        digit_i : list[int] = [0 for n in range(int_magnitude + 1)] # list of enough zeros to handle integer part's magnitude
        while buffer != 0 and i <= int_magnitude:
            my_remainder = buffer%base
            buffer = buffer//base
            digit_i[i] = my_remainder
            i += 1
        if base > 10:
            digit_i = convert_number_list(digit_i)
        return digit_i[::-1] # reverse list to proper orientation for alt base representation
                             # AKA this algorithm gives results 'backwards'
    except ValueError: # catches log(0)
        return [0]
    except: # catches log_b(a) where 0 < a < b
        if base > 10:
            return convert_number_list([buffer])
        return [buffer]

def convert_fractional(buffer : float) -> list[int]:
    base = BASE_INT
    precision = MAX_DIGITS
    i : int = 0
    digit_i : list[int] = [0 for n in range(precision)] # precision-length list of zeros
    while buffer != 0 and i < precision:
        buffer *= base
        digit_i[i] = int(buffer)
        buffer -= digit_i[i]
        i += 1
    for elem in digit_i:
        if elem != 0:
            digit_i = cut_trailing_zeros(digit_i)
    if base > 10:
        digit_i = convert_number_list(digit_i)
    return digit_i
