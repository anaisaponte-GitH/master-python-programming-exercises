# Your code here
def sequence_of_words(words):
    result = []
    str_result = ""
    palabra = ""
    for i in range(len(words)):
        if (words[i] == ','):
            result.append(palabra)
            palabra = ""
        elif (i == len(words)-1):
            palabra += words[i]
            result.append(palabra)
        else: 
            palabra += words[i]
        result.sort()
    print(result)
    for x in range(len(result)):
        str_result += result[x]
        if (x != len(result)-1):
            str_result += ','
    return(str_result)

print(sequence_of_words("No,gain,pain"))
