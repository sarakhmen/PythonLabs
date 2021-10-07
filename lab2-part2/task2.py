import os


class TextProcessor:
    """
    This class represents a text processor that performs statistical processing
    of a text file - counting characters, words, sentences and spaces
    Parameters
    ----------
    file_name : 'str'
       Name of the file to be processed

    """

    def __init__(self, file_name):
        if not os.path.exists(file_name):
            raise FileNotFoundError('Your file not found')
        self.__file_name = file_name
        self.__num_words = 0
        self.__num_lines = 0
        self.__num_chars = 0
        self.__num_spaces = 0

    def parse_text(self):
        with open(self.__file_name, 'r') as f:
            for line in f:
                line = line.strip(os.linesep)
                self.__num_lines = self.__num_lines + 1
                self.__num_words = self.__num_words + len(line.split())
                self.__num_chars = self.__num_chars + sum(1 for c in line if not c.isspace())
                self.__num_spaces = self.__num_spaces + sum(1 for s in line if s.isspace())

    def get_number_of_words(self):
        return self.__num_words

    def get_number_of_lines(self):
        return self.__num_lines

    def get_number_of_chars(self):
        return self.__num_chars

    def get_number_of_spaces(self):
        return self.__num_spaces


if __name__ == '__main__':
    file = 'text.txt'
    try:
        text_processor = TextProcessor(file)
        text_processor.parse_text()
        print("Number of words in text file: ", text_processor.get_number_of_words())
        print("Number of lines in text file: ", text_processor.get_number_of_lines())
        print("Number of characters in text file: ", text_processor.get_number_of_chars())
        print("Number of spaces in text file: ", text_processor.get_number_of_spaces())
    except IOError as e:
        print(e)
