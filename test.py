str_temp = 's(1)f43f(sf1(shf))djio(s132(223tg)s32(23)233)haha'

stack = ''
ph = 0

for w in str_temp:
    if w == "(":
        ph = ph + 1
        continue
    elif w == ")":
        ph = ph - 1
        continue

    if ph == 0:
        stack = stack + w


print(stack)
