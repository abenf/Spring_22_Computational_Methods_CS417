# Requirements

    * Python 3.9

This code makes use of:

- matplotlib.pyplot
- from math, sin, cos
- from typing, Callable
- f-string syntax
- Type hints and type aliases

# Sample Execution & Output

If run using

```
./main.py
```

the following or similar data will be displayed alongside a plot 'h vs. absolute error'

```

Machine Epsilon (using Cleve Moler algorithm): 2.220446049250313e-16

|           h            |  x  |      experimental      |         known          |     absolute error     |
|------------------------|-----|------------------------|------------------------|------------------------|
| 0.50000000000000000000 |  1  | 0.31204800359231588125 | 0.54030230586813976501 | 0.22825430227582388376 |
| 0.25000000000000000000 |  1  | 0.43005453819075878386 | 0.54030230586813976501 | 0.11024776767738098116 |
| 0.12500000000000000000 |  1  | 0.48637287432958942190 | 0.54030230586813976501 | 0.05392943153855034311 |
```
