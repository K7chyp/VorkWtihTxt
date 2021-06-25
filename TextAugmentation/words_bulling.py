from random import sample
from random import choice
from random import randrange
from random import randint
from typing import List
from typing import Dict


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


class WordsMultiplyerDropper:

    def __init__(self): 
      self.randomizer: List[bool] = [True] * randint(1, 30) + [False] * randint(1, 30)

    def drop_random_words_from_sequence(self, sequence: str, split_by=" ") -> str:
        """
        Input:
        sequence -> str object like Мама помыла раму'
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
        sequence -> str object like 'Мама помыла раму'
        Output
        sequence -> str object like 'Мама Мама Мама помыла раму раму '
        """
        return " ".join(
            str(str(word + " ") * randint(2, max_multiplying)).replace("  ", " ")
            if choice(self.randomizer)
            else word
            for word in sequence.split(split_by)
        )

    def drop_random_letters_from_word(self, word: str) -> str:
        """
        Input:
        word -> str object like 'колбаса'
        Output
        word -> str object like 'коласа'
        """
        split_word: List[str] = [letter for letter in word]
        indexes_to_drop: Dict[int] = {
            randint(1, len(split_word)) for _ in range(randint(1, len(split_word)))
        }
        return "".join(
            letter
            for idx, letter in enumerate(split_word)
            if idx not in indexes_to_drop
        )
    
    def multiply_random_letters_in_word(self, word: str, max_times_multiplying = 3) -> str:
        """
        Input:
        word -> str object like 'колбаса'
        Output
        word -> str object like 'кооолббаасаа'
        """
        return ''.join(letter * randint(1,max_times_multiplying) if choice(self.randomizer) else letter for letter in word)


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
            letter.upper() if choice(self.randomizer) else letter for letter in word
        )
