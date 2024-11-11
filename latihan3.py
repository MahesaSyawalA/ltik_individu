# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

inputan_nilai = str(input('masukan deret nilai dengan format seperti contoh 1,2,3,4 : '))

data_list = inputan_nilai.split(',')
data_list = [int(i) for i in data_list]

def tot_rat():
    str_rat = sum(data_list) / len(data_list)
    str_tot = ''
    for i in range(len(data_list)):
        if i == len(data_list)-1:
            str_tot += str(data_list[i]) + ' = '
        else:
            str_tot += str(data_list[i]) + ' + '

    print(f'total dari {str_tot} {sum(data_list)}')
    print(f'rata rata dari {sum(data_list)} / {len(data_list)} : {str_rat}')


tot_rat() 