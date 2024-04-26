# input dari user

coba = input("masukkan nilai")
print("coba : ","tipe datanya:",type(coba))

# aritmatika
x = 10
y = 3

# penjualan +
hasil = x + y
print(x,"+",y,"=",hasil)

# pengurangan -
hasil = x - y
print(x,"-",y,"=",hasil) 

# perkalian =
hasil = x * y
print(x,"*",y,"=",hasil)

# pembagian /
hasil = x / y
print(x,"/",y,"=",hasil)

#exponan (perpangkatan)**
hasil = x ** y
print(x,"**",y,"=",hasil)

#modulus (sisa bagi) %
hasil = x % y
print(x,"%",y,"=",hasil)

# floor division (pembulatan kebawah) //
hasil = x // y
print(x,"//",y,"=",hasil)

# aritmatika prioritas 
# () , exponen, perkalian, penjualan 
x = 3
y = 4
z = 5
hasil = ( x ** y * z + x / y - z % x // y )
print(x,"**",y,"*",z,"+",x,"/",y,"-",z,"%",x