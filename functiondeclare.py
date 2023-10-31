def delchar(s, c):
    if len(c) == 1:
        result = [char for char in s if char != c]
        return ''.join(result)
    else:
        return s
s = "Hello, World!"
c = "l"
result = delchar(s, c)
print(result)
