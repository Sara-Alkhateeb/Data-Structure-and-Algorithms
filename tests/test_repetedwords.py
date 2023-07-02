import pytest
from hash_table.repetedword.hashmap_repeatedword import repeated_word

def test_repeated_word():
    assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
    assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...") == "it"
    assert repeated_word("It was a queer, sultry summer, the summer they electrocuted me, and I didn’t realize I was dead yet...") == "summer"

def test_repeated_word_no_repeats():
    assert repeated_word("") is None
    assert repeated_word("Hello hashtable") is None
    assert repeated_word("Hello hello hashtable") == "hello"