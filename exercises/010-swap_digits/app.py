# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
  dec = num // 10
  uni = num % 10
  resul = (uni * 10) + dec
  return resul
   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(79))
