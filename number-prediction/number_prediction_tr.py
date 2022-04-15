import random

dogru_sayi = random.randint(1, 10)
hak = 5
sayac = 0
puan = 120

while hak > 0:
    hak -= 1
    sayac += 1
    puan -= 20
    tahmin = int(input('tahmin: '))

    if dogru_sayi == tahmin:
        print(f'Tebrikler {sayac}. denemenizde bildiniz. Puaniniz {puan}')
        break
    elif dogru_sayi > tahmin:
        print('Daha buyuk bir sayi seciniz.')
    else:
        print('Daha kucuk bir sayi seciniz.')
    
    if hak == 0:
        print(f"Hakkiniz kalmadi. Tutulan sayi : {dogru_sayi}")
