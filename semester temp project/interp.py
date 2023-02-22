from pre_processing import TemperatureData


def linear_coefficients_from_points(point1: tuple[float], point2: tuple[float]) -> tuple[float]:
    """
    Return Tuple of linear coefficients for a line spanning two adjacent data points.
    """
    
    c1 = (point1[1] - point2[1])/(point1[0] - point2[0])
    c0 = point1[1] - c1*point1[0]
    return (c0, c1)

def generate_interpolation_data(temp_data_set: TemperatureData, core_num: int) -> list[tuple[float]]:
    """
    Return list of linear coefficent Tuples for lines between data points.
    """
    
    interpolation_data: list[tuple[float]] = []
    for i in range(temp_data_set.number_of_readings - 1):
        x1, x0 = temp_data_set.times[i + 1], temp_data_set.times[i]
        y1, y0 = temp_data_set.data[i + 1, core_num], temp_data_set.data[i, core_num]
        interpolation_data.append(linear_coefficients_from_points(point1=(x0,y0), point2=(x1,y1)))
    return interpolation_data
