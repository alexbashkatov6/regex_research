import re

lesson = 4.5

if lesson == 4.1:
    match = re.search(r"(?P<first>\d{2})(\d{2})(\d{2})", "sdf353467324534dfgdfg")
    print(match[0])
    print(match.group(0))

    print()
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

    print()
    print(match["first"])
    print(match.group("first"))
    print(match.start("first"))
    print(match.span("first"))

    print()
    print(match.groups())

    print()
    print(match.groupdict())

if lesson == 4.2:
    # findall returns list of group values (group num >= 1)
    res = re.findall(r"(?P<first>\d{2})(\d{2})(\d{2})", "sdf353467324534dfgdfg")
    print(res)

if lesson == 4.3:
    # split inserts group values between splitted elements
    res = re.split(r'\s([+*-:])\s', "2 + 2 * 2 - 5 : 6")
    print(res)

if lesson == 4.4:
    # sub with group gives nothing
    res = re.sub(r'(test)(\d)', "f", "test1 test2 test3 test5")
    print(res)
    # ... but N of group can be used in replaces
    res = re.sub(r'(test)(\d)', r"\2\1", "test1 test2 test3 test5")
    print(res)

if lesson == 4.5:
    # functions in sub
    def func(x):
        print(x)  # match-objects
        return "1"
    res = re.sub(r'(test)(\d)', func, "test1 test2 test3 test5")
    print(res)
    res2 = re.sub(r'\d{2}', lambda x: str(int(x[0])**2), "12 23 34 45")
    print(res2)
