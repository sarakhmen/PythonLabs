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
        num_words = 0
        num_lines = 0
        num_chars = 0
        num_spaces = 0

        with open(file_name, 'r') as f:
            for line in f:
                line = line.strip(os.linesep)
                num_lines = num_lines + 1
                num_words = num_words + len(line.split())
                num_chars = num_chars + sum(1 for c in line if not c.isspace())
                num_spaces = num_spaces + sum(1 for s in line if s.isspace())

        self.__num_words = num_words
        self.__num_lines = num_lines
        self.__num_chars = num_chars
        self.__num_spaces = num_spaces

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
        print("Number of words in text file: ", text_processor.get_number_of_words())
        print("Number of lines in text file: ", text_processor.get_number_of_lines())
        print("Number of characters in text file: ", text_processor.get_number_of_chars())
        print("Number of spaces in text file: ", text_processor.get_number_of_spaces())
    except OSError as e:
        print(e)
