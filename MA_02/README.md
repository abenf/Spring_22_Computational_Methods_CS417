# Requirements

    * Python 3.9

This code makes use of:

- From sys, argv
- From math, modf and log
- The divmod function
- f-string syntax
- Type hints and type aliases

# Sample Execution & Output

If run without command line arguments, using

```
./main.py
```

the following usage message will be displayed

```

Convert decimal numbers to alternative base (default = base 2) using selected precision (default = 8)

./main.py -[options] [option_arg_base, option_arg_prec] [decimal_number_to_convert_0, decimal_number_to_convert_1...]

    options:
        b: changes base to corresponding integer value >= 2
        p: changes display precision to corresponding integer value > 0, < 20

        for multiflag use with example base=4, prec=9, options should be entered with arguments as follows:

        ./main.py -bp 4 9 [decimal_numbers_to_convert]
        ./main.py -pb 9 4 ["]
```

If run using

```
./main.py 0.25 1.5 -4 0.72
```

output *simliar* to

```
|  Decimal   |   Base 2   |
|------------|------------|
| 0.25       | 0.01       |
| 1.5        | 1.1        |
|-4.0        |-100        |
| 0.72       | 0.10111    |

```
will be generated.

If run using

```
./main.py -bp 16 12 0.25 1.5 -4 0.72 17.5
```

output *simliar* to

```
|    Decimal     |    Base 16     |
|----------------|----------------|
| 0.25           | 0.4            |
| 1.5            | 1.8            |
|-4.0            |-4.000000000000 |
| 0.72           | 0.B851EB851EB8 |
| 17.5           | 11.8           |

```
