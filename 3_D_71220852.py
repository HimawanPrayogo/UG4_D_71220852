
kalimat=input("Masukkan sebuah kalimat:").split()


def terpanjang(kalimat):
    a=len(kalimat)
    
    for i in range(0,a,1):
        if len(kalimat[i])>len(kalimat[i-1]):
            maks=kalimat[i]

            print("Kata terpanjang dalam kalimat tersebut adalah: ",maks)
        
        

terpanjang(kalimat)
