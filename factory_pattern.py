# Factory Method design pattern example.
import sys


class Word:
    word = ''

    @staticmethod
    def get_word(w):
        if 'red' == w:
            return Red()
        elif 'blue' == w:
            return Blue()


class Red(Word):
    word = 'Word is red'


class Blue(Word):
    word = 'Word is blue'

arg = sys.argv[1]

w = Word.get_word(arg)
print('Word: {}, Class Name: {}'.format(w.word, w.__class__.__name__))

