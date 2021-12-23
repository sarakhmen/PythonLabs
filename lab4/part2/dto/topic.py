class ITopic:
    """
    A class to represent an interface of the training course topic

    Attributes
    ----------
    name : str
        name of the topic

    """

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be of type str')
        self.__name = value


class Topic(ITopic):
    """
    A class to represent a training course topic

    Attributes
    ----------
    name : str
        name of the topic

    """

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'Topic: name={self.name}'
