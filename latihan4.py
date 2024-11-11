# nama : mahesa syawal abdurahman
# nim : 2403372
# kelas : 1 C

username = 'Daspro2023'
password = 'Latihan'

count_death = 0
status_username = False
status_login = False

def Login():
    # menggunakan global agar bisa mengubah data yang telah di deklarasikan di atas
    global count_death, status_username, status_login
    
    if not status_login:
        while count_death < 3:
            if not status_username:
                input_u = input('Masukkan username: ')
                if input_u == username:
                    status_username = True
                else:
                    print('Username salah')
                    count_death += 1
                    print(f'Tersisa {3 - count_death} percobaan')
                    continue
            
            if status_username:
                input_p = input('Masukkan password: ')
                if input_p == password:
                    status_login = True
                    print('Anda berhasil login')
                    break
                else:
                    print('Password salah')
                    count_death += 1
                    print(f'Tersisa {3 - count_death} percobaan')
        
        if not status_login:
            print('Akun terkunci, coba lagi nanti.')
    else:
        print('Anda sudah login')

Login()