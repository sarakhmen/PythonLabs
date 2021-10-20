class ProductInfo:
    """
    This class represents a binary tree node with Product's code and price
    """
    def __init__(self, code, price):
        self.__left = None
        self.__right = None
        self.__set_code(code)
        self.__price = price

    @property
    def code(self):
        return self.__code

    def __set_code(self, code):
        if not isinstance(code, int):
            raise TypeError('code should be of type int')
        if code < 1:
            raise ValueError('code should be greater than 0')
        self.__code = code

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('price must be of type int or float')
        if price < 0:
            raise ValueError('price should not be less than 0')

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, product_info):
        if product_info and not isinstance(product_info, ProductInfo):
            raise TypeError('left should be of ProductInfo type')
        self.__left = product_info

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, product_info):
        if product_info and not isinstance(product_info, ProductInfo):
            raise TypeError('right should be of ProductInfo type')
        self.__right = product_info
