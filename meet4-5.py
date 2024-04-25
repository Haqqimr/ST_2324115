# inputan dari user
# aritmatika

coba = input("masukkan nama : ")
print ("coba : ", coba, "tipe datanya :", type(coba))

# aritmetika
x = 9
y = 3

# penjumlahan +
hasil = x + y
print(x, '+', y, '=', hasil)

# pengurangan -
x = 10
y = 5

hasil = x - y
print(x, '-', y, '=', hasil)

# perkalian
x = 2
y = 7

hasil = x * y
print(x, '*', y, '=', hasil)

#pembagian
x = 30
y = 2
hasil = x / y
print(x, '/', y, '=', hasil)

# exponen (perpangkatan) **
x = 9
y = 3
hasil = x ** y
print(x, '^', y, '=', hasil)

# modulus (sisa pembagian) %
hasil = x % y
print(x, 'Mod', y, '=', hasil)

# floar division (pembulatan kebawah) //
hasil = x // y
print(x, '//', y, '=', hasil)

# aritmatika prioritas
# () , exponen, perkalian, pembagian, penjumlahan, pengurangan
x = 3
y = 4
z = 5
hasil = ( x ** y * z + x / y - z % x // y)
print(x, '^', y, '*', z, '+', x, '/', y, '-', z, '%', x, '//', y, '=', hasil)
'**' '*' '+' '/' '-' '%' '//'
