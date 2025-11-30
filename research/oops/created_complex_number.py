class ComplexNumber:
    def __init__(self, real: float = 0.0, img: float = 0.0):
        self.real = real
        self.img = img

    def __str__(self):
        
        if self.real == 0:
            return f"{self.img}i"
        elif self.img < 0:
            s = f"{self.real}{self.img}i"
        else:
            s = f"{self.real}+{self.img}i"

        return s

    def __add__(self, other):

        new_real = 0
        new_img = 0
        new_real = self.real + other.real
        new_img = self.img + other.img
        return ComplexNumber(new_real, new_img)

    def __sub__(self, other):

        new_real = 0
        new_img = 0
        new_real = self.real - other.real
        new_img = self.img - other.img
        return ComplexNumber(new_real, new_img)

    def __mul__(self, other):
        new_real = 0
        new_img = 0

        new_real = (self.real * other.real) - (self.img * other.img)
        new_img = (self.real * other.img) + (other.real * self.img)
        return ComplexNumber(new_real, new_img)

    def __truediv__(self, other):
        den = other.real**2 + other.img**2
        return self * ComplexNumber(other.real/den, (-1*other.img)/den)

    def conjugate(self):
        return ComplexNumber(self.real, self.img * -1)

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img


