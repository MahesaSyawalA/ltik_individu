# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

deret = [];

def function_fibonaci(c) :
    for i in range(c):
        jumlah = deret[i]+deret[i+1]
        deret.append(jumlah)

    return print(deret)

nilai_pertama = int(input('masukan nilai pertama : '))
deret.append(nilai_pertama)

nilai_kedua = int(input('masukan nilai kedua : '))
deret.append(nilai_pertama)

rentang_deret = int(input('masukan rentang/panjang deret fibonaci yang ingin anda buat setelah angka ke dua : '))

function_fibonaci(rentang_deret) 

