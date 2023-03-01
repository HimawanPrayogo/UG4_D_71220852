
angka=input("Masukkan sebuah angka :")


try:
    angka=int(angka)

    kuadrat= lambda angka:angka**2

    print("Hasil kuadrat dari angka",angka,"adalah:",(kuadrat(angka)))


except:
    print("inputan anda salah")
