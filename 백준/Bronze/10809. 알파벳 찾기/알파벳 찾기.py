INPUT = str(input())

import string
apb = list(string.ascii_lowercase)

for i in range(len(apb)):
    apb[i] = INPUT.find(apb[i])
    print(apb[i], end = ' ')