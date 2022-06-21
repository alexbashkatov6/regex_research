# https://stepik.org/lesson/694358 - курс
# r"[а-яА-ЯёЁa-zA-Z]" - только буквы
# подача неск строк на вход:  str_list = list(map(str.strip, sys.stdin.readlines()))
# подача 1 строки на вход: s = sys.stdin.read()


import re

lesson = 3.11

if lesson == 3.2:
    match = re.match(r"123", "123")
    print(match)

    print("group0 = ", match.group(0), match[0])  # i=0 - regex itself
    print("groups = ", match.groups())
    print("groupdict = ", match.groupdict())

    print("start = ", match.start(0))
    print("end = ", match.end(0))
    print("span = ", match.span(0))

""" MATCH OBJECT - RETURN """

if lesson == 3.3:
    """ 1 match only at string start """
    match = re.match(r"123", "sdfsdf123")
    print(match)

if lesson == 3.4:
    """ 1 match everywere """
    print(re.search(r"123", "sdfsdf123"))
    print(re.search(r"123", "sdfsdf13"))

if lesson == 3.5:
    print(re.fullmatch(r"123", "sdfsdf123"))
    print(re.fullmatch(r"123", "123"))

if lesson == 3.6:
    it = re.finditer(r"123", "sdf123sdf123")
    for i in it:
        print(i)

""" NOT MATCH OBJECT - RETURN """

if lesson == 3.7:
    print(re.findall(r"123", "sdf123sdf123"))

if lesson == 3.8:
    print(re.split(r"123", "asd123fgh123jkl"))
    print(re.split(r"123", "asd123fgh123jkl", 1))

if lesson == 3.9:
    print(re.sub(r"123", "WOW NUMBER", "asd123fgh123jkl"))
    print(" ".join("qwe"))

if lesson == 3.10:
    print(re.subn(r"123", "WOW NUMBER", "asd123fgh123jkl"))

if lesson == 3.11:
    print(re.findall(re.escape("[123]"), "[123]gfhgh[123]"))
