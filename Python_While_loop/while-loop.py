# EX1
i = 1
while i < 5:
    print(i)
    i += 1
# เงื่อนไข
# 1
# 2
# 3
# 4

# EX2
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# break หยุดได้
# 1
# 2
# 3


# EX3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# 1
# 2
# 4
# 5
# 6

# EX4
i = 1
while i < 3:
    print(i)
    i += 1
else:
    print("i is no longer than 3")

# 1
# 2
# i is no longer than 3