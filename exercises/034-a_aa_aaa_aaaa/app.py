# Your code here
def computed_value(d):
    dicc = {"d": 1, "dd": 2, "ddd": 3, "dddd": 4}
    dicc["d"] = d
    dicc["dd"] = int(str(d) + str(d))
    dicc["ddd"] = int(str(d) + str(d) + str(d))
    dicc["dddd"] = int(str(d) + str(d) + str(d) + str(d))
    return(dicc["d"]+dicc["dd"]+dicc["ddd"]+dicc["dddd"])

print(computed_value(123))
