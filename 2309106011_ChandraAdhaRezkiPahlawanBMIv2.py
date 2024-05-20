#LOGIN
while True:
    nama_user = "chandra"
    password_user = "11"
    login_attempts = 0
    while True:
        nama_input = input("masukkan nama anda: ")
        passoword_input = input("masukkan password anda: ")
        passoword_input = passoword_input.lstrip("0")
        #periksa
        if (nama_input == nama_user) and (passoword_input == password_user):
            print ("selamat datang")
            break
        else:
            print ("login gagal, coba lagi!")
            login_attempts += 1
        #jika login gagal 3x program akan berhenti
            if login_attempts >= 3:
                print("anda telah gagal login 3x. Coba lain waktu")
                exit()

    while True:
        print("kalkulator BMI")
            #Masukkan berat di mg dan tinggi di km
        weight = float(input("Input your weight in mg: "))
        height = float(input("Input your height in km: "))

            #Ubah berat ke kg
        weight = weight / 1000000
            #Ubah tinggi ke m
        height = height * 1000
                #kalkulator BMI
        BMI = weight / (height ** 2)   

            #Kategori BMI
        if BMI < 18.5:
            print("Underweight")
        elif BMI <= 24.9:
            print("Normal")
        elif BMI <= 29.9:
            print("Overweight")
        else:
            print("Obesitas")
            print("Olahraga mas/mba Diet")
        break

    while True:
        pilihan = input("Apakah Anda ingin melanjutkan (ya/tidak)? ").lower()

        if pilihan == "tidak":
            print("Program berhenti.")
            exit()  # Keluar dari loop
        elif pilihan == "ya":
            # Isi dengan tindakan yang ingin Anda lakukan ketika pengguna memilih 'ya'
            break
        else:
            print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")
            break
