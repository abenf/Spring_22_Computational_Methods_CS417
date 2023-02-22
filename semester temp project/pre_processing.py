from typing import Generator, Tuple
import numpy as np
from intake import split_generator, rows_from_txt

class TemperatureData:
    """
    ADT for storing and manipulating CPU temperature data
    
    Attributes:
    data -- mx4 np.ndarray storing temperature data in columns by cpu number
    times -- mx1 np.ndarray storing time data in 30s intervals
    number_of_readings -- count of the number of samples taken
    data_already_initialized -- boolean flag
    time_already_initialized -- boolean flag
    """
    
    def __init__(self):
        """
        __init__ method
        """

        self.data:  np.ndarray = np.array([[0., 0., 0., 0.]])
        self.times: np.ndarray = np.array([[0.]])
        self.number_of_readings: int = 0
        self.least_sqrs_coefs: Tuple[float] = None
        self.data_already_initialized: bool = False
        self.time_already_initialized: bool = False
    
    def get_rows_from(self, filepath: str) -> None:
        """
        Store data from input file 
        """
        
        raw_data = rows_from_txt(filepath)
        for line in raw_data:
            self.store_row(line)

    def store_row(self, row: str, /, count: int=4, delim: str=" ") -> None:
        """
        Given a consistently delimited line-str, parse and store data from line
        
        Line-str format should be:
            'core0_temp core1_temp core2_temp core3_temp'
        
        count can be changed to accomodate number of elements in row
        """

        #count==4 by default
        number_of_elems_in_row: int = count
        #split line and create row
        raw_temps: Generator[str, None, None] = split_generator(row, delim)
        #store time of readings (incr. of 30s)
        if not self.time_already_initialized:
            self.times[0,0] = 0.
            self.time_already_initialized = True
        else:
            self.times = np.append(self.times, np.array([[self.number_of_readings*30.]]), axis=0)
        #increment total readings stored
        self.number_of_readings += 1
        #the memory overhead saved here is negligalbe, but this structure can easily scale to wider data sets 
        temps_array: np.ndarray = np.fromiter(\
                                    (float(string) for string in raw_temps), #str to float generator \
                                    dtype=float, \
                                    count=number_of_elems_in_row)\
                                    .reshape((1, 4)) 

        #add row to data
        if not self.data_already_initialized:
            self.data = temps_array
            self.data_already_initialized = True
            return
        self.data = np.concatenate((self.data, temps_array), axis=0)

    def get_core(self, core_num: int) -> np.ndarray:
        """
        Return all readings from a single core
        """

        core_col = np.empty([self.number_of_readings, 1], dtype=float)
        for i in range(self.number_of_readings):
            core_col[i] = self.data[i, core_num]
        return core_col
