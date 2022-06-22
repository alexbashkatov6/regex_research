import re

# for code productivity increasing when same pattern used many times
regex = re.compile(r"(\d{3})")
print(regex)
print(regex.findall("123dfsdf234"))
