# Your code here
class InputOutString:
    def get_string(self):
        self.param = input('Escribe un string: ')
    def print_string(self):
        print (str.upper(self.param))

obj = InputOutString()
obj.get_string()
obj.print_string()