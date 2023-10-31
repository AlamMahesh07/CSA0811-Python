import re
test_str="3+4*2"
print("the original string is:"+test_str)
res=sum(map(int,re.findall(r'[+-]?\d+',test_str)))
print("the evaluated result is:"+str(res))
