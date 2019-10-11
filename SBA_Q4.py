populasi_digital = int(input('Input Populasi Kota Digital = '))
populasi_talent = int(input('Input Populasi Kota Talent = '))

pertumbuhan_digital = float(input('Input rate pertumbuhan kota Digital = '))
pertumbuhan_talent = float(input('Input rate pertumbuhan kota Talent = '))

tahun = int(input('Tahun '))

def result(populasi_digital,populasi_talent,pertumbuhan_digital,pertumbuhan_talent,tahun):
    
    for i in range(tahun-2019):
        populasi_digital*=(1+pertumbuhan_digital)

    for i in range(tahun-2019):
        populasi_talent*=(1+pertumbuhan_talent)

    result = '\nPopulasi Digital '+str('{0:.5f}'.format(populasi_digital))+'\nPopulasi Talent '+str(populasi_talent)

    return result

print(result(populasi_digital,populasi_talent,pertumbuhan_digital,pertumbuhan_talent,tahun))        


