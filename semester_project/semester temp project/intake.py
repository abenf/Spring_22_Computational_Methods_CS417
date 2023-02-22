from typing import Generator

def rows_from_txt(filepath: str) -> Generator[str, None, None]:
    """
    generator obj yielding lines from provided .txt file located at filepath
    """

    return (row for row in open(filepath, "r"))     

def split_generator(search_str: str, delimiter: str=" ") -> Generator[str, None, None]:
    """
    splits a string by the specified delimiter, returns a generator object
    
    Keyword Arguments:
    search_str -- the string to be split up by specified delimiter
    delimiter -- delimiting substring
    """
    search_str = search_str.strip()
    start_i: int = 0                                    #init
    delim_i: int = 0                                    #init
    delim_len: int = len(delimiter)                     #length of delimiting substring
    search_str_len: int = len(search_str)               #length of search string
    while delim_i != -1:                                #until end of string is reached
        delim_i = search_str.find(delimiter, start_i)   #find next delimiter index
        slice_i: int = delim_i%(search_str_len + 1)     #compensate for end of string where search_str.find()==-1 
        yield search_str[start_i:slice_i]               #return substring between delimiters
        start_i = slice_i + delim_len                   #increment starting index
        