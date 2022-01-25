# Requirements

    * Python 3.9

This code makes use of:

- From sys, argv
- From math, modf and log
- f-string syntax
- Type hints and type aliases

# Sample Execution & Output

If run without command line arguments, using

```
./main.py
```

the following header will be displayed

```
|  Decimal   |   Binary   |
|------------|------------|
```

If run using

```
./main.py 0.25 1.5 -4 0.72
```

output *simliar* to

```
|  Decimal   |   Binary   |
|------------|------------|
| 0.25       | 0.01       |
| 1.5        | 1.1        |
|-4.0        |-100        |
| 0.72       | 0.10111    |

```
will be generated.
