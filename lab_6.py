class Fraction:
    def __init__(self, numerator, denominator): #Untuk objek
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}" #Untuk menghasilkan bentuk pembilang penyebut

    def as_float(self):
        return self.numerator / self.denominator #Untuk memberikan hasil pecahan

fraction1 = Fraction(1, 8)
print(fraction1)  
print(fraction1.as_float())  

fraction2 = Fraction(7, 6)
print(fraction2)
print(fraction2.as_float())  



