def balanced_brackets(text):
    stack = []
    for t in text:
        if t == "(" or t == "[" or t == "{":
            stack.append(t)
        elif t == ")":
            if not stack or stack.pop() != "(":
                return False
        elif t == "]":
            if not stack or stack.pop() != "[":
                return False
        elif t == "}":
            if not stack or stack.pop() != "{":
                return False
    return len(stack) == 0

print(balanced_brackets("(hello)"))
print(balanced_brackets("{[()]}"))
print(balanced_brackets("([]"))
print(balanced_brackets("((hello)"))

    
    
    
    
    
    
    
    

