class Rectangle:
    """
    This class represents a rectangle entity
    Parameters
    ----------
    length, width : 'int' or 'float'
       Sides of the rectangle

    """

    def __init__(self, length=1, width=1):
        self.__length = self.set_length(length)
        self.__width = self.set_length(width)

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def set_length(self, length):
        if not isinstance(length, (int, float)):
            raise TypeError("length must be of data type int or float")
        if length not in range(0, 21):
            raise ValueError("Length should be a floating point number in range 0-20")
        self.__length = length

    def set_width(self, width):
        if not isinstance(width, (int ,float)):
            raise TypeError("width ust be of data type int or float")
        if width not in range(0, 21):
            raise ValueError("Length should be a floating point number in range 0-20")
        self.__width = width

    def calc_perimeter(self):
        return (self.__length + self.__width) * 2

    def calc_area(self):
        return self.__length * self.__width


if __name__ == '__main__':
    rect = Rectangle()
    try:
        rect.set_length(-1)
        print(rect.calc_perimeter())
        print(rect.calc_area())
    except Exception as e:
        print(e)
