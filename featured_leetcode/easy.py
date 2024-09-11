# Good stack problem demonstration
def is_valid_parentheses(s):
    """
    20. Valid Parentheses

    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# Good two pointers method demonstration
def is_palindrome(s: str) -> bool:
    """
    125. Valid Palindrome
    A phrase is a palindrome if, after converting all uppercase to lowercase letters and removing all non-alphanumeric
    characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    start, finish = 0, len(s) - 1

    while start < finish:
        if s[start] != s[finish]:
            return False
        start += 1
        finish -= 1
    return True


# Interesting solution with two dicts
def find_judge(n: int, trust: list[list[int]]) -> int:
    """
    997. Find the Town Judge

    In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town
    judge.

    If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person
    labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

    Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
    """
    trust_count = {}
    trustors = set()

    for truster, trusted in trust:
        if trusted not in trust_count:
            trust_count[trusted] = 1
        else:
            trust_count[trusted] += 1

        trustors.add(truster)

    for person in range(1, n + 1):
        if trust_count.get(person, 0) == n - 1 and person not in trustors:
            return person

    return -1
