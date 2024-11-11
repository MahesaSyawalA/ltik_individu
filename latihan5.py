# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C


inputan_user = {}
def Inputan():
    for i in range(2) : 
        if i == 0:
            print('\033[1m Inputan Mulai : \033[0m')
        else:
            print('\033[1m Inputan Selesai : \033[0m')

        jam = int(input('jam : '))
        menit = int(input('menit : '))
        detik = int(input('detik : '))

        inputan_user[f'input_{i+1}'] = {'jam': jam, 'menit': menit, 'detik': detik}

    sel_jam = inputan_user['input_2']['jam'] - inputan_user['input_1']['jam']
    sel_mnit = inputan_user['input_2']['menit'] - inputan_user['input_1']['menit'] 
    sel_detik = inputan_user['input_2']['detik'] - inputan_user['input_1']['detik'] 

    if sel_detik < 0:
        sel_detik += 60
        sel_menit -= 1
    
    if sel_menit < 0:
        sel_menit += 60
        sel_jam -= 1

    print('\033[1m Hitung Selisih : \033[0m')
    print(f'{sel_jam} jam - {sel_menit} menit - {sel_detik} detik')
    

Inputan()