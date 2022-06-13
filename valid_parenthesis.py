def isMatch(char, stack, pairs):
    return stack.pop() == pairs[char]


def isOpening(char, pairs):
    return char in pairs.values()


def isValid(s: str) -> bool:
    openingParens = []
    pairs = {"}": "{", "]": "[", ")": "("}

    for char in s:
        if isOpening(char, pairs):
            openingParens.append(char)

        elif len(openingParens) == 0 or not isMatch(char, openingParens, pairs):
            return False

    return len(openingParens) == 0


isValid("(()")
