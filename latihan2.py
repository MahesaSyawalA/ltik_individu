# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

import math

def volume_tabung (r,t):
    hitung = math.pi * r ** 2 * t
    return print(f'volume tabung berdasarkan input yang anda masukan adalah : {hitung}')

jari = int(input('masukan panjang jari-jari tabung : '))
tinggi = int(input('masukan tinggi tabung : '))

volume_tabung(jari,tinggi)