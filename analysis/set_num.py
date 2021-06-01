#-*- coding: utf-8 -*-

SET = 52
id = int(input("input set id >>"))
ans = int(id / 32) * 2048 + (id % 32) * (1 << 6) + SET
print(ans)
