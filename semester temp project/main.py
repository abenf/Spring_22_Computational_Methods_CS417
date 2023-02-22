from sys import argv
from typing import List, Tuple
import numpy as np
from pre_processing import TemperatureData
import least_squares as l_sq
import interp

def get_data(temp_data_objects: List[TemperatureData], *args: Tuple[str]) -> None:
    """
    intake and organize data from text files
    """
    
    for i, file_name in enumerate(args):
        temp_data_objects.append(TemperatureData())
        temp_data_objects[i].get_rows_from(file_name)

def find_least_squares_approximations(temp_data_set: List[TemperatureData]) -> List[Tuple[float]]:
    """
    Find least squares approx. coefficients for each cpu core in the data set.
    Return a List of Tuples containing the above coefficients.
    """

    return [l_sq.gauss_jordan_solver(temp_data_set, core_num) for core_num in range(4)]

def find_piecewise_interpolation_approximations(temp_data_set: List[TemperatureData]) -> List[Tuple[float]]:
    """
    Find Lists of piecewise interpolation approx. coefficients for each pair of points ((xn-1,fn-1),(xn,fn)) in each core
    Return a List consisting of each core's List of point-to-point interpolation coefficients.
    The first Tuple will represent the line spanning the points at time = 0s and time = 30s, the second: the line between 30s and 60s, and so on in 30s intervals.
    """

    return [interp.generate_interpolation_data(temp_data_set, core_num) for core_num in range(4)]

def least_squares_line_str(time_range: Tuple[float], data: Tuple[float]) -> str:
    """
    Return string of data formatted for writefile.
    """
    
    return f"{time_range[0]: > 7}<=x<{time_range[1][0]: < 8} ; yi={data[0]:>.5f} + {data[1]:>.5f}x ; least_squares\n"

def interpolation_line_str(time_range: Tuple[float], data: Tuple[float]) -> str:
    """
    Return string of data formatted for writefile.
    """
    
    return f"{time_range[0][0] : > 7}<=x<{time_range[1][0] : < 8} ; yi={data[0][0]:>.5f} + {data[1][0]:>.5f}x ; interpolation\n"

def write_least_squares_data(core_num: int, approx_data: List[Tuple[float]], times: np.ndarray, total_readings: int, file_number: int,  multiple_files=False) -> None:
    """
    Write formatted data to output file
    """

    mult_files_header = f"dataset-{file_number}-" if multiple_files else ""
    output_file_name = ".\\" + mult_files_header + f"leastsquares-core-{core_num}.txt"
    
    with open(output_file_name, 'w') as writefile:
        time_range: Tuple[float] = (0., times[total_readings - 1])
        coefficients: Tuple[float] = approx_data[core_num]
        line: str = least_squares_line_str(time_range, coefficients)
        writefile.write(line)

def write_interpolation_data(core_num: int, approx_data: List[Tuple[float]], times: np.ndarray, total_readings: int, file_number: int, multiple_files=False) -> None:
    """
    Write formatted data to oput file
    """
    
    mult_files_header = f"dataset-{file_number}-" if multiple_files else ""
    output_file_name = ".\\" + mult_files_header + f"interpolation-core-{core_num}.txt"

    with open(output_file_name, 'w') as writefile:
        lines: List[str] = []
        for i in range(total_readings - 1):
            time_range = (times[i], times[i + 1])
            coefficients = approx_data[core_num][i]
            lines.append(interpolation_line_str(time_range, coefficients))
        writefile.writelines(lines)

def main(*args: Tuple[str]):
    temp_data_objects: List[TemperatureData] = []
    file_names: List[str] = [args[i] for i in range(1, len(args))]
    multiple_files = True if len(args[1:]) > 1 else False
    
    #extract raw data
    for file_name in file_names:    
        get_data(temp_data_objects, file_name)
    
    for file_number, (temp_data_set, file_name) in enumerate(zip(temp_data_objects, file_names)):
        #approximate least squares
        least_squares_approximation_data: List[Tuple[float]] = find_least_squares_approximations(temp_data_set)
        
        #approximate linear piecewise interpolation
        piecewise_interpolation_data: List[Tuple[float]] = find_piecewise_interpolation_approximations(temp_data_set)
        
        #write approximations to .txt files
        for core_num in range(4):
            write_least_squares_data(core_num, least_squares_approximation_data, temp_data_set.times, temp_data_set.number_of_readings, file_number, multiple_files)
            write_interpolation_data(core_num, piecewise_interpolation_data, temp_data_set.times, temp_data_set.number_of_readings, file_number, multiple_files)

if __name__ == '__main__':
    main(*argv)