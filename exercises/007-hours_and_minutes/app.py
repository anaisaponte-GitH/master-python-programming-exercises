def hours_minutes(seconds):
  # Your code here
  hour = seconds//3600
  sec = seconds%3600
  return hour,sec//60

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
