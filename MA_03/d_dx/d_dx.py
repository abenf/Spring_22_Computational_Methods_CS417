from math import sin, cos
from typing import Callable

def derivative_of_f_at_x(f: Callable[[float], float], x: float, precision_magnitude: int) -> float:
    h = pow(2, -precision_magnitude)
    return (f(x + h) - f(x))/h

def true_derivative_of_sin_x(x: float) -> float:
    return cos(x)

def abs_err(experimental: float, known: float) -> float:
    return abs(experimental - known)

def plot_h_vs_abs_err(h: list[float], abs_err: list[float]) -> None:
    pass

def cleve_moler() -> float:
    one_third: float = 1.0/3.0
    experimental: float = one_third + one_third + one_third
    return abs_err(experimental, 1)
