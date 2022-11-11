def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k = 0
    while k < len(s):
        space = s.index(' ')
        start = s[:space]
        end = s[space + 1:]
        s_e = start + end
        k += 1
        num = ''
        for i in s_e:
            if i.isdigit():
                num += i
    return len(s_e) - len(num)