def isBalanced(s):
    open_brackets = ["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    stack = []
    for sub_s in list(s):
        if sub_s in open_brackets:
            stack.append(sub_s)
        elif sub_s in close_brackets:
            if not stack:
                return "NO"
            first_stack_elem = stack.pop()
            if first_stack_elem == "(" and sub_s == ")":
                continue
            elif first_stack_elem == "[" and sub_s == "]":
                continue
            elif first_stack_elem == "{" and sub_s == "}":
                continue
            else:
                return "NO"
    if stack:
        return "NO"
    return "YES"


isBalanced("{[]}")
