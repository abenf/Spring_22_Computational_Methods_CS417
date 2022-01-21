from math import modf, log

BinListTuple = list[list[int], list[int]] #fractional and whole number parts
DecBinTuple = (float, BinListTuple, int) #(decimal, binary -> [integer, fractional], sign)
MAX_DIGITS = 8 #precision
BASE_INT = 2 #number base

def set_max_digits(value : int): #for use with future command line flags
    global MAX_DIGITS
    MAX_DIGITS = value

def set_base_int(value : int):
    global BASE_INT
    BASE_INT = value

def results_header(width : int=(MAX_DIGITS + 4)) -> str:
    return f'|{"Decimal":^{width}}|{"Binary":^{width}}|\n' + ("|" + "-"*(width))*2 + '|\n'

def binary_string(bin_list : list[int]) -> str:
    return ''.join(str(zeros_and_ones) for zeros_and_ones in bin_list) #convert contents of list[int] to strings and join
          
def result_string(my_decimal : float, my_binary : BinListTuple, sign : int, width : int=(MAX_DIGITS + 2)) -> str:
    s : str = (sign >= 0)*' ' + (sign < 0)*'-' #add a minus sign if number is negative
    bin_str =  binary_string(my_binary[0]) 
    try: #don't print fractional if my_binary is a whole number
        bin_str += '.' + binary_string(my_binary[1])
    except IndexError:
        pass
    return f'|{s}{my_decimal:<{width}} |{s}{bin_str[:width]:<{width}} |\n'


def cut_trailing_zeros(my_list : list[int]) -> list[int]:
    i : int = 0
    val_at_index_is_zero : bool = True
    while val_at_index_is_zero:
        i -= 1
        val_at_index_is_zero -= (my_list[i]) #search backwards for final 1
    return my_list[:i+1]

def dec_to_bin(my_decimal : float, base : int=BASE_INT, precision : int=MAX_DIGITS) -> DecBinTuple:
    sign : int = (my_decimal >= 0) - (my_decimal < 0) #determine and store sign of inputted decimal number
    my_binary_list : BinListTuple = []
    fractional, integer = modf(abs(my_decimal)) #split integer and fractional elements
    integer = int(integer)

    my_binary_list.append(convert_integer(integer, base))
    bin_fractional = convert_fractional(fractional, base, precision)
    if bin_fractional:
        my_binary_list.append(bin_fractional)

    return (abs(my_decimal), my_binary_list, sign)

def convert_integer(buffer : int, base : int) -> list[int]:
    i  : int = 0
    try:
        int_magnitude = int(log(buffer, base)) #throws ValueError if buffer == 0
        if int_magnitude == 0: 
            raise Exception()
        digit_i : list[int] = [0 for n in range(int_magnitude + 1)] #list of enough zeros to handle integer part's magnitude
        while buffer != 0 and i <= int_magnitude:
            my_remainder = buffer%base
            buffer = buffer//base
            digit_i[i] = my_remainder
            i += 1
        return digit_i[::-1] #reverse list to proper orientation for binary representation AKA this algorithm gives results 'backwards'
    except ValueError: #catches log(0)
        return [0]
    except: #catches log_b(a) where 0 < a < b
        return [buffer]

def convert_fractional(buffer : float, base : int, precision : int) -> list[int]:
    i : int = 0
    digit_i : list[int] = [0 for n in range(precision)] #precision-length list of zeros
    while buffer != 0 and i < precision:
        buffer *= base
        digit_i[i] = int(buffer)
        buffer -= digit_i[i]
        i += 1
    for elem in digit_i:
        if elem != 0:
            return cut_trailing_zeros(digit_i)
    return []
