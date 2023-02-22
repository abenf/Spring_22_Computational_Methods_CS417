from typing import Tuple
import numpy as np
from sys import exit
from pre_processing import TemperatureData

def x(temp_data: TemperatureData) -> np.ndarray:
    """
    return X := [[1, x0],[1, x1],...,[1, xm-1]]
    """

    times: np.ndarray = temp_data.times.reshape(temp_data.times.shape[0], -1)
    ones: np.ndarray = np.ones_like(times)
    return np.concatenate((ones, times), axis=1)

def xTx(temp_data: TemperatureData) -> np.ndarray:
    """
    Return the product of the transposed X matrix with itself
    X  := [[1, x0],[1, x1],...,[1, xm-1]]
    XT := [[1, 1,...,1], [x0, x1,..., xm-1]]
    XTX:= [[1, x0 +...+ xm-1], [x0 +...+ xm-1, x0^2 +...+ xm-1^2]]
    """
    
    X:  np.ndarray = x(temp_data)
    return np.matmul(X.T, X)

def xTy(temp_data: TemperatureData, core_num: int) -> np.ndarray:
    """
    Return the product of the transposed X matrix with a core's temperature readings
    X  := [[1, x0],[1, x1],...,[1, xm-1]]
    Y  := [[f0], [f1], ..., [fn-1]]
    XT := [[1, 1,...,1], [x0, x1,..., xm-1]]
    XTY:= [[f0 +... + fn-1],[x0*f0 +...+xm-1*fn-1]]
    """

    X:  np.ndarray = x(temp_data)
    Y:  np.ndarray = temp_data.get_core(core_num)
    return np.matmul(X.T, Y)

def swap_rows(matrix: np.ndarray, a: int, b: int) -> None:
    """
    Gaussian elimination step: swap rows a and b
    """

    matrix[[a, b], :] = matrix[[b, a], :]

def scale_row(matrix: np.ndarray, i: int, scalar: float) -> None:
    """
    Gaussian elimination step: multiply each element of a row by a scalar
    """

    matrix[[i], :] = scalar * matrix[[i], :]

def subtract_rows(matrix: np.ndarray, a: int, b: int, /, scale_pivot_by=1) -> None:
    """
    Gaussian elimination step: subtract each indexed element of one row from another, one row optinally scaled
    """

    c = scale_pivot_by
    matrix[[a],:] = matrix[[a],:] - c*matrix[[b],:]

def gauss_jordan_solver(matrix: np.ndarray, core_num: int) -> Tuple[float]:
    """
    uses row techniques to transform matrix into reduced row-echelon form, return tuple of solutions
    aka solve for basis-function coefficients

    FOR THE PURPOSES OF THIS PROJECT:
    simple linear regression (least squares), assuming best fit polynomial: phi_hat(x) = c0*x^0 + c1*x^1
    ==> XTX|XTY is a 2x2 square matrix augmented with a 2-vector
    """

    XTX = xTx(matrix)                       
    XTY = xTy(matrix, core_num)   
    
    #augmented matrix
    XTX_XTY = np.concatenate((XTX, XTY), axis=1)
    row_dim = np.shape(XTX_XTY)[0]
    
    # pivot column                  
    pivot_col = -1

    for pivot_row in range(row_dim):
        pivot_col += 1
        nonzero_row = pivot_row
        
        #if a diagonal element == 0, search below for non-zero element in pivot column then swap the rows
        while XTX_XTY[nonzero_row, pivot_col] == 0:
            nonzero_row += 1
            if nonzero_row == row_dim:
                print("oops! dependent system! ya done goofed")
                exit()
        if nonzero_row != pivot_row:
            swap_rows(XTX_XTY, nonzero_row, pivot_row)
        
        #if pivot entry != 1, scale pivot_row
        if XTX_XTY[pivot_row, pivot_col] != 1:
            scale_row(XTX_XTY, pivot_row, 1/XTX_XTY[pivot_row, pivot_col])
        
        #reduce all other elements in pivot column to zero
        for i in range(row_dim):
            if i == pivot_row or XTX_XTY[i, pivot_col] == 0: continue
            subtract_rows(XTX_XTY, i, pivot_row, scale_pivot_by=XTX_XTY[i, pivot_col])
    return tuple((XTX_XTY[i,-1] for i in range(row_dim)))
