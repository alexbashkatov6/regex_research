import re

lesson = 6.26

if lesson == 6.1:
    res = re.findall(r"test", "test TEST", flags=re.IGNORECASE)
    print(res)
    res = re.findall(r"test", "test TEST", flags=re.IGNORECASE + re.MULTILINE + re.DOTALL)
    print(res)
    res = re.findall(r"test", "test TEST", flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
    print(res)
    res = re.findall(r"test", "test TEST", flags=re.I | re.M | re.S)
    print(res)
    res = re.findall(r"(?ims)test", "test TEST")
    print(res)

if lesson == 6.26:
    pass
    # re.IGNORECASE == re.I == (?i)
    # re.MULTILINE == re.M == (?m) - then ^ and $ not for all test, but for 1 line
    # ? re.ASCII == re.A == (?a) - ascii matches only for \w, \W, \b, \B, \d, \D, \s, \S
    # ? re.UNICODE == re.U == (?u) - by default in python re
    # ? re.LOCALE
    # re.DOTALL == re.S == (?s) - (. == any symbol, and new-line symbol too !)
    # re.VERBOSE == re.X == (?x) - use comments in regex and use " " and \n as delimeters
    # re.DEBUG - prints debug info when use re.compile
