
bilangan=input("Masukkan sekumpulan bilangan (pisahkan dengan koma):").split(",")


a=len(bilangan)

for i in range(0,a,1):
    aa=bilangan[i]
    bb=bilangan[i-1]

    if aa>bb:
        maks=aa

    elif aa<bb:
        minim=aa
    
print("")
print("Bilangan terbesar dari kumpulan bilangan yang di input adalah",maks)
print("Bilangan terkecil dari kumpulan bilangan yang di input adalah",minim)


            

