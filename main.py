# https://stepik.org/lesson/694358 - курс
# r"[а-яА-ЯёЁa-zA-Z]" - только буквы


import re

lesson = 3.4

if lesson == 3.2:
    match = re.match(r"123", "123")
    print(match)

    print("group0 = ", match.group(0), match[0])  # i=0 - regex itself
    print("groups = ", match.groups())
    print("groupdict = ", match.groupdict())

    print("start = ", match.start(0))
    print("end = ", match.end(0))
    print("span = ", match.span(0))

if lesson == 3.3:
    """ 1 match only at string start """
    match = re.match(r"123", "sdfsdf123")
    print(match)

if lesson == 3.4:
    """ 1 match everywere """
    print(re.search(r"123", "sdfsdf123"))
    print(re.search(r"123", "sdfsdf13"))

