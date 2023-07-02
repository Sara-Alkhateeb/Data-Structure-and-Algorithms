import re
from hash_table.hashtable.hashtable import Hashtable
    """
    Finds the first repeated word in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The first repeated word found in the string, or None if no repeated word is found.

    """
def repeated_word(string):
    words = re.split(r"\s+|,\s*", string)  
    obj = Hashtable()
    for word in words:
        if obj.has(word.lower()):
            return word.lower()
        else:
            obj.set(word.lower(), word.lower()) 

if __name__ == "__main__":
    print(repeated_word("Once upon a time, there was a brave princess who..."))
    print(repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness..."))
    print(repeated_word("It was a queer, sultry summer, the summer they electrocuted me, and I didn’t realize I was dead yet..."))


