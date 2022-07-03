hafta = 1
aylar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
pazar_sayaci = 0

for yil in range(1900, 2001):
    if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
        aylar[1] = 29
    else:
        aylar[1] = 28

    for i in aylar:
        hafta = (hafta + i) % 7

        if hafta == 0 and yil > 1900:
            pazar_sayaci += 1

print(pazar_sayaci)