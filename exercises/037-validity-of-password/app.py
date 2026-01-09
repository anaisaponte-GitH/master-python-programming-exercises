# Your code here
import re
def valid_password(password):
    if (len(password) >= 6) and (len(password) <= 12):
        if re.search("[0-9]", password) and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[$#@]", password):
            return "Valid password"
        else:
            return "Invalid password. Please try again"
    else:
        return "Invalid password. Please try again"
    
print (valid_password("ABd"))