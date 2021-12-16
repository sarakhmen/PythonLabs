from lab4.part2.dto.ITopic import ITopic


class Topic(ITopic):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'Topic: name={self.name}'
