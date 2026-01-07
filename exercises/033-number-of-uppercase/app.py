# Your code here
def number_of_uppercase(oracion):
    result = {"upper": 0, "lower": 0}
    for c in oracion:
        if (c.isupper()):
            result["upper"] += 1
        elif (c.islower()):
            result["lower"] += 1
    return(f"UPPERCASE {result['upper']} LOWERCASE {result['lower']}")


print(number_of_uppercase("Hello world!"))