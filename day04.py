from itertools import groupby
from spitslurp import slurp


def is_valid(phrase):
    words = phrase.split()
    freq = [len(list(group)) for key, group in groupby(sorted(words))]
    dups = [count for count in freq if count > 1]
    return len(dups) == 0


assert is_valid('aa bb cc dd ee') is True
assert is_valid('aa bb cc dd aa') is False
assert is_valid('aa bb cc dd aaa') is True


def is_valid_anagram(phrase):
    words = phrase.split()
    words = [''.join(sorted(word)) for word in words]
    freq = [len(list(group)) for key, group in groupby(sorted(words))]
    dups = [count for count in freq if count > 1]
    return len(dups) == 0


assert is_valid_anagram('abcde fghij') is True
assert is_valid_anagram('abcde xyz ecdab') is False
assert is_valid_anagram('a ab abc abd abf abj') is True
assert is_valid_anagram('iiii oiii ooii oooi oooo') is True
assert is_valid_anagram('oiii ioii iioi iiio') is False


phrases = slurp('day04.txt')


print len([phrase for phrase in phrases.split('\n') if is_valid(phrase)])
print len([phrase for phrase in phrases.split('\n') if is_valid_anagram(phrase)])
