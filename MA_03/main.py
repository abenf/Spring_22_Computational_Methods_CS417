from d_dx import *
from d_dx.d_dx import abs_err, cleve_moler, derivative_of_f_at_x, plot_h_vs_abs_err, sin_of_x, true_derivative_of_sin_at_x

def results_header() -> str:
    return f"| {'h':^22} | {'x':^3} | {'experimental':^22} | {'known':^22} | {'absolute error':^22} |\n" \
        +  f"|{'':-<24}|{'':-<5}|{'':-<24}|{'':-<24}|{'':-<24}|\n"

def results_line(h: float, x: float, experimental: float, known: float, absolute_error: float) -> str:
    return f"| {h:<.20f} | {x:^3} | {experimental:.20f} | {known:.20f} | {absolute_error:.20f} |\n"

def main() -> None:
    result_str: str = results_header()
    abs_err_list: list[float] = []
    x: int = 1
    h: list[float] = [pow(2, -precision_magnitude) for precision_magnitude in range(1,31)]
    
    for precision in h:
        experimental: float = derivative_of_f_at_x(sin_of_x, x, precision)
        known: float = true_derivative_of_sin_at_x(x)
        abs_err_list.append(abs_err(experimental, known))
        result_str += results_line(precision, x, experimental, known, abs_err_list[-1])
    print(f"\nMachine Epsilon (using Cleve Moler algorithm): {cleve_moler()}\n")
    print(result_str)
    plot_h_vs_abs_err(h[::-1], abs_err_list[::-1])
    
if __name__ == "__main__":
    main()