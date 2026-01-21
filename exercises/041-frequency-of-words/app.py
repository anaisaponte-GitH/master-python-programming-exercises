# Your code here
def compute_word_frequency(cadena):
    lista = cadena.split(" ")
    dicc = {}
    for elemento in lista:
        if elemento in dicc.keys():
            dicc[elemento] += 1
        else:
            dicc[elemento] = 1
    dicc_sorted = dict(sorted(dicc.items()))
    for word, frequency in dicc_sorted:
        print(f"{word}: {frequency}")


input_sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
compute_word_frequency(input_sentence)   
