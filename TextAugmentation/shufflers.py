from random import sample
from random import choice
from typing import List


class Shufflers:
    def __init__(self):
        pass

    def sequence_shuffle(self, sequence: str, split_by=" ") -> str:
        """
        Input:
        sequence -> str object like 'Мама помыла раму'
        Output:
        sequence -> str object like 'Раму помыла мама'
        """
        split_sequence: List[str] = sequence.split(split_by)
        return split_by.join(sample(split_sequence, k=len(split_sequence)))

    def letters_shuffler(self, word: str) -> str:
        """
        Input:
        word -> str object like 'колбаса'
        Output
        word -> str object like 'кобаосл'
        """
        split_word: List[str] = [letter for letter in word]
        return "".join(sample(split_word, k=len(split_word)))

    def random_words_upper(self, word: str) -> str:
        """
        Idk how but maybe you'll be using it
        Input:
        word -> str object like 'колбаса'
        Output
        word -> str object like 'КоЛбаСА'
        """
        return "".join(
            letter.upper() if choice((True, False)) else letter for letter in word
        )
