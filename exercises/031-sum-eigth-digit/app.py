# Your code here
def all_digits_even():
    l = []
    result = "" 
    for i in range(1000,3001):
        if ((i % 2) == 0):
            l.append(i)
        result = ",".join(map(str,l))
    return result

print(all_digits_even())
