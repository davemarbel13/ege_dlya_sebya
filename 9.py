for x in "0123456789ABCDEF":
    s = int("D49" + x + "1", 16) + int("48A3" + x, 16)
    if s % 14 == 0:
        print(s // 14)