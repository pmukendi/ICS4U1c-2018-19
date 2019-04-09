from math import sqrt

def fool(num):
    try:
      return sqrt (num)

    except ValueError:
        raise ValueError("cannot square root a negative number.")