print ("==================== KASIR ====================")
nahd = int(input("Harga barang : "))
bbam = nahd

while True:
    orgio = input ("Apakah anda membeli barang lagi? [yes/no] :")
    if orgio == ("yes"):
        print (bbam)
        bbam = nahd + bbam


    else: 
        break
