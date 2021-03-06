def bracket_pair_checker(brackets: str) -> bool:

    stack: list[str] = []
    for bracket in brackets:
        if bracket in '{[(':
            stack.append(bracket)
        if bracket in '}])':
            peek = stack[-1]
            if bracket == ')' and peek == '(':
                stack.pop()
            elif bracket == ']' and peek == '[':
                stack.pop()
            elif bracket == '}' and peek == '{':
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(bracket_pair_checker('[({()})]'))











