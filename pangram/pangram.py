from string import ascii_lowercase

def is_pangram(sentence="this is a test of pangram"):
    return set(ascii_lowercase).issubset(sentence)
