# Your code here
def divisibles_7(n):
    for i in range(n):
        if (i % 7 == 0):
            yield i

for i in divisibles_7(15):
    print(i)

    
