kode = input("Masukkan kode barang: ")

match kode:
    case "A01":
        nama = "Snack"
        harga = 10000
    case "A02":
        nama = "Minuman"
        harga = 8000
    case "B01":
        nama = "Mie Instan"
        harga = 3000
    case "B02":
        nama = "Sabun"
        harga = 5000
    case "C01":
        nama = "Shampoo"
        harga = 12000
    case _:
        nama = "Tidak ada"
        harga = 0

print("Nama Barang:", nama)
print("Harga:", harga)