int_number=0
multiple=1

for i in range(3):
    int_number=int(input())
    multiple*=int_number

multiple=str(multiple)

for i in range(10):
    print(multiple.count(str(i)))