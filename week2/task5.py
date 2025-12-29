letrs = set('ABCEHKMOPTXY')
n = int(input())
for _ in range(n):
    plate = input().strip()

    if len(plate) != 6:
        print("No")
        continue

    if (plate[0] not in letrs or
            plate[4] not in letrs or
            plate[5] not in letrs):
        print("No")
        continue

    if not (plate[1].isdigit() and plate[2].isdigit() and plate[3].isdigit()):
        print("No")
        continue

    print("Yes")