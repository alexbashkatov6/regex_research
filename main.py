# https://stepik.org/lesson/694358 - курс
# r"[а-яА-ЯёЁa-zA-Z]" - только буквы


import re

match = re.match(r"123", "123")
print(match)

print("group0 = ", match.group(0), match[0])  # i=0 - regex itself
print("groups = ", match.groups())
print("groupdict = ", match.groupdict())

print("start = ", match.start(0))
print("end = ", match.end(0))
print("span = ", match.span(0))

