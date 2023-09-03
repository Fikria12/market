#init harga
priceApel = 100000
priceJeruk = 15000
priceAnggur = 20000

#init stok
stockApel = 10
stockJeruk = 15
stockAnggur = 8

#deklarasi jumlah buah
def input_fruit(name, stock, price):
    """_summary_

    Args:
        name (_type_): _description_
        stock (_type_): _description_
        price (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        n = int(input(f'Input jumlah {name.capitalize()}: '))
        if n <= stock:
            price = n * price
            break
        else:
            print(f'Jumlah terlalu banyak. {name.capitalize()} sisa {stock}')
    return price, n

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
print( f'''Detail Belanja
Apel   : {nApel} x {priceApel}
Jeruk  : {nJeruk} x {priceJeruk}
Anggur : {nAnggur} x {priceAnggur}
Total  : {priceTotal}''')

while True:
    npembayaran = (int(input('Silahkan masukan nominal uang untuk membayar: ')))
    selisihpembayaran = npembayaran - priceTotal
    if npembayaran < priceTotal:
        print (f'Maaf jumlah kekurangan yang anda harus bayar adalah: Rp. {selisihpembayaran}')
    elif npembayaran > priceTotal:
        print(f'Terimakasih, berikut jumlah kembaliannya:Rp. {selisihpembayaran}')
        break
    else:
        npembayaran == selisihpembayaran
        print(f'Terimakasih')
        break4
        