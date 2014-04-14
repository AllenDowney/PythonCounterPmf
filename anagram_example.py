"""This file contains code examples I used for a talk.

Copyright 2013 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from collections import Counter


def is_anagram(word1, word2):
    """Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    t = list(word2)
    for c in word1:
        if c not in t:
            return False
        t.remove(c)

    return len(t) == 0


print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')


def is_anagram(word1, word2):
    """Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    t1 = sorted(list(word1))
    t2 = sorted(list(word2))
    return t1 == t2


print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')


def is_anagram(word1, word2):
    """Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    return sorted(list(word1)) == sorted(list(word2))


print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')


def is_anagram(word1, word2):
    """Checks whether the words are anagrams.

    word1: string
    word2: string

    returns: boolean
    """
    return Counter(word1) == Counter(word2)


print is_anagram('tachymetric', 'mccarthyite')
print is_anagram('banana', 'peach')


class Multiset(Counter):
    """A multiset is a set where elements can appear more than once."""

    def is_subset(self, other):
        """Checks whether self is a subset of other.

        other: Multiset

        returns: boolean
        """
        for char, count in self.items():
            if other[char] < count:
                return False
        return True


def can_spell(word, tiles):
    """Checks whether a set of tiles can spell a word.

    word: string
    tiles: string

    returns: boolean
    """
    return Multiset(word).is_subset(Multiset(tiles))


print can_spell('apple', 'aapples')
print can_spell('apple', 'aaples')
