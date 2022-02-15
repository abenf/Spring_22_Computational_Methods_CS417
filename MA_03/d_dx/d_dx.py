from math import sin, cos
from typing import Callable
import matplotlib.pyplot as plt

def derivative_of_f_at_x(f: Callable[[float], float], x: float, h: float) -> float:
    return (f(x + h) - f(x))/h

def sin_of_x(x: float) -> float:
    return sin(x)

def true_derivative_of_sin_at_x(x: float) -> float:
    return cos(x)

def abs_err(experimental: float, known: float) -> float:
    return abs(experimental - known)

def plot_h_vs_abs_err(h_revd: list[float], abs_err_list_revd: list[float]) -> None:
    plt.scatter(h_revd,abs_err_list_revd)
    plt.plot(h_revd,abs_err_list_revd)
    plt.grid()
    plt.xlabel("h")
    plt.ylabel("Absolute Error")
    plt.loglog(base=2)
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    plt.show()

def cleve_moler() -> float:
    one_third: float = 4.0/3.0 -1.0
    experimental: float = one_third + one_third + one_third
    return abs_err(experimental, 1)
