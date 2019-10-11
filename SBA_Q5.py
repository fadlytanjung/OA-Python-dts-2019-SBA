gaji_per_jam = int(input('Gaji per jam yang anda inginkan : '))
jumlah_jam_kerja = int(input('Jumlah jam kerja yang akan dilakukan dalam 1 minggu : '))

# rules
total_gaji = gaji_per_jam*jumlah_jam_kerja
gaji_setelah_pajak = total_gaji*(1-0.14)
beli_baju_aksesoris = gaji_setelah_pajak*0.1
beli_alat_tulis = gaji_setelah_pajak*0.01
sisa_gaji_setelah_beli_baju_aksesoris = gaji_setelah_pajak-beli_baju_aksesoris
sisa_setelah_alat_tulis = sisa_gaji_setelah_beli_baju_aksesoris-beli_alat_tulis

untuk_sedekah = sisa_setelah_alat_tulis*0.25

untuk_anak_yatim = ((untuk_sedekah//1000)*0.3)*1000
untuk_anak_dhuafa = ((untuk_sedekah//1000)*0.7)*1000

print('Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak : '+str(total_gaji)+'\n')
print('Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak : '+str(gaji_setelah_pajak)+'\n')
print('Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris : '+str(beli_baju_aksesoris)+'\n')

print('Jumlah uang yang akan Budi habiskan untuk membeli alat tulis : '+str(beli_alat_tulis)+'\n')

print('Jumlah uang yang akan Budi sedekahkan : '+str(untuk_sedekah)+'\n')

print('Jumlah uang yang akan diterima anak yatim : '+str(untuk_anak_yatim)+'\n')

print('Jumlah uang yang akan diterima kaum dhuafa : '+str(untuk_anak_dhuafa)+'\n')
