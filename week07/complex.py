from __future__ import annotations

class Complex:

    def __init__(self, re:float, im:float) -> None:
        self.re = re
        self.im = im
    
    def __str__(self) -> str:
        return f"{self.re} + {self.im}i"
    
    def add(self, other:Complex) -> Complex:
        """Adds two numbers in the form
        z1 = a+ib
        z2 = c+id
        and returns 
        (a+c) + i*(b+d)
        """
        return Complex(self.re + other.re, self.im + other.im)

    def __add__(self, other:Complex) -> Complex:
        return self.add(other)

    def substract(self, other:Complex) -> Complex:
        return Complex(self.re - other.re, self.im - other.im)
    
    def __sub__(self, other:Complex) -> Complex:
        return self.substract(other)
    
    def __eq__(self, other:Complex) -> bool:
        return ((self.re == other.re) and (self.im == other.im))

