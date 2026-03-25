class Calculator:
    def __init__(self):
        self._sum = 0
        
    @staticmethod
    def add(x, y):
      return x + y
    
    @staticmethod
    def subtract(x,y):
       return abs(x-y)

def main():
   calc_instance=Calculator()
   print('Enter the first number:') 
   num1 = float(input()) # Input from user for First Number.
   operation = input("Enter an operator ('+' or '-', '*' , '/'): ")
    if (operation == "+") :
        result=calc_instance._sum += num1; print('Addition Result: ', calc_instance._sum)
    elif(operation=="-"): 
         ...and so on...