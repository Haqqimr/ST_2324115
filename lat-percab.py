print("Silahkan masukkan operasi yang diinginkan:")
print("1 - Operasi penjumlahan")
print("2 - Operasi pengurangan")
pilihan = int(input("Masukkan pilihan anda: "))

if pilihan == 1:
    print("Ini operasi penjumlahan")
    bilangan_pertama = int(input("Masukkan bilangan pertama: "))
    bilangan_kedua = int(input("Masukkan bilangan kedua: "))
    hasil = bilangan_pertama + bilangan_kedua
    print("Hasil adalah:", hasil)
elif pilihan == 2:
    print("Ini operasi pengurangan")
    bilangan_pertama = int(input("Masukkan bilangan pertama: "))
    bilangan_kedua = int(input("Masukkan bilangan kedua: "))
    hasil = bilangan_pertama - bilangan_kedua
    print("Hasil adalah:", hasil)
else:
    print("Pilihan tidak valid")
