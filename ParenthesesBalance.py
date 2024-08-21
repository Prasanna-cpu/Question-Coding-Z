def check(s):
    stack=[]

    for char in s:
        if char=='(':
            stack.append(char)

        else:
            if stack:
                stack.pop()
            else:
                return 1

    if not stack:
        return 0
    else:
        return 1