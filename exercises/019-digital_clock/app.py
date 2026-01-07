# Complete the function to return how many hours and minutes are displayed on the 24h digital clock
def digital_clock(n):
  h = n // 60
  m = n % 60
  return h, m

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(150))
