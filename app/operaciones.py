def sum(a: float, b: float) -> float:
    """
    Args:
      a:float: first number
      b:float: second number
 
    Returns:float: sum first plus second number.
    """
    return a + b

def subtract(a: float, b: float ) -> float:
    """
    Args:
      a:float: fisrt number 
      b:float: second number

    Returns:float: fist number minus second number
    """
    return a - b

def multiply(a: float, b: float ) -> float:
    """
    Args:
      a:float: first number
      b:float: second number

    Returns:float: multiply first by second numbers.
    """
    return a * b

def decorador(func):
    """
    Args:
      func: function

    Returns:float: return decorator function
    """
    def inner(a, b):
        """
        Args:
          a: first input
          b: secound input
        Returns:float:  evaluate function inputs on func arg
        """
        if b == 0:
            "No division by zero is allowed."
        else:
            return func(a,b)    
    return inner
        
@decorador
def divide(a:float, b:float) -> float:
    """
    Args:
      a:float: first number
      b:float: second number

    Returns:float: first divide by secound number
    """    
    return a / b

if __name__ == "__main__":
   print(
      "------ Pruebas unitarias ------ \n",
      f"sum 1 + 2: {sum(1, 2)} \n", 
      f"subtract 1 - 2: {subtract(1, 2)} \n", 
      f"multiply 1 * 2 : {multiply(1, 2)} \n",   
      f"divide 1 + 2: {divide(1, 2)}\n",
      "divide 1 / 0: \n"
   ) 
   divide(1, 0)