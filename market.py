#init harga
priceApel = 100000
priceJeruk = 15000
priceAnggur = 20000

#input jumlah buah
nApel = int(input("Input jumlah apel: "))
nJeruk = int(input("Input jumlah jeruk: "))
nAnggur = int(input("Input jumlah anggur: "))

#hitung harga per buah
totalPriceApel   = nApel * priceApel
totalPriceJeruk  = nJeruk* priceJeruk
totalPriceAnggur = nAnggur*priceAnggur 

#hitung harga total buah
priceTotal= totalPriceAnggur + totalPriceApel + totalPriceJeruk

#show
print(
    f'''
Detail Belanja

Apel   : {nApel} x {priceApel}
Jeruk  : {nJeruk} x {priceJeruk}
Anggur : {nAnggur} x {priceAnggur}
Total  : {priceTotal}''')