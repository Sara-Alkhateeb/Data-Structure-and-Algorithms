def common_word(paragraph):
    """
    Find the first word in the paragraph that achieves the maximum count.
    
    Args:
        paragraph (str): The input paragraph string.
        
    Returns:
        str or None: The first word in the paragraph that has the maximum count,
                     or None if there are no words in the paragraph.
    """
    word_counts = {}
    max_count = 0

    paragraph = paragraph.replace(".", "")
    words = paragraph.lower().split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
        if word_counts[word] > max_count:
            max_count = word_counts[word]
            

    # Find the first word(s) with the maximum count
    for word, count in word_counts.items():
        if count == max_count:
            return word

    return None  # Return None if there are no words in the paragraph


# Test the function
p1 = "In a galaxy far far away"
print(common_word(p1))  # Output: far

p2 = "Taco cat ate a taco"
print(common_word(p2))  # Output: taco

p3 = "No. Try not. Do or do not. There is no try."
print(common_word(p3))  # Output: no
