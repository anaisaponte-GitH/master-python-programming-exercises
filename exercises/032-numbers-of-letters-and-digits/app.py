# Your code here
def letters_and_digits(oracion):
    result = {"letras": 0, "nros": 0}
    for c in oracion:
        if (c.isalpha()):
            result["letras"] += 1
        elif (c.isdigit()):
            result["nros"] += 1
    return(f"LETTERS {result['letras']} DIGITS {result['nros']}")


print(letters_and_digits("hello world! 123"))