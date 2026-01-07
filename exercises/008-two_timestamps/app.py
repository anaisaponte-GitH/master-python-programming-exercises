def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    # Your code here 
    hr_resul = hr2 - hr1
    seg_resul = hr_resul * 60 * 60
    min_resul = min2 - min1
    seg_resul = seg_resul + (min_resul * 60)
    seg_resul = seg_resul + (sec2 - sec1)
    return seg_resul


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,2,30,1,3,20))
