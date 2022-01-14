
DecBinTuple = (float, float)
MAX_DIGITS = 8
RESULTS_HEADER = "" #TODO header string here

def result_string(nums : DecBinTuple) -> str:
    return f"{nums[0]:.{MAX_DIGITS}f} | {nums[1]:.{MAX_DIGITS}f}"

def dec_to_bin(my_dec : float) -> DecBinTuple:
    #TODO implement algorithm
    my_bin = my_dec #STUB
    return (my_dec, my_bin)
