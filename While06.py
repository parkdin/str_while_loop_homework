def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    s = s.lower()
    i = 0
    ans = 0
    vowel = "a", "e", "i", "o", "u"
    while i < len(s):
        if not s[i] in vowel:
            ans += 1
        i += 1
    return ans
print(main("CodeschoolUz"))