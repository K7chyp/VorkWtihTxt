from random import sample
from random import choice
from random import randrange
from random import randint
from typing import List


class Shufflers:
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


class WordsMultiplyer:
    def drop_random_words_from_sequence(self, sequence: str, split_by=" ") -> str:
        """
        Input:
        sequence -> str object like ''Мама помыла раму'
        Output
        sequence -> str object like 'Мама помыла'
        """
        split_sequence: List[str] = sequence.split(split_by)
        count_indexes_to_delete: int = randint(a=0, b=len(split_sequence))
        return " ".join(
            word
            for idx, word in enumerate(split_sequence)
            if idx
            not in {
                randint(0, len(split_sequence)) for _ in range(count_indexes_to_delete)
            }
        )

    def multiply_random_words(
        self, sequence: str, max_multiplying=3, split_by=" "
    ) -> str:
        """
        Input:
        sequence -> str object like ''Мама помыла раму'
        Output
        sequence -> str object like 'Мама Мама Мама  помыла  раму раму '
        """
        return " ".join(
            str(str(word + " ") * randint(1, max_multiplying)).replace("  ", " ")
            if choice((True, False))
            else word
            for word in sequence.split(split_by)
        )


class WordsModification:
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
