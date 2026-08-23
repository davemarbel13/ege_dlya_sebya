alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in alph:
    s = int(f"{x}1{x}2{x}3{x}4{x}5", 27) + int(f"20{x}204", 27) + int(f"20{x}20", 27)
    if s % 25 == 0:
        print(s // 25)
        break

