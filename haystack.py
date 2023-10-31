def find_needle(haystack, needle):
    if not needle:
        return []
    n = len(needle)
    result = []
    for i in range(len(haystack)):
        if haystack[i:i+n] == needle:
            result.append(i)
    return result if result else [-1]
haystack = 'sadbutsad'
needle = 'sad'
print(find_needle(haystack, needle))
