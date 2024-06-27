# program penjumlahan sederhana 
#output seperti berikut

print("silahkan masukkan operasi yang di inginkan")
print("1 - operasi penjumlahan")
print("2 - operasi pengurangan")
pilihan = int(input("masukkan pilihan anda :"))

if pilihan == 1 :
    print ("\n ini operasi penjumlahan")
    bilangan1 = int(input("masukkan bilanga pertama : "))
    bilangan2 = int(input("masukkan bilangan kedua: "))
    hasil = bilangan1 + bilangan2
    print("hasil adalah: ",hasil)
elif pilihan ==2 :
    print ("\n ini operasi pengurangan")
    bilangan1 = int(input("masukkan bilanga pertama : "))
    bilangan2 = int(input("masukkan bilangan kedua: "))
    hasil = bilangan1 - bilangan2
    print("hasil adalah: ",hasil)
else :
    print("pilih angka 1 atau 2")