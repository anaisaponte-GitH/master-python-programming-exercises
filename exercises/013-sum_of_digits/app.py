# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):
  total = 0
  while num > 0:
    dig = num % 10 # Me quedo con el ultimo digito
    num = num // 10 # Me deshago del ultimo digito
    total += dig
  return total


# Invoke the function with any three-digit number
print(digits_sum(1234))
