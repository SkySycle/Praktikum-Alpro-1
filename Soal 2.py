beli1 = 650000 * 25
beli2 = 685000 * 15 
jual1 = 685000 * 25
jual2 = 715000 * 40 
hargabeli = beli1 + beli2
untung1 = jual1 - beli1
untungpersen1 = (untung1 / beli1) * 100
untung2 = jual2 - hargabeli 
untungpersen2 = (untung2 / hargabeli) * 100
print ("Keuntungan Rupiah Gerard = Rp.",untung1)
print ("Keuntungan Persen Gerard = ",round (untungpersen1, 2),"%")
print ("Keuntungan Gerard (dalam Rupiah, harga baru)",untung2)
print ("Keuntungan Gerard (dalam persentase, harga baru) = ",round (untungpersen2, 2),"%")