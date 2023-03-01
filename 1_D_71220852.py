
#hanya jumlah seluruh deret
#Sn = n/2 (2a + (n – 1) b)

print("="*10," BARIS ARITMATIKA ","="*10)

awal=input("Masukkan bilangan awal :")
selisih=input("Masukkan selisih bilangan :")
suku=input("Masukkan banyaknya suku :")

try:
    awal=int(awal)
    selisih=int(selisih)
    suku=int(suku)

    def aritmatika(awal,selisih,suku):
        total=suku/2*((2*awal) + (suku-1)*selisih)
        print("Total dari deret aritmatika tersebut adalah :",float(total))

    aritmatika(awal,selisih,suku)



except:
    print("inputan anda salah")
