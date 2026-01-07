# Complete the function to return the respective number of the century
import math

def century(year):
  century = year // 100
  if (year % 100) > 0:
    century += 1
  return century


# Invoke the function with any given year
print(century(1990))
