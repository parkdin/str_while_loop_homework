def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    import string
    punc = string.punctuation
    i = 0
    ans = 0
    while i < len(s):
        if s[i] in punc:
            ans += 1
        i += 1
    return ans
