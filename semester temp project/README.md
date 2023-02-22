# Requirements

    * Python 3.9

This code makes use of:

- From sys: argv, exit
- Numpy
- f-string syntax
- Type hints and type aliases

# Sample Execution & Output
Given a data file in format:
```
core_0_temp@time_0 core_1_temp@time_0 core_2_temp@time_0 core_3_temp@time_0
core_0_temp@time_1 core_1_temp@time_1 core_2_temp@time_1 core_3_temp@time_1
.
.
.
core_0_temp@time_n-1 core_1_temp@time_n-1 core_2_temp@time_n-1 core_3_temp@time_n-1
```

produce least squares and linear piecewise interpolations approximations for the data.

If run:

```
./main.py datafile1.txt [optional: datafile2.txt ...]
```

output *simliar* to

```
0.0<=x<21780.0 ; yi=83.73854 + -0.00025x ; least_squares

```

and 

```
 0.0<=x< 30.0   ; yi=83.00000 + -0.53333x ; interpolation
30.0<=x< 60.0   ; yi=66.00000 + 0.03333x  ; interpolation
60.0<=x< 90.0   ; yi=22.00000 + 0.76667x  ; interpolation
.
.
.
 n-1<=x< n      ; yi=  c0_n-1 + c1_n-1x   ; interpolation
```

for each cpu core will be stored in uniquely named .txt files.

If run with more than one input file, the program will execute and generate output files for each input file.